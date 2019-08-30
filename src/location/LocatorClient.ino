// Listens for beacon signals to extract name and RSSI for trilateration.

#include <string.h>
#include <BLEDevice.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>

typedef struct BeaconReading BeaconReading;
struct BeaconReading {
  char name[20];
  int rssi;
};



float distanceFromRSSI(int rssi) {
  return -0.4274385+0.04534152/pow(2, rssi/9.227183);
}

int compare(const void* a, const void* b) {
  BeaconReading *first = (BeaconReading*)a;
  BeaconReading *second = (BeaconReading*)b;
  return strcmp(first->name, second->name);
}

BLEScan* BLEScan; //Creates scan class to call
int debugging = 1;
const int packetSize = 500; //Size of one packet to send (in characters)
//Extract name from given string of beacon data
char *getName(const char* data) {
  char dataBuffer[100] = {};
  strcpy(dataBuffer, data);
  char *name = (char*)malloc(20*sizeof(char));
  char *returnPointer = name;
  int start = 0;                                          //If name characters have begun
  int end = 0;                                            //If name characters have ended
  int i = 0; int j = 0;                                   //Data and Name index
  while (end != 1) {                                      //Loop until name is copied
    if(dataBuffer[j] == 44) {end == 1; start = 0; break;} //Stops copying at first ,-character, stops loop so it doesn't copy
    if(dataBuffer[j] == 32) {start = 1; j++;}             //At first space, start copying: Also skips all spaces in name
    if (start == 1) {name[i] = dataBuffer[j]; i++;}       //Copies current index of data to name buffer
    j++;
  }
    name[i] = 0;
    return returnPointer;
};

char *dataBuffer; //Global variable for a string of data to be transmitted
BeaconReading *scannedBeacons; //Global array of scanned beacons and their RSSI
int beaconAmount = 0;
int dataPackets = 0;

//Creates a packet of data with all beacon and sensor readings
char *createData() {
  char *createdPacket = (char*)malloc(sizeof(char)*100);
  sprintf(createdPacket, "<%d", millis());
  qsort(scannedBeacons, beaconAmount, sizeof(BeaconReading), compare);
  for (int i = 0; i < beaconAmount;i++) {
    char *temporaryData = (char*)malloc(sizeof(char)*20);
    sprintf(temporaryData, "#%s/%d", scannedBeacons[i].name, scannedBeacons[i].rssi);
    strcat(createdPacket, temporaryData);
    free(temporaryData);
  }
  //char *temporaryData = (char*)malloc(sizeof(char)*30);
  //sprintf(temporaryData, "#Breathing/%d#Heart/%d\n", breathing, heart);
  //strcat(createdPacket, temporaryData);
  //free(temporaryData);
  strcat(createdPacket, ">");
  return createdPacket;
};

//Sends the buffered packet and resets it.
void sendPacket() {

  Serial1.printf(dataBuffer);
  memset(dataBuffer, 0, packetSize*sizeof(char));
};

//Adds given string to the buffer to send at a later date
void buffer(char *dataString) {
  if(strlen(dataBuffer) < packetSize-strlen(dataString)) {
    dataPackets++;
    strcat(dataBuffer, dataString);
  } else {
    Serial.print("The buffer is full! Send the data forward.\n");
    sendPacket();
    };
};


//The BeaconData class represent a singular found beacon; It prints the name and RSSI to the serial port for debugging
class BeaconData: public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) {
    if(strstr(advertisedDevice.toString().c_str(), "Beacon") != NULL) { //We're only interested in beacons
      char *beaconInfo = (char*)advertisedDevice.toString().c_str();
      char *beaconName = getName(beaconInfo);
      beaconAmount++;
      scannedBeacons = (BeaconReading*)realloc(scannedBeacons, sizeof(BeaconReading)*beaconAmount);
      strcpy(scannedBeacons[beaconAmount-1].name, beaconName);
      scannedBeacons[beaconAmount-1].rssi = advertisedDevice.getRSSI();
      free(beaconName);
    }
  }
};

void startBLE() {
  BLEDevice::init("Locator");
  BLEScan = BLEDevice::getScan(); //Create new scan object
  BLEScan->setAdvertisedDeviceCallbacks(new BeaconData());
  BLEScan->setActiveScan(true); //Active scan uses more power, but get results faster
  esp_ble_tx_power_set(ESP_BLE_PWR_TYPE_SCAN, ESP_PWR_LVL_P9);
  BLEScan->setInterval(100);
  BLEScan->setWindow(99);  // less or equal setInterval value
  
}




void setup() {
  Serial.begin(115200);
  Serial1.begin(9600, SERIAL_8N1, 16, 17);
  startBLE();
  dataBuffer = (char*)calloc(packetSize, sizeof(char)); //Initialize global data buffer


}

void loop() {
  scannedBeacons = (BeaconReading*)calloc(1, sizeof(BeaconReading)); //Initialize global beacon buffer
  BLEScanResults beacons = BLEScan->start(1, false);
  char *dataPacket = createData();
  sendPacket();
  if(debugging == 1) {Serial.printf("New datapacket: %s\n", dataPacket);};
  buffer(dataPacket);
  sendPacket();
  free(dataPacket);
  free(scannedBeacons); //Reset found beacons
  beaconAmount = 0;
  //Serial.printf("\nCurrent buffer:\n %s\n", dataBuffer);
  delay(500);
}
