// Подключаем необходимые библиотеки
#include <OneWire.h>
#include <DallasTemperature.h>
#include <SIM800L.h>

SIM800L sim800l(3, 2); //Rx, Tx
String PHONE = "+7<>";   // Fhone to send  Alarm SMS
String phones = "+7<>";  // Wite list number


#define ONE_WIRE_BUS 11

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);


void handleSMS(String number, String message) {
  Serial.println("number: " + number + "\nMessage: " + message);
  if (message == "Temp" && phones.indexOf(number) > -1) {
    Serial.println("New sms from " + number);
    float temp = sensors.getTempCByIndex(0);
    sim800l.sendSMS(number, "Temperature: " + String(temp));
    Serial.println("Temperature : " + String(temp) + " Sended to " + number);
    }
  }

void handleCall(String number) {
  Serial.println("New call from " + number);
  //float temp = sensors.getTempCByIndex(0);
  //sim800l.sendSMS(number, "Temperature: " + String(temp));
  //Serial.println("Temperature : " + String(temp) + " Sended to " + number);
  //delay(10000); // 15 sec

}


void setup(void)
{
  Serial.begin(9600);
  sensors.begin();

  sim800l.begin(9600);

  sim800l.setSMSCallback(handleSMS);
  sim800l.setCallCallback(handleCall);
}



void loop(void)
{
  sim800l.listen();
	sensors.requestTemperatures();

  //float temp_notufy = sensors.getTempCByIndex(0);
  //int count = 0;
  //if(String(temp_notufy) < "10.0" && count < 1){
  //  Serial.println("Temperature < 10.0");
  //  sim800l.sendSMS(PHONE, "Temperature Alarm: " + String(temp_notufy));
  //  count++;
  //  delay(300);
//
  //if (count == 1){
  //  count = 1;
  //}
  //}
}
