#define RPWM1 5
#define LPWM1 6
#define ENCA1 2
#define ENCB1 3

//ROS
#include <ros.h>
#include <std_msgs/Float64.h>
#include <std_msgs/Int64.h>
#include <std_msgs/Int16.h>

// Error
float error;

//PID
float kp =  0.4137 ;
float ki = kp * 0.9 ;
float kd = kp * 0.00001 ;
float dt = 1;
float prevError;
float integral;
float derivative;
float PID;

// RPM
unsigned long currentMillis, previousMillis;

//PWM
float pwm1;

//ENCODER
long pulse = 0;
volatile long previousEncoder = 0;
volatile long currentEncoder;

// MOTOR
const int ppr = 7; //define number of pulses in one round of encoder
const float GR = 1 / 19.2; //gear ratio
const float R = 0.538048496; //load (omniwheel) ratio
//RPM
float RPM;           //rotating speed in rad/s
float old_RPM = 0;
float new_RPM = 0;
//rad/s
float RPS;
float old_RPS = 0 ;
float new_RPS = 0;
//m/s
float Vel;
float old_Vel = 0;
float new_Vel = 0;
const int interval = 100; //choose interval is 0.1 second (100 milliseconds)

float set_point = 0;
int pulse_pub = 0;

//ROS

ros::NodeHandle nh;
std_msgs::Int64 encoder;

void set_point_callback(const std_msgs::Float64& set_point_3) {
  set_point = set_point_3.data;
}

void pulse_callback(const std_msgs::Int64& pulse_3) {
  pulse_pub = pulse_3.data;
}

ros::Subscriber<std_msgs::Float64> sub("/V3", &set_point_callback);
ros::Publisher encoderValue("/encoderValue_3", &encoder);

void setup() {
  nh.getHardware()->setBaud(57600);
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(encoderValue);

  pinMode (ENCA1, INPUT);
  pinMode (ENCB1, INPUT);

  pinMode(RPWM1, OUTPUT);
  pinMode(LPWM1, OUTPUT);

  digitalWrite(ENCA1, HIGH);
  digitalWrite(ENCB1, HIGH);

  attachInterrupt(digitalPinToInterrupt(ENCA1), readEncoder, CHANGE);
  //  Serial.begin(9600);/
}

void loop() {
  readSpeed();
  nh.loginfo("Encoder_Value_3");

  encoder.data = pulse;
  encoderValue.publish(&encoder);

  nh.spinOnce();
  delay(100);
}

void readEncoder() {
  if (digitalRead(ENCA1) == digitalRead(ENCB1)) {
    pulse--;
  } else {
    pulse++;
  }
}

void readSpeed() {
  currentEncoder = pulse;
  currentMillis = millis();
  if (currentMillis - previousMillis > interval)
  {
    previousMillis = currentMillis;
    RPM = (float)((((currentEncoder - previousEncoder) * 600) / ppr) * GR) ;
    RPS = (float)((RPM * 2 * 3.14) / 600); // konversi Rotasi per menit ke Radian per sekon dikali keliling roda dan dibagi waktu
    Vel = (float)(RPS * 0.05); // kecepatan linear adalah kecepatan sudut dikali dengan jari jari roda

    previousEncoder = currentEncoder;
    new_RPM = RPM;
    new_RPS = RPS;
    new_Vel = Vel;

    error = abs(set_point) - abs(new_Vel);
    integral += error * dt;
    derivative = ((error - prevError)  / dt );

    PID = (kp * error) + (ki * integral) + (kd * derivative);
    prevError = error;

    pwm1 =  ((499.44 * PID) + 5.221);
    pwm1 = min(max(pwm1, 0), 255);
    
//    PID = min(max(PID, 0), 255);
//    pwm1 =  ((499.44 * PID) + 5.221);

    old_RPM = new_RPM;
    old_RPS = new_RPS;
    old_Vel = new_Vel;

    if (pwm1 >= 0) {
      analogWrite(LPWM1, pwm1);
    }
    else if (pwm1 <= 0) {
      analogWrite(RPWM1, pwm1);
    }
  }
}
