int number=7;

void setup() {
  Serial.begin(9600);
  
  pinMode(number, OUTPUT);
  digitalWrite (number, LOW);
}

void loop() {
  
  while (Serial.available()) {
    int data = Serial.read();

    if (data == '1')
      digitalWrite (number, HIGH);

    else if (data == '0')
      digitalWrite (number, LOW);
  }
}
