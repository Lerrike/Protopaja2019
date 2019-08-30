#include <WiFi.h>
#include <string.h>
#include <beacon.h>
#include <test_trilateration.h>
#include <trilateration.h>
#include <map>
#include <iostream>
#include <stdlib.h>

// Most of the beacon algorithms are taken from Navigine open source trilateration code.

//char WIFI_SSID[]="Sampsa-PC";
//char WIFI_PASSWORD[]="Miesluola1";
char WIFI_SSID[]="aalto open";
char WIFI_PASSWORD[]="";
int status = WL_IDLE_STATUS;

Beacon beacon; //Holder for currently operated beacon
BeaconMeas beaconData; //Holder for storing RSSI data of a single beacon
Trilateration trilateration;
std::vector<BeaconMeas> beaconMeasurements;
std::vector <Beacon> knownBeacons; //Array of known beacon locations
std::map<std::string, char*> beaconNames = {};
double x = 0;
double y = 0;
//Add all beacon names here
void addKnownBeacons() {
  //Beacon Name / Beacon UUID / Beacon X coordinate / Beacon Y Coordinate
  addBeacon("Beacon1", "f7fdb76e-7ef1-4333-86aa-aff71e769276", 0, 0);
  addBeacon("Beacon2", "44616f19-c598-456d-a1ef-2ecbd986794d", 3.02, 0);
  addBeacon("Beacon3", "3f21a6ea-5b3f-45d3-b7ec-42699025977d", 0, 3.7);
  addBeacon("Beacon4", "6e524cba-98db-4e38-870c-6e63d5257476", 3.02, 3.7);
}


//Connects to a Wi-Fi with defined SSID and password
void connectWifi() {
  while (status != WL_CONNECTED){
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(WIFI_SSID);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    delay(2000);
    }
  Serial.println("Connected to wifi");
}
//Adds a beacon to known beacon coordinates
void addBeacon(char* beaconName, char* uuid, float xCoord, float yCoord) {
  beaconNames.insert(std::pair<char*, char*>(beaconName, uuid));
  setBeacon(xCoord, yCoord, uuid, beaconName, "TestArea");
}
//Helper function for addBeacon
void setBeacon(float xCoord, float yCoord, char* UUID, char* beaconName, char* location) {
  beacon.fillData(xCoord, yCoord, UUID, beaconName, location);
  knownBeacons.push_back(beacon);
}
//Transfers RSSI value into a distance value (in metres)
float distanceFromRSSI(int rssi) {
  return 0.5*exp(1.0/21.0*(-rssi-52.0));
}

//Sets individual reading of a single beacon to given value
void setReading(char* beaconName, float rssi) {
  beaconData.setBeaconId(beaconNames[std::string(beaconName)]);
  beaconData.setRssi(rssi);
  beaconData.setDistance(distanceFromRSSI(rssi));
  beaconMeasurements.push_back(beaconData);
}

void readBeacon(char *string) {
  char beaconName[30];
  int nameLength = strlen(string)-strlen(strstr(string, "/"));
  int rssi = atoi(strstr(string, "/")+1);
  memcpy(beaconName, string, (sizeof(char)*nameLength));
  beaconName[nameLength] = '\0';
  printf("Name: %s | RSSI: %.2F\n", beaconName, float(rssi));
  setReading(beaconName, float(rssi));
   
}

int addBeaconReadings(char* processedPacket) {
  char str[80];
  char beaconStr[80];
  strcpy(str, processedPacket);
  const char delimiter[2] = "#";
  char *token;
  char *beaconToken;
  token = strtok(str, delimiter);
  int timestamp = 0;
    while( token != NULL ) {
    if(timestamp != 0) {
      strcpy(beaconStr, token);
      readBeacon(beaconStr);
    } else {
      timestamp = atoi(token);
    }
    token = strtok(NULL, delimiter);
   }
   return timestamp;
}



int breathingGPIO = 34; //A2 on Feather
//Returns current reading of breathing sensor
int getBreathing() {
  int breathingValue = analogRead(breathingGPIO);
  //if (debugging == 1) {Serial.printf("Breathing: %d\n", breathingValue);}
  return breathingValue;
};

int heartGPIO = 4; //A5 on Feather
//Returns current reading of heart sensort
int getHeart() {
  int heartValue = analogRead(heartGPIO);
  //if (debugging == 1) {Serial.printf("Heart: %d\n", heartValue);}
  return heartValue;
};

