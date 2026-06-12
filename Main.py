from sentence_transformers import SentenceTransformer, util
import tkinter as tk
from tkinter import scrolledtext

model = SentenceTransformer('all-MiniLM-L6-v2')

qa_pairs = [
    ("hello hi hey greetings καλησπερουδια γεια χαρά", "Hi! How can I help with ESP32, Arduino, or microcontroller projects today?"),
    ("esp32", "ESP32 is a powerful microcontroller with Wi-Fi and Bluetooth built in."),
    ("arduino", "Arduino is great for learning electronics, sensors, and microcontroller programming."),
    ("microcontroller mcu", "A microcontroller is a small computer used to control electronics projects."),
    ("esp32 vs arduino", "ESP32 is faster and has Wi-Fi/Bluetooth, while Arduino is simpler for beginners."),
    ("arduino uno", "Arduino Uno is one of the most beginner-friendly microcontroller boards."),
    ("arduino nano", "Arduino Nano is a compact board useful for small projects."),
    ("arduino mega", "Arduino Mega has many GPIO pins, ideal for larger projects."),
    ("esp32 devkit", "ESP32 DevKit boards are commonly used for IoT and wireless projects."),
    ("esp32 wroom", "ESP32-WROOM is a popular ESP32 module used in many development boards."),
    ("esp32 cam", "ESP32-CAM can stream video over Wi-Fi and is useful for camera projects."),
    ("iot internet of things", "ESP32 is excellent for IoT because it has built-in Wi-Fi."),
    ("wifi esp32", "ESP32 can connect to Wi-Fi networks and send data online."),
    ("bluetooth esp32", "ESP32 supports Bluetooth Classic and BLE communication."),
    ("ble bluetooth low energy", "BLE is useful for low-power wireless communication with phones and sensors."),
    ("gpio pins", "GPIO pins let your microcontroller read inputs and control outputs."),
    ("digital input", "Digital input reads HIGH or LOW signals from buttons or sensors."),
    ("digital output", "Digital output controls devices like LEDs, buzzers, and relays."),
    ("analog input", "Analog input reads variable voltages from sensors."),
    ("adc analog to digital", "ADC converts analog voltage into digital values."),
    ("dac digital to analog", "ESP32 has DAC pins that can output analog-like voltages."),
    ("pwm", "PWM lets you control LED brightness, motor speed, and servos."),
    ("led blink", "Blinking an LED is the classic first microcontroller project."),
    ("button pushbutton", "A pushbutton can be used as a digital input."),
    ("resistor", "Resistors limit current and protect components like LEDs."),
    ("breadboard", "A breadboard lets you build circuits without soldering."),
    ("jumper wires", "Jumper wires connect components on a breadboard."),
    ("usb cable", "A USB cable powers the board and uploads code."),
    ("arduino ide", "Arduino IDE is a simple tool for writing and uploading microcontroller code."),
    ("platformio", "PlatformIO is a powerful development environment for ESP32 and Arduino."),
    ("upload code", "Select the correct board and port before uploading code."),
    ("compile error", "Compile errors usually mean syntax mistakes or missing libraries."),
    ("serial monitor", "Serial Monitor helps debug by printing messages from the board."),
    ("serial print", "Serial.print() displays values in the Serial Monitor."),
    ("baud rate", "The baud rate must match between your code and Serial Monitor."),
    ("setup function", "setup() runs once when the microcontroller starts."),
    ("loop function", "loop() runs repeatedly after setup()."),
    ("pinmode", "pinMode() sets a pin as INPUT, OUTPUT, or INPUT_PULLUP."),
    ("digitalwrite", "digitalWrite() sets a digital pin HIGH or LOW."),
    ("digitalread", "digitalRead() reads HIGH or LOW from a digital pin."),
    ("analogread", "analogRead() reads an analog sensor value."),
    ("analogwrite", "analogWrite() outputs PWM on supported pins."),
    ("delay", "delay() pauses the program, but millis() is better for multitasking."),
    ("millis", "millis() lets you time events without blocking the program."),
    ("interrupt", "Interrupts react quickly to events like button presses or sensor signals."),
    ("debounce", "Debouncing prevents false button readings caused by mechanical noise."),
    ("pullup resistor", "A pull-up resistor keeps an input HIGH when not pressed."),
    ("pulldown resistor", "A pull-down resistor keeps an input LOW when not pressed."),
    ("input_pullup", "INPUT_PULLUP uses the microcontroller’s internal pull-up resistor."),
    ("voltage 3.3v 5v", "ESP32 uses 3.3V logic, while many Arduino boards use 5V logic."),
    ("logic level", "Logic levels must match to avoid damaging your microcontroller."),
    ("level shifter", "A level shifter converts signals between 3.3V and 5V."),
    ("power supply", "Use a stable power supply to avoid resets and unreliable behavior."),
    ("battery", "Battery-powered projects need voltage regulation and power-saving design."),
    ("lipo battery", "LiPo batteries are compact but need proper charging and protection circuits."),
    ("voltage regulator", "A voltage regulator provides stable voltage to your board."),
    ("current", "Make sure your power supply can provide enough current for all components."),
    ("ground gnd", "All connected modules usually need a common ground."),
    ("short circuit", "A short circuit can damage components or the board."),
    ("overheating", "Overheating may mean wrong wiring, too much current, or a damaged component."),
    ("relay", "A relay lets a microcontroller switch higher-voltage devices."),
    ("relay module", "Relay modules are useful for lights, pumps, and automation projects."),
    ("transistor", "A transistor can switch larger loads than a GPIO pin can handle."),
    ("mosfet", "MOSFETs are efficient switches for motors, LEDs, and power loads."),
    ("diode", "A diode allows current to flow in one direction."),
    ("flyback diode", "A flyback diode protects circuits from voltage spikes caused by coils."),
    ("capacitor", "Capacitors store charge and help smooth voltage fluctuations."),
    ("buzzer", "A buzzer can produce tones, alarms, and alerts."),
    ("passive buzzer", "A passive buzzer needs PWM to generate tones."),
    ("active buzzer", "An active buzzer makes sound when voltage is applied."),
    ("servo", "Servo motors move to specific angles using PWM control."),
    ("dc motor", "DC motors need a driver circuit because GPIO pins cannot power them directly."),
    ("motor driver", "Motor drivers control motors safely using external power."),
    ("l298n", "L298N is a common motor driver for small DC motors."),
    ("uln2003", "ULN2003 is commonly used to drive 28BYJ-48 stepper motors."),
    ("stepper motor", "Stepper motors move in precise steps and are useful for positioning."),
    ("robot car", "A robot car can use motors, sensors, and an Arduino or ESP32."),
    ("ultrasonic sensor", "HC-SR04 measures distance using ultrasonic sound waves."),
    ("hc-sr04", "HC-SR04 is a common distance sensor for obstacle detection."),
    ("ir sensor", "IR sensors can detect objects, lines, or remote-control signals."),
    ("pir sensor", "PIR sensors detect motion from people or animals."),
    ("ldr light sensor", "An LDR changes resistance based on light level."),
    ("photoresistor", "A photoresistor can detect brightness or darkness."),
    ("temperature sensor", "Temperature sensors measure heat or environmental temperature."),
    ("dht11", "DHT11 measures temperature and humidity but is less accurate than DHT22."),
    ("dht22", "DHT22 measures temperature and humidity with better accuracy than DHT11."),
    ("ds18b20", "DS18B20 is a reliable digital temperature sensor, often waterproof."),
    ("bmp280", "BMP280 measures temperature and air pressure."),
    ("bme280", "BME280 measures temperature, humidity, and pressure."),
    ("mq sensor", "MQ gas sensors detect gases but need calibration."),
    ("mq2", "MQ-2 can detect smoke, LPG, methane, and other gases."),
    ("soil moisture", "Soil moisture sensors are useful for plant watering projects."),
    ("water level sensor", "Water level sensors detect liquid presence or level."),
    ("rain sensor", "Rain sensors detect water droplets on a conductive surface."),
    ("flame sensor", "Flame sensors detect infrared light from fire."),
    ("accelerometer", "Accelerometers measure motion and tilt."),
    ("gyroscope", "Gyroscopes measure rotation."),
    ("mpu6050", "MPU6050 combines an accelerometer and gyroscope."),
    ("magnetometer", "A magnetometer detects magnetic fields and can work as a compass."),
    ("rtc real time clock", "RTC modules keep accurate time even when power is off."),
    ("ds3231", "DS3231 is a very accurate real-time clock module."),
    ("sd card", "SD card modules store data logs from sensors."),
    ("data logging", "Data logging saves sensor readings over time."),
    ("oled", "OLED displays are compact and clear for showing sensor data."),
    ("lcd", "LCD screens can display text from Arduino or ESP32."),
    ("16x2 lcd", "A 16x2 LCD shows two lines of sixteen characters."),
    ("i2c lcd", "I2C LCD modules use fewer pins than parallel LCD wiring."),
    ("display screen", "Displays are useful for menus, sensor values, and status messages."),
    ("tft display", "TFT displays can show graphics, colors, and touch interfaces."),
    ("touch screen", "Touch screens allow user interaction with microcontroller projects."),
    ("i2c", "I2C is a communication protocol using SDA and SCL lines."),
    ("spi", "SPI is a fast communication protocol using MOSI, MISO, SCK, and CS."),
    ("uart serial", "UART is used for serial communication between devices."),
    ("onewire", "OneWire allows communication with devices like DS18B20 using one data pin."),
    ("can bus", "CAN bus is used in vehicles and industrial systems."),
    ("rs485", "RS485 is good for long-distance wired communication."),
    ("mqtt", "MQTT is a lightweight messaging protocol often used in IoT."),
    ("http request", "ESP32 can send HTTP requests to web servers and APIs."),
    ("web server", "ESP32 can host a web server to control devices from a browser."),
    ("websocket", "WebSockets allow real-time communication between ESP32 and a web page."),
    ("api", "ESP32 can send sensor data to APIs over Wi-Fi."),
    ("cloud", "Microcontrollers can send data to cloud platforms for monitoring."),
    ("thingspeak", "ThingSpeak is a common IoT platform for logging sensor data."),
    ("blynk", "Blynk lets you control IoT devices from a smartphone app."),
    ("home assistant", "ESP32 works well with Home Assistant for smart home automation."),
    ("esphome", "ESPHome makes ESP32 smart home projects easier with YAML configuration."),
    ("wifi manager", "WiFiManager lets users configure Wi-Fi without hardcoding credentials."),
    ("access point", "ESP32 can create its own Wi-Fi access point."),
    ("station mode", "Station mode lets ESP32 connect to an existing Wi-Fi network."),
    ("ssid password", "SSID is the Wi-Fi network name; password is needed to connect."),
    ("static ip", "A static IP keeps your ESP32 at the same network address."),
    ("ota update", "OTA updates let you upload new firmware over Wi-Fi."),
    ("firmware", "Firmware is the program running on the microcontroller."),
    ("bootloader", "The bootloader helps upload and start firmware on the board."),
    ("flash memory", "Flash memory stores your uploaded program."),
    ("eeprom", "EEPROM stores small values that remain after power off."),
    ("preferences esp32", "ESP32 Preferences library stores settings in flash memory."),
    ("nvs", "NVS is ESP32 non-volatile storage for saving data."),
    ("deep sleep", "Deep sleep greatly reduces ESP32 power consumption."),
    ("light sleep", "Light sleep saves power while allowing faster wake-up."),
    ("wake up", "ESP32 can wake from sleep using timers, touch pins, or external signals."),
    ("low power", "Low-power design is important for battery projects."),
    ("watchdog", "A watchdog timer resets the board if the program freezes."),
    ("reset", "Reset restarts the microcontroller program."),
    ("boot button", "The BOOT button on ESP32 is often used for flashing firmware."),
    ("en button", "The EN button resets many ESP32 boards."),
    ("com port", "Select the correct COM port before uploading code."),
    ("driver ch340", "Some boards need the CH340 USB driver installed."),
    ("cp2102", "Many ESP32 boards use the CP2102 USB-to-serial chip."),
    ("ftdi", "FTDI adapters are used for USB-to-serial programming."),
    ("library", "Libraries provide ready-made code for sensors, displays, and modules."),
    ("install library", "Install missing libraries through Arduino Library Manager."),
    ("missing library", "A missing library can cause compile errors."),
    ("board manager", "Board Manager installs support for ESP32 and other boards."),
    ("esp32 board package", "Install the ESP32 board package to program ESP32 in Arduino IDE."),
    ("select board", "Choose the exact board model before uploading."),
    ("upload speed", "Lower upload speed can help if ESP32 upload fails."),
    ("failed to connect", "Hold BOOT while uploading if ESP32 says failed to connect."),
    ("brownout detector", "Brownout errors usually mean unstable or insufficient power."),
    ("guru meditation", "Guru Meditation on ESP32 usually means a crash or memory error."),
    ("stack overflow", "Stack overflow happens when a task uses too much stack memory."),
    ("heap memory", "Heap memory is dynamic memory used while the program runs."),
    ("memory leak", "A memory leak happens when memory is allocated but not released."),
    ("free heap", "Checking free heap helps debug ESP32 memory problems."),
    ("task", "ESP32 can run tasks using FreeRTOS."),
    ("freertos", "FreeRTOS allows multitasking on ESP32."),
    ("core 0 core 1", "ESP32 has two cores, often called Core 0 and Core 1."),
    ("multitasking", "ESP32 can run multiple tasks using FreeRTOS."),
    ("semaphore", "Semaphores help coordinate tasks safely."),
    ("queue", "Queues pass data between FreeRTOS tasks."),
    ("mutex", "A mutex protects shared resources from simultaneous access."),
    ("timer", "Timers trigger actions at specific intervals."),
    ("hardware timer", "Hardware timers provide precise timing without blocking code."),
    ("software timer", "Software timers schedule repeated actions in code."),
    ("interrupt service routine", "An ISR should be short and fast."),
    ("volatile", "Use volatile for variables changed inside interrupts."),
    ("state machine", "State machines help organize complex microcontroller logic."),
    ("non blocking code", "Non-blocking code avoids delay() and keeps the system responsive."),
    ("finite state machine", "A finite state machine separates behavior into clear states."),
    ("scheduler", "A scheduler runs tasks at planned intervals."),
    ("led strip", "LED strips can create colorful lighting effects."),
    ("ws2812", "WS2812 LEDs are individually addressable RGB LEDs."),
    ("neopixel", "NeoPixel strips are popular addressable RGB LEDs."),
    ("fastled", "FastLED is a powerful library for addressable LED animations."),
    ("adafruit neopixel", "Adafruit NeoPixel library makes controlling RGB LEDs easy."),
    ("rgb led", "RGB LEDs mix red, green, and blue light to create colors."),
    ("matrix led", "LED matrices can display text, icons, and animations."),
    ("max7219", "MAX7219 controls LED matrices or 7-segment displays."),
    ("seven segment", "7-segment displays show numbers using LED segments."),
    ("keypad", "Keypads allow number or password input."),
    ("rotary encoder", "Rotary encoders detect rotation and direction."),
    ("potentiometer", "A potentiometer provides adjustable analog input."),
    ("joystick", "Joystick modules provide two analog axes and a button."),
    ("rfid", "RFID modules read tags and cards wirelessly."),
    ("rc522", "RC522 is a common RFID reader module."),
    ("nfc", "NFC allows short-range wireless communication."),
    ("gps", "GPS modules provide location, speed, and time data."),
    ("neo 6m", "NEO-6M is a common GPS module for Arduino and ESP32."),
    ("gsm module", "GSM modules send SMS or connect to mobile networks."),
    ("sim800l", "SIM800L is a small GSM module, but it needs strong power supply."),
    ("lora", "LoRa enables long-range low-power wireless communication."),
    ("sx1278", "SX1278 is a common LoRa radio module."),
    ("nrf24l01", "NRF24L01 is a low-cost 2.4GHz wireless module."),
    ("433mhz", "433MHz modules are used for simple wireless communication."),
    ("infrared remote", "IR remotes can control microcontroller projects using infrared signals."),
    ("ir receiver", "An IR receiver reads commands from remote controls."),
    ("ir transmitter", "An IR LED can send remote-control signals."),
    ("camera", "Camera modules allow image capture and video streaming."),
    ("ov2640", "OV2640 is the camera sensor commonly used with ESP32-CAM."),
    ("face detection", "ESP32-CAM can run basic face detection examples."),
    ("image streaming", "ESP32-CAM can stream video over a local Wi-Fi network."),
    ("sd card esp32 cam", "ESP32-CAM often uses a microSD card for saving images."),
    ("webcam project", "ESP32-CAM can be used as a simple Wi-Fi camera."),
    ("smart home", "ESP32 is great for smart home sensors, switches, and automation."),
    ("smart light", "A smart light project can use ESP32, relay, MOSFET, or LED strip."),
    ("smart plug", "Smart plug projects require extra safety because they involve mains voltage."),
    ("thermostat", "A thermostat project reads temperature and controls heating or cooling."),
    ("plant watering", "Automatic plant watering uses a soil sensor, pump, and relay or MOSFET."),
    ("weather station", "A weather station can measure temperature, humidity, pressure, and light."),
    ("security system", "A basic security system can use PIR sensors, buzzers, and notifications."),
    ("door sensor", "Magnetic reed switches can detect if a door is open or closed."),
    ("reed switch", "A reed switch detects magnets and is useful for door sensors."),
    ("alarm", "An alarm project can use sensors, buzzers, LEDs, and messages."),
    ("garage door", "ESP32 can monitor or control a garage door with sensors and relays."),
    ("water pump", "Control water pumps using a relay or MOSFET with external power."),
    ("fan control", "Fans can be controlled by temperature using PWM or relays."),
    ("temperature control", "Temperature control projects use sensors and switching devices."),
    ("pid control", "PID control adjusts output based on error, useful for heating or motors."),
    ("robot arm", "Robot arms commonly use servo motors for joint movement."),
    ("line follower", "Line-following robots use IR sensors to track a dark or light line."),
    ("obstacle avoidance", "Obstacle avoidance robots often use ultrasonic or IR sensors."),
    ("bluetooth car", "A Bluetooth robot car can be controlled from a phone."),
    ("wifi car", "An ESP32 robot car can be controlled through a Wi-Fi web page."),
    ("drone", "Drone projects need IMU sensors, motor drivers, and careful control algorithms."),
    ("cnc", "CNC projects use stepper motors and precise motion control."),
    ("3d printer", "3D printers use microcontrollers to control motors, heaters, and sensors."),
    ("grbl", "GRBL is firmware for CNC motion control on Arduino-compatible boards."),
    ("marlin", "Marlin is popular firmware for 3D printers."),
    ("encoder feedback", "Encoders measure motor position or speed."),
    ("hall sensor", "Hall sensors detect magnetic fields."),
    ("current sensor", "Current sensors measure electrical current in a circuit."),
    ("acs712", "ACS712 is a common current sensor module."),
    ("ina219", "INA219 measures voltage and current over I2C."),
    ("voltage divider", "A voltage divider reduces voltage using two resistors."),
    ("measure voltage", "Use a voltage divider to safely measure higher voltages with an ADC."),
    ("multimeter", "A multimeter helps measure voltage, current, resistance, and continuity."),
    ("oscilloscope", "An oscilloscope shows electrical signals over time."),
    ("logic analyzer", "A logic analyzer helps debug digital communication signals."),
    ("soldering", "Soldering creates permanent electrical connections."),
    ("pcb", "A PCB is a custom board for a finished electronics project."),
    ("prototype", "Prototype first on a breadboard before making a PCB."),
    ("schematic", "A schematic shows how electronic components are connected."),
    ("circuit diagram", "Circuit diagrams help plan and debug wiring."),
    ("fritzing", "Fritzing is often used to draw beginner-friendly wiring diagrams."),
    ("kicad", "KiCad is a free tool for designing schematics and PCBs."),
    ("ground loop", "Ground problems can cause noise, unstable readings, or communication errors."),
    ("noise", "Electrical noise can affect sensors and communication."),
    ("filter capacitor", "Filter capacitors help smooth noisy power lines."),
    ("decoupling capacitor", "Decoupling capacitors should be placed near IC power pins."),
    ("pull resistor", "Pull-up or pull-down resistors prevent floating input pins."),
    ("floating pin", "A floating pin can randomly read HIGH or LOW."),
    ("safety mains voltage", "Be very careful with mains voltage; use proper isolation and certified modules."),
    ("220v 230v ac", "Projects involving 220V or 230V AC require serious safety precautions."),
    ("relay safety", "Use relay modules with proper isolation, ratings, and enclosures."),
    ("enclosure", "An enclosure protects your circuit and users from accidental contact."),
    ("fuse", "A fuse protects circuits from excessive current."),
    ("esd", "ESD can damage sensitive electronics, so handle boards carefully."),
    ("waterproof", "Use waterproof enclosures and sealed sensors for outdoor projects."),
    ("outdoor project", "Outdoor electronics need weather protection and stable power."),
    ("solar power", "Solar projects need a panel, charger, battery, and regulator."),
    ("charging module", "Charging modules safely charge rechargeable batteries."),
    ("tp4056", "TP4056 is a common Li-ion/LiPo charging module."),
    ("boost converter", "A boost converter raises voltage."),
    ("buck converter", "A buck converter lowers voltage efficiently."),
    ("buck boost", "A buck-boost converter can raise or lower voltage."),
    ("logic analyzer i2c", "A logic analyzer is excellent for debugging I2C and SPI problems."),
    ("i2c scanner", "An I2C scanner finds connected device addresses."),
    ("i2c address", "I2C devices use addresses so multiple devices can share the same bus."),
    ("spi chip select", "Each SPI device usually needs its own chip select pin."),
    ("uart baud mismatch", "Wrong baud rate causes unreadable serial data."),
    ("sensor calibration", "Calibration improves sensor accuracy."),
    ("map function", "map() converts a value from one range to another."),
    ("constrain", "constrain() limits a value within a minimum and maximum range."),
    ("array", "Arrays store multiple values under one variable name."),
    ("string", "Strings store text, but too many dynamic Strings can fragment memory."),
    ("struct", "Structs group related variables together."),
    ("class", "Classes help organize code into reusable objects."),
    ("function", "Functions make code cleaner and reusable."),
    ("variable", "Variables store values used by your program."),
    ("constant", "Constants store values that should not change."),
    ("define", "#define creates a macro or constant before compilation."),
    ("include", "#include adds libraries or header files to your code."),
    ("bool boolean", "Boolean values are true or false."),
    ("int", "int stores whole numbers."),
    ("float", "float stores decimal values."),
    ("char", "char stores a single character."),
    ("byte", "byte stores values from 0 to 255."),
    ("long", "long stores larger integer values."),
    ("unsigned long", "unsigned long is often used with millis()."),
    ("if else", "if and else let your program make decisions."),
    ("switch case", "switch-case is useful when checking many possible values."),
    ("for loop", "A for loop repeats code a fixed number of times."),
    ("while loop", "A while loop repeats while a condition is true."),
    ("do while", "A do-while loop runs at least once before checking the condition."),
    ("break", "break exits a loop or switch statement."),
    ("continue", "continue skips to the next loop iteration."),
    ("return", "return exits a function and can send back a value."),
    ("comment", "Comments explain code and are ignored by the compiler."),
    ("syntax error", "Syntax errors usually come from missing semicolons, brackets, or wrong spelling."),
    ("semicolon", "Most Arduino C++ statements end with a semicolon."),
    ("curly braces", "Curly braces group code blocks in functions, loops, and conditions."),
    ("debugging", "Debugging means finding and fixing problems in your code or circuit."),
    ("troubleshooting", "Check power, wiring, code, board selection, and Serial Monitor output."),
    ("wiring problem", "Most beginner issues come from incorrect wiring or missing common ground."),
    ("sensor not working", "Check power, ground, signal pin, library, and example code."),
    ("upload failed", "Check cable, port, board selection, drivers, and boot mode."),
    ("board not detected", "Try another USB cable, port, driver, or board."),
    ("usb cable power only", "Some USB cables only provide power and cannot upload code."),
    ("random reset", "Random resets usually mean bad power, brownout, or code crashes."),
    ("wifi disconnect", "Wi-Fi disconnects can happen from weak signal, bad power, or code blocking."),
    ("mqtt disconnect", "MQTT disconnects often need reconnect logic in the code."),
    ("sensor noise", "Average multiple readings to reduce sensor noise."),
    ("average readings", "Averaging readings can make sensor data smoother."),
    ("moving average", "A moving average smooths noisy sensor values over time."),
    ("calibrate sensor", "Compare sensor readings to a known reference and adjust your code."),
    ("project idea", "Try a weather station, smart plant monitor, robot car, or ESP32 web server."),
    ("beginner project", "Start with LED blink, button input, sensor reading, or OLED display."),
    ("intermediate project", "Try an ESP32 web server, MQTT sensor node, or Bluetooth controller."),
    ("advanced project", "Try ESP32-CAM streaming, FreeRTOS multitasking, or LoRa sensor networks."),
    ("thanks thank you appreciate", "You're welcome! Ask me anything about ESP32, Arduino, sensors, or microcontroller code."),
]

