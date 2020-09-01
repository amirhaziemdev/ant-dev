
/*!
* @file QuadMotorDriverShield.ino
* @brief QuadMotorDriverShield.ino  Motor control program
*
* Every 2 seconds to control motor positive inversion
*
* @author linfeng(490289303@qq.com)
* @version  V1.0
* @date  2016-4-5
*/
const int E1 = 3; ///<Motor1 Speed
const int E2 = 11;///<Motor2 Speed

const int M1 = 4; ///<Motor1 Direction
const int M2 = 12;///<Motor2 Direction

void M1_forward(char Speed) ///<Motor1 Advance
{
 digitalWrite(M1,LOW);
 analogWrite(E1,Speed);
}
void M2_forward(char Speed) ///<Motor2 Advance
{
 digitalWrite(M2,HIGH);
 analogWrite(E2,Speed);
}

void M1_reverse(char Speed) ///<Motor1 Back off
{
 digitalWrite(M1,HIGH);
 analogWrite(E1,Speed);
}
void M2_reverse(char Speed) ///<Motor2 Back off
{
 digitalWrite(M2,LOW);
 analogWrite(E2,Speed);
}

void stop_all(){
  M1_forward(0);
  M2_forward(0);
}

void setup() {
  for(int i=3;i<9;i++)
    pinMode(i,OUTPUT);
  for(int i=11;i<13;i++)
    pinMode(i,OUTPUT);
}

void loop() {
  M1_forward(100);
  M2_forward(100);
  delay(2000); ///<Delay 2S
  M1_reverse(100);
  M2_reverse(100);
  delay(2000); ///<Delay 2S
  stop_all();
}
