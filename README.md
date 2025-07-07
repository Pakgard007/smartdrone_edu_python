

## 📘 1. Introduction to Python Programming 

### 🔹 Basic Syntax

* **Comments:**

  * Single-line: `# This is a comment`
  * Multi-line: `''' multi-line comment '''`
  * Inline: `print("Hello") # comment`

* **Statements:**
  Python executes one command per line. Multiple statements in one line can be separated by semicolons.

* **Indentation:**
  Mandatory for defining blocks (`if`, `for`, `def`, etc.). Blocks must have consistent spacing.

### 🔹 Variables and Data Types

* Variables are dynamically typed:

  ```python
  a = 3          # Integer
  b = 4.92       # Float
  c = "text"     # String
  c = 10.5       # Reassigns to Float
  ```

* **Multiple assignment**:

  ```python
  a, b = 1, 2
  x = y = z = 10
  ```

### 🔹 Data Types

* **Numbers:** int, float, complex, decimal
* **Strings:** Text in `'` or `"` quotes. Use `\` for escape characters.
* **Lists:** Ordered, mutable collections. Can hold multiple data types.

  ```python
  numbers = [1, 2, 3]
  names = ["Alice", "Bob"]
  ```

### 🔹 Useful Functions

* `type()`: get variable type
* `sys.getsizeof()`: get memory size
* `del`: delete variable
* `locals()`, `globals()`: check declared variables

### 🔹 Print Formatting

* `print(value1, value2, ..., sep=" ", end="\n")`
* Format strings: `"%s %d %f" % (str, int, float)`

### 🔹 Operators

* **Arithmetic:** `+`, `-`, `*`, `/`, `//`, `%`, `**`
* **Comparison:** `<`, `>`, `==`, `!=`, `>=`, `<=`, `is`, `is not`
* **Logical:** `and`, `or`, `not`
* **Membership:** `in`, `not in`

### 🔹 Conditionals

```python
if score > 80:
    print("A")
elif score > 70:
    print("B")
else:
    print("F")
```

---

## 🚁 2. DJI Tello Drone User Guide 

### 🔹 Drone Specs

* Weight: 80g
* Flight time: \~13 minutes
* Control range: \~100 meters
* Camera: 5MP still, 720p video
* Stabilization: EIS (Electronic Image Stabilization)
* Battery: 3.8V 1100mAh

### 🔹 Initial Setup

1. Insert propeller guards and battery
2. Power on (tap the button once)
3. Watch LED indicators for status

### 🔹 LED Status Overview

* **Startup:** Red/Green/Yellow flashing
* **Normal Flight:** Green blinking
* **Vision system error:** Yellow blinking
* **Battery low:** Red blinking

### 🔹 Tello App Setup

1. Connect to drone’s WiFi (`TELLO-XXXXXX`)
2. Launch **Tello App** (Android/iOS)
3. Go to settings → rename WiFi (e.g., A001, password: 00112345)
4. Reconnect and verify settings

### 🔹 Flight Modes (Smart Flight)

* **Throw & Go** – toss drone to launch
* **8D Flips** – perform flips
* **Up & Away** – cinematic backward flight
* **360** – rotate and record
* **Circle** – orbit around subject
* **Bounce Mode** – vertical bounce auto-mode

### 🔹 App Controls

* Left Stick: throttle up/down and yaw
* Right Stick: pitch and roll
* Settings: camera exposure, EV, firmware updates, beginner guide, etc.

### 🔹 FAQ Highlights

* **Not waterproof**
* **No GPS** – lands on signal loss
* **No SD Card support** – media saved to smartphone
* **Firmware updates via app only**
* **Indoor preferred**; outdoor flight possible but affected by wind

---

## ✨ 3. Drone Formation Control with Python 
### 🔹 Drone Basics

* UAV = Unmanned Aerial Vehicle
* Controlled via remote or autonomously
* Types: Quad, Hex, Octo rotors
* Key components: GPS, Frame, Barometer, IMU, Optical Flow, etc.

### 🔹 Legal Notes (Thailand)

* Must register both **operator** and **drone**
* Drone over 250g or has a camera → registration required
* Penalties for violations:

  * Owner: up to 5 years in jail / 100,000 THB fine
  * Operator: up to 1 year in jail / 40,000 THB fine

### 🔹 Basic Controls

* **Left stick:** Ascend/descend, yaw
* **Right stick:** Forward/backward, left/right (roll)

### 🔹 Python Integration

* Programming languages supported: **Scratch**, **Python**, **Node.js**

* Python is preferred for flexible control and logic

* Example usage:

  ```python
  print("Hello")
  input("Enter name:")
  for x in range(5):
      print(x)
  if score > 50:
      print("Pass")
  ```

* Data Types:

  * `int`, `float`, `string`, `complex`

* Operators:

  * Arithmetic: `+ - * / // % **`
  * Logical: `and, or, not`
  * Comparison: `<, <=, >, >=, ==, !=`

* Common Errors:

  * `SyntaxError`, `NameError`, `TypeError`, `ValueError`, `ZeroDivisionError`

---

📂 check_SN_drone.py
📝 Description
This script is designed to initialize a Tello EDU drone session using the FlyTello library. It's commonly used to verify if the serial number works correctly with the SDK, but the actual serial is left blank.

🔧 How It Works
python
Copy
Edit
my_tello = list()
my_tello.append('')
A drone list is created but left empty (should contain serial number of the drone).

python
Copy
Edit
with FlyTello(my_tello) as fly:
    pass
Initializes the drone context but performs no actions.

The script is wrapped in a try...except to suppress errors if the connection fails.

📂 mission_multi_drone.py
📝 Description
An interactive command-line controller for one or more Tello EDU drones with an included predefined flight mission using Mission Pads.

🔧 Key Functions
python
Copy
Edit
my_tellos.append('0TQDG6SEDB7WCT')  # Serial number of active drone
💻 Command Input
Users can enter:

t → Takeoff

l → Land

b → Battery status

speed → Speed status

h → Height

bounce → Drone bounces up/down

1 → Start predefined mission

q → Quit

✈️ Mission Logic (triggered by input '1')
Executes synchronized flight movements using fly.sync_these() and fly.jump_between_pads(...)

Movement path: m1 → m2 → m3 → m4 → m1 (square path)

Uses fly.reorient() at each pad for repositioning

Ends with landing

🧯 Safety
Gracefully exits via KeyboardInterrupt and calls fly.Stop().

📂 set_ap_edu_drone.py
📝 Description
Sets the WiFi Access Point (AP) credentials for a Tello EDU drone. Useful for connecting the drone to a shared network in a classroom/lab.

🔧 Core Logic
python
Copy
Edit
fly.set_ap_wifi(ssid='staff tello SB', password='45224522')
When user types ap, the drone is configured to connect to the specified WiFi network.

💻 CLI Command
ap → Apply predefined SSID and password settings

📂 network-scan.py
📝 Description
Scans the entire local subnet (192.168.0.1/24) to check which IP addresses are active — typically to detect Tello EDU drones connected to a shared WiFi.

🔧 Core Logic
python
Copy
Edit
for ip in ip_net.hosts():
    Popen(['ping', '-c', '1', '-W', '50', ip], stdout=PIPE)
Pings each IP once and checks if it's online.

Output: "192.168.0.X is online" or "offline"

✅ Use Case
Helpful to identify drone IPs automatically before running multi-drone commands.

