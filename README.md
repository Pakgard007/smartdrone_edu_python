

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

