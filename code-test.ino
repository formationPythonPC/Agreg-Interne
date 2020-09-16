void setup() {
  // put your setup code here, to run once:
pinMode(13, OUTPUT) ; // la broche 13 (LED de la carte) est vue comme une sortie
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(13, HIGH) ; // on place la broche 13 à l'état haut (5 Volts)
delay(500) ;// on attend 500 ms
digitalWrite(13, LOW) ; // on place la broche 13 à l'état bas (0 Volt)
delay(300) ;// on attend 300 ms 
}
