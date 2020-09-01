/*
 * Amir Haziem Razali
 * Serial Comms with Python
 * 20/08/2020
 */

const int E1 = 3; ///<Motor1 Speed
const int E2 = 11;///<Motor2 Speed

const int M1 = 4; ///<Motor1 Direction
const int M2 = 12;///<Motor2 Direction

const int med_speed = 100; //medium speed
const int full_speed = 255; //full speed


void M1_forward(char Speed) ///<Motor1 forward
{
 digitalWrite(M1,LOW);
 analogWrite(E1,Speed);
}
void M2_forward(char Speed) ///<Motor2 forward
{
 digitalWrite(M2,LOW);
 analogWrite(E2,Speed);
}
void M1_reverse(char Speed) ///<Motor1 reverse
{
 digitalWrite(M1,HIGH);
 analogWrite(E1,Speed);
}
void M2_reverse(char Speed) ///<Motor2 reverse
{
 digitalWrite(M2,HIGH);
 analogWrite(E2,Speed);
}

void forward(char Speed){
  M1_forward(Speed);
  M2_forward(Speed);
}

void reverse(char Speed){
  M1_reverse(Speed);
  M2_reverse(Speed);
}

void left(char Speed){
  M1_forward(Speed);
  M2_reverse(Speed);
}

void right(char Speed){
  M1_reverse(Speed);
  M2_forward(Speed);
}

void stop_all(){ //Stop both motors
  M1_forward(0);
  M2_forward(0);
}

void setup() {
  Serial.begin(115200);
  for(int i=3;i<9;i++)
    pinMode(i,OUTPUT);
  for(int i=11;i<13;i++)
    pinMode(i,OUTPUT);
}

void loop() {
  if(Serial.available() > 0){
    char data = Serial.read(); //read a byte
    char str[2];
    str[0] = data;
    str[1] = '\0';
    Serial.print(str);
    if(*str=='w'){
      forward(med_speed);
    }else if(*str=='s'){
      reverse(med_speed);
    }else if(*str=='d'){
      right(med_speed);
    }else if(*str=='a'){
      left(med_speed);
    }else if(*str=='e'){
      stop_all();
    }
  }
}
