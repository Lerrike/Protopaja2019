/*
  Creates a beacon to send out a bluetooth signal for a tracker to pick up and get RSSI from
  for distance measurement. At least 3 beacons are required for trilateration to work.
*/
#include "sys/time.h"
#include "BLEDevice.h"
#include "BLEUtils.h"
#include "BLEBeacon.h"
#include "esp_sleep.h"


BLEAdvertising *Advertising;

void createBeacon() {

  BLEBeacon Beacon = BLEBeacon();
  Beacon.setManufacturerId(0x4C00); // fake Apple 0x004C LSB (ENDIAN_CHANGE_U16!)
  Beacon.setProximityUUID(BLEUUID("f7fdb76e-7ef1-4333-86aa-aff71e769276"));
  Beacon.setMajor(100);  //Sets two unique identifiers on top of the UUID; Needs a better implementation.
  Beacon.setMinor(1);
  BLEAdvertisementData AdvertisementData = BLEAdvertisementData();
  BLEAdvertisementData ScanResponseData = BLEAdvertisementData();
  
  AdvertisementData.setFlags(0x04); // BR_EDR_NOT_SUPPORTED 0x04

  //Advertisement data shown
  std::string strServiceData = "Aboense Locator Beacon";
  
  strServiceData += (char)26;     // Len
  strServiceData += (char)0xFF;   // Type
  strServiceData += Beacon.getData(); 
  AdvertisementData.addData(strServiceData);
  AdvertisementData.setName("Beacon 1"); //Configures the beacon name
  Advertising->setAdvertisementData(AdvertisementData);
  Advertising->setScanResponseData(ScanResponseData);

}

void setup() {
  BLEDevice::init("");
  Advertising = BLEDevice::getAdvertising();
  createBeacon();
}

void loop() {
  esp_ble_tx_power_set(ESP_BLE_PWR_TYPE_ADV, ESP_PWR_LVL_P1);
  Advertising->start();
  delay(100);
  Advertising->stop();
  delay(5000);
}