const byte numChars = 190;
char receivedChars[numChars];

int newData = 0;
int ndx = 0;

//Reads a datapacket from serial connection
void getPacket() {
    static int inProgress = 0;
    char startMarker = '<';
    char endMarker = '>';
    char received;
    
    while (Serial1.available() > 0 && newData == 0) {
        received = Serial1.read();
        if (inProgress == 1) {
          if (received != endMarker) {
            receivedChars[ndx] = received;
            ndx++;
            if (ndx >= numChars) {
              ndx = numChars - 1;
            }
          } else {
              receivedChars[ndx] = '\0'; // terminate the string
              inProgress = 0;
              ndx = 0;
              newData = 1;
              addBeaconReadings(receivedChars);
              //sendString(receivedChars);
              trilaterate();
              memset(receivedChars, 0, sizeof(receivedChars));
              newData = 0;
            }
          } else if (received == startMarker) {
            //receivedChars[ndx] = '';
            //ndx++;
            inProgress = 1;
        }
    }
}
//Combines beacon data from BLE with breathing and heart sensor data
void processPacket(float x, float y, int breathing, int heart) {
    if (newData == 1) {
        char *createdPacket = (char*)malloc(sizeof(char)*200);
        memset(createdPacket, 0, 200);
        sprintf(createdPacket, "#Name/Prototyyppi2#x/%.2f#y/%.2f", x, y);
        char *temporaryData = (char*)malloc(sizeof(char)*35);
        sprintf(temporaryData, "#Breathing/%d#Heart/%d\n", breathing, heart);
        strcat(createdPacket, temporaryData);
        free(temporaryData);
        sendString(createdPacket);
        Serial.print(createdPacket);
        free(createdPacket); //Process packet, needs implementation
    }
}

char *dataBuffer; //Global variable for a string of data to be transmitted
int dataPackets = 0;
const int packetSize = 500; //Size of one packet to send (in characters)
  
void buffer(char *dataString) {
  if(strlen(dataBuffer) < packetSize-strlen(dataString) && dataPackets != 3) {
    dataPackets++;
    strcat(dataBuffer, dataString);
  } else if (dataPackets == 3) {
    //Needs implementation of handling buffer
    memset(dataBuffer, 0, packetSize*sizeof(char));
    dataPackets = 0;
  } else {
    Serial.print("Buffer is full. Transmitting...\n");
    //Needs implementation of handling full buffer
    memset(dataBuffer, 0, packetSize*sizeof(char));
    dataPackets = 0;
    };
};

//Get X and Y coordinates from beacon RSSIs and known beacon locations.
void trilaterate() {
  trilateration.updateMeasurements( beaconMeasurements );
  int errorCode = trilateration.calculateCoordinates();
  printf( "x = %lf y = %lf \n", trilateration.getX()-x, trilateration.getY()-y );
  //The library doesn't clear the X and Y coordinates, hence the "-x" and "-y" of old location values
  processPacket(trilateration.getX()-x, trilateration.getY()-y, 1, 1); //Process the current location
  x = trilateration.getX();
  y = trilateration.getY();
}

TaskHandle_t Task1;

void setup() {
  Serial.begin(115200); //Start serial for debugging
  Serial1.begin(9600, SERIAL_8N1, 16, 17); //Start communication between ESP32s
  dataBuffer = (char*)calloc(packetSize, sizeof(char)); //Initialize global data buffer
  connectWifi();
  addKnownBeacons();
  trilateration.setCurrentLocationId( 0 );
  trilateration.fillLocationBeacons(knownBeacons);
  xTaskCreatePinnedToCore(
      sensorLoop, //Name of function that runs the task
      "Task1",    //Name of task
      10000,      //Stack size
      NULL,       //Task input param.
      0,          //Task priority
      &Task1,     //Task handle
      0);         //Task core
      
}

//Beacon data processing loop running on core 1
void loop() {
  getPacket();
}

WiFiClient client;
const uint16_t port = 8090;
//const char * host = "82.130.28.134";
const char * host = "10.100.59.94";


void sendString(char *dataString) {
  WiFiClient client;
  if (!client.connect(host, port)) {
    Serial.println("Connection to host failed");
    delay(1000);
    return;
  }
  String clientString = String(dataString);
  client.print(clientString);
  client.stop();
}
//Sensor signal processing loop running on core 0
void sensorLoop(void * parameter) {
for(;;) {
  
  //Add sensor reading and processing here
  delay(1000);
}
}
