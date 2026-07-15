# 🌡️ Lab 10 - Smart Weather Monitor
### Team 7 | EEC3612 Embedded Systems Lab (Week 12)

![RaspberryPi](https://img.shields.io/badge/Raspberry_Pi-3_Model_B-C51A4A)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![DHT11](https://img.shields.io/badge/Sensor-DHT11-orange)
![LDR](https://img.shields.io/badge/Sensor-LDR-yellow)
![I2C_LCD](https://img.shields.io/badge/Display-I2C_LCD-blue)

---

## 👥 Team Members

| Name | Role |
|------|------|
| **Ravan Jafarov** | Team Leader, Hardware & Circuit Setup |
| Azar Aslanov | Hardware (DHT11 & LDR wiring) |
| Riad Alizada | Code (Task 1 - Weather Monitor) |
| Hasan Aliyev | Code (Task 2 - Servo Fan Control) |

📅 **Date:** November 2025  
🎓 **Professor:** Kim Deokhwan  
🛠️ **LA:** Rasim Mahmudov

---

## 🎯 Objective

Build a **Smart Weather Monitor** using Raspberry Pi 3 that:
- Reads **temperature & humidity** from DHT11 sensor
- Detects **ambient light** using LDR (Light Dependent Resistor)
- Displays information on **I2C LCD**
- Activates **LEDs & Buzzer** when temperature exceeds threshold
- (Task 2) Controls a **Servo Motor** as a simulated fan

---

## 🔧 Components Used

| Component | Description |
|-----------|-------------|
| Raspberry Pi 3 Model B | Main controller |
| DHT11 Sensor | Temperature & Humidity sensor |
| LDR (Light Dependent Resistor) | Ambient light detection |
| I2C LCD (PCF8574, 0x27) | 16x2 Display |
| Red LED | High temperature alert |
| Green LED | Normal temperature indicator |
| Buzzer | Audio alert |
| SG90 Servo Motor | Simulated fan (Task 2) |
| Breadboard & Jumper Wires | For connections |

---

## 📂 Project Structure

```
lab10-smart-weather-monitor-team7/
├── README.md
├── task1_weather_monitor/
│   └── pyfile_no_servo.py
├── task2_fan_servo/
│   └── pyfile_servo.py
└── images/
    ├── task1_circuit.jpg
    └── task2_circuit.jpg
```

---

## ⚙️ Raspberry Pi Configuration

### 1. Enable I2C
```bash
sudo raspi-config
```
Go to: **Interface Options** → **I2C** → **Enable** → **Finish** → **Reboot**

### 2. Create Virtual Environment
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Required Libraries
```bash
pip install adafruit-circuitpython-dht RPLCD gpiozero pigpio
```

### 4. Enable pigpio Service (for Servo)
```bash
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
```
*(Password: `123`)*

---

## 🔌 Circuit Setup

### Task 1: Weather Monitor
| Component | Raspberry Pi GPIO |
|-----------|-------------------|
| DHT11 Data | GPIO 4 |
| LDR Output | GPIO 18 |
| Red LED | GPIO 17 |
| Green LED | GPIO 27 |
| Buzzer | GPIO 22 |
| LCD SDA | GPIO 2 (SDA) |
| LCD SCL | GPIO 3 (SCL) |

### Task 2: Add Servo Motor
| Component | Raspberry Pi GPIO |
|-----------|-------------------|
| SG90 Servo Signal | GPIO 23 |

---

## 💻 Task 1: Smart Weather Monitor (No Servo)

### Purpose
Monitor temperature, humidity, and light levels. Display on LCD and alert with LED + Buzzer when temperature > 30°C.

### Code
👉 See [`task1_weather_monitor/pyfile_no_servo.py`](task1_weather_monitor/pyfile_no_servo.py)

### How to Run
```bash
source myenv/bin/activate
python3 pyfile_no_servo.py
```

Or download directly on RPi:
```bash
wget https://rasimmax.com/fsm/pybook/pyfile_no_servo.py
```

---

## 💻 Task 2: Add Servo Motor (Fan Simulation)

### Purpose
Extend Task 1 by adding a servo motor that simulates a fan. When temperature > 27°C:
- Red LED + Buzzer activate
- Servo rotates (fan ON)
- When temperature drops, fan turns OFF

### Code
👉 See [`task2_fan_servo/pyfile_servo.py`](task2_fan_servo/pyfile_servo.py)

### How to Run
```bash
source myenv/bin/activate
python3 pyfile_servo.py
```

Or download directly on RPi:
```bash
wget https://rasimmax.com/fsm/pybook/pyfile_servo.py
```

---

## 📊 Results

✅ DHT11 successfully reads temperature & humidity  
✅ LDR detects day/night conditions  
✅ I2C LCD displays real-time data  
✅ Red LED + Buzzer alert when temperature > threshold  
✅ Green LED indicates normal conditions  
✅ Servo motor rotates as fan simulation (Task 2)  

---

## 💡 Key Learnings

- **I2C Communication**: Using only 2 wires (SDA, SCL) for LCD
- **Virtual Environments**: Isolated Python workspace for dependencies
- **GPIO Control**: Digital output for LEDs, input for LDR
- **PWM for Servo**: Using `gpiozero` + `pigpio` for precise motor control
- **Sensor Integration**: Combining multiple sensors in one system

---

## 📝 Conclusion

This lab demonstrated how to build a complete IoT weather monitoring system using Raspberry Pi. The project integrates multiple sensors (DHT11, LDR), output devices (LEDs, Buzzer, LCD, Servo), and shows how to create automated responses based on environmental conditions.

---

## 📄 License
Educational project for EEC3612 Embedded Systems course.
