//Wechselspannung: Sinusförmige Spannung mittels PWM erzeugen
//Deklaration und Initialisierung globaler Variablen 
const int AnalogPin = 9 ; //Deklaration PWM-Analog Pin 9

float t = 0.f ; // Momentanwert der Zeit in Millisekunden
float T = 0.f ; // Periodendauer in Millisekunden
const float U_ref = 5.f ; //Referenzspannung in Volt
int PWM_Value = 0 ; //Parameterwert für analogWrite
unsigned int AD_Value = 0 ; //Parameterwert für analogRead
float ReadVoltage = 0.f ; //Gemessene Spannung in Volt
float Skal_Amplitude = 0 ; //Berechnete Amplitude
/**********************************************************/
//Einstellbare Parameter: 
float Amplitude = 0.5f ; //Amplitude in Volt (0 - 2.5 V)
unsigned int Frequenz = 5 ; //Frequenz in Hertz (max 20Hz)
/**********************************************************/

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //Initialisierung Serielle Kommunikation 115200 Baud
  TCCR1B = (TCCR1B & 0b11111000) | 0x01 ; //Änderung der PWM-Frequenz des Analog Pins 9 und 10 auf 31372 Hz
  //Quelle: http://playground.arduino.cc/Main/TimerPWMCheatsheet

  Skal_Amplitude = Amplitude * (254.f / U_ref) ; //Berechnung/Anpassung der Amplitude für analogWrite
  T = (1.f / Frequenz) * 1000.f ; //Berechnung der Periodendauer mittels der Frequenz
}

void loop() {
  // put your main code here, to run repeatedly:
  t = millis()%(int)T ; //Laufzeit des Arduinos, Berechnung des Rests der Division durch Periodendauer 

  //Sinusfunktion
  PWM_Value = (int) ( Skal_Amplitude * sin ((t/T) * 2.f * PI) ) ;  //Berechnung der Sinusfunktion und Skalierung
  PWM_Value += 127 ;                  //Addition des Offsets

  //Sägezahnspannung

  //Rechteckspannung
  
  //Dreieckspannung
  
  analogWrite(AnalogPin ,PWM_Value);  //PWM-Ausgabe an Pin 9

  AD_Value = analogRead(A0) ;         //Analogen Wert an Pin A0 einlesen

  ReadVoltage = (float)AD_Value * (U_ref/1023.f) ;  //Berechnung der momentan anliegenden Spannung

  Serial.println(ReadVoltage);        //Ausgabe der momentanen Spannung über UART
//Ergebnissanzeige mittels Werkzeuge->Serieller Plotter (aktuelle Arduino Version  1.6.9 installieren!)
//  delay(1) ;
}
