const int AirValue = 560;   //you need to replace this value with Value_1
const int WaterValue = 280;  //you need to replace this value with Value_2
int soilMoistureValue = 0;
int soilmoisturepercent=0;
const int LightValue = 75;
const int DarkValue = 1000;
int ldr_value = 0;
int ldr_percent = 0;
#include <dht.h>
dht DHT;

int thermistor_value = 0;
String concat_values = "";

void setup() {
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop() {
soilMoistureValue = analogRead(A0);  //put Sensor insert into soil
//Serial.println(soilMoistureValue);
soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);
ldr_percent = map(ldr_value, DarkValue, LightValue, 0, 100);
int chk = DHT.read11(2);
ldr_value = analogRead(A1);
thermistor_value = analogRead(A2);
if(soilmoisturepercent > 100)
{
  soilmoisturepercent = 100;
  //Serial.println("100 %");
}
else if(soilmoisturepercent <0)
{
  soilmoisturepercent = 0;
//  Serial.println("0 %");
}
if(ldr_percent > 100)
{
  ldr_percent = 100;
}
else if(ldr_percent < 0)
{
  ldr_percent = 0;
}
concat_values = "start," + String(DHT.temperature) + "," + String(DHT.humidity) +  "," + String(ldr_percent) +  "," + String(thermistor_value) +  "," + String(soilmoisturepercent) + ",end";
  Serial.println(concat_values);
  
  /*Serial.println(DHT.humidity);
  Serial.println(ldr_value);
  Serial.println(thermistor_value);*/
  delay(2500);
}