question_texts = [q for q, a in qa_pairs]
question_embeddings = model.encode(question_texts, convert_to_tensor=True)

# Similarity threshold — below this, the bot says it doesn't understand
THRESHOLD = 0.3


# Semantic matching replaces keyword matching
def get_response(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(input_embedding, question_embeddings)[0]
    best_idx = similarities.argmax().item()
    best_score = similarities[best_idx].item()

    if best_score < THRESHOLD:
        return best_score, "Sorry, I don't understand. Try asking about esp32, arduino."

    return best_score, qa_pairs[best_idx][1]

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Microcontroller Chatbot")
        self.root.geometry("400x500")
        self.root.configure(bg="#2E2E2E")

        tk.Label(
           root, text = "Microcontroller Chatbot", font = ("Helvetica", 16, "bold"),
            fg = "#FFFFFF", bg="#2E2E2E"
        ).pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, height=20, width= 50, font=("Arial", 11),
            bg="#3C3C3C", fg = "#E0E0E0", insertbackground="white"
        )
        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.insert(tk.END,
                              "Welcome to MicroChat\n"
                              "Ask about microcontrollers!\n")
        self.chat_area.config(state="disabled")

        input_frame = tk.Frame(root, bg="#2E2E2E")
        input_frame.pack(pady=5)

        self.input_field =tk.Entry(
            input_frame, width=40, font=('Arial', 11), bg="#4A4A4A", fg="#FFFFFF",
            insertbackground="white"
        )
        self.input_field.pack(side=tk.LEFT,padx=5)
        self.input_field.bind("<Return>", self.send_message)

        # Send button
        tk.Button(
            input_frame, text="Send", command=self.send_message, font=("Arial", 11),
            bg="#4CAF50", fg="#FFFFFF", activebackground="#45A049"
        ).pack(side=tk.LEFT, padx=5)

        # Clear button
        tk.Button(
            root, text="Clear Chat", command=self.clear_chat, font=("Arial", 11),
            bg="#F44336", fg="#FFFFFF", activebackground="#D32F2F"
        ).pack(pady=5)

    def send_message(self, event=None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return

        score, response = get_response(user_input)
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"\nYou: {user_input}\n")
        self.chat_area.insert(tk.END, f"Match confidence: {score:.2f}\n")
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
        self.input_field.delete(0, tk.END)

    def clear_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.insert(tk.END,
                              "Welcome to MicroChat!\n"
                              "Ask about microcontrollers.\n")
        self.chat_area.config(state='disabled')


















def main():
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
