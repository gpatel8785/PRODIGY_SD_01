# 🌡️ Temperature Conversion Program

<div align="center">

![Temperature Converter](https://img.shields.io/badge/Temperature-Converter-blue?style=for-the-badge&logo=thermometer)
![Python](https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge&logo=python)
![HTML5](https://img.shields.io/badge/HTML5-Web_Interface-orange?style=for-the-badge&logo=html5)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

**A comprehensive temperature conversion program supporting Celsius, Fahrenheit, and Kelvin scales**

*Prodigy InfoTech Software Development Internship - Task 01*

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-integration)

</div>

---

## 📋 Task Requirements

**Task-01: Build a Temperature Conversion Program**

Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales with the following specifications:

### ✅ Requirements Fulfilled

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| **Input temperature value** | ✅ Complete | Interactive prompts with validation |
| **Input original unit (C/F/K)** | ✅ Complete | Menu-driven unit selection |
| **Convert to other two units** | ✅ Complete | Comprehensive conversion algorithms |
| **Handle all conversion combinations** | ✅ Complete | 6 conversion methods implemented |
| **Validate against absolute zero** | ✅ Complete | Physical limit validation |
| **Display converted values** | ✅ Complete | Formatted output with symbols |
| **Clear, formatted output** | ✅ Complete | Professional console interface |

### 🎯 Example Functionality

**Input:** 25 degrees Celsius  
**Output:**
🧊 Celsius: 25.00°C
🌡️ Fahrenheit: 77.00°F
🔬 Kelvin: 298.15K

---

## 🌟 Features

### 🐍 Python Console Application

- **Interactive CLI** with elegant formatting
- **Input Validation** including physical limits
- **Error Handling** for invalid inputs
- **Loop for Multiple Conversions**
- **Clean Output** with clear emojis & layout
- **Reference Tables** for user understanding

### 🌐 Web Interface (Bonus)

- **Modern UI** with gradients and glass morphism
- **Live Conversion** as you type
- **Responsive Design** for all screen sizes
- **History Tracking** of conversions
- **Smooth Animations** and UX transitions
- **Visual Temperature Cards** with icons and scale info

### 🔧 Technical Excellence

- **Object-Oriented Python Design**
- **Type Hints and Docstrings**
- **API-Ready Functions**
- **Validated Against Absolute Zero**
- **Production-Level Code Quality**

---

## 🚀 Demo

### Console Interface Preview
============================================================
🌡️ TEMPERATURE CONVERSION PROGRAM
Prodigy InfoTech Software Development Internship
Task-01: Temperature Conversion Program

🌡️ Enter temperature value: 100
📋 Available Temperature Units:
[C] Celsius (°C)
[F] Fahrenheit (°F)
[K] Kelvin (K)

📐 Enter unit (C/F/K): C

==================================================
🎯 CONVERSION RESULTS

📥 Input: 100.00°C (Celsius)

📤 Converted Values:
🧊 Celsius: 100.00°C
🌡️ Fahrenheit: 212.00°F
🔬 Kelvin: 373.15K

📚 Reference Points:
• Water Freezing: 0°C = 32°F = 273.15K
• Water Boiling: 100°C = 212°F = 373.15K
• Absolute Zero: -273.15°C = -459.67°F = 0K

### Web Interface Preview

![Web Interface Preview](https://via.placeholder.com/800x400/667eea/ffffff?text=Beautiful+Web+Interface+with+Real-time+Conversion)

---

## 📦 Installation

### Prerequisites

- Python 3.7 or higher  
- A modern web browser (for web interface)

### Quick Start

```bash
# Clone the repository
git clone [your-repo-url]
cd PRODIGY_SD_01_Temperature_Converter

# Run the console app
python temperature_converter.py
To launch the web version:

Open temperature_converter.html in any browser

💻 Usage
Python Console Application
bash

python temperature_converter.py
Steps:

Enter temperature value (e.g., 25)

Select unit (C, F, or K)

View all conversion results

Repeat or exit

Web Interface
Open temperature_converter.html

Enter temperature value

Select original unit

View results in styled cards

See conversion history updates in real-time

🔬 Conversion Formulas
From → To	Formula	Function
Celsius → Fahrenheit	F = (C × 9/5) + 32	celsius_to_fahrenheit()
Celsius → Kelvin	K = C + 273.15	celsius_to_kelvin()
Fahrenheit → Celsius	C = (F - 32) × 5/9	fahrenheit_to_celsius()
Fahrenheit → Kelvin	K = (F - 32) × 5/9 + 273.15	fahrenheit_to_kelvin()
Kelvin → Celsius	C = K - 273.15	kelvin_to_celsius()
Kelvin → Fahrenheit	F = (K - 273.15) × 9/5 + 32	kelvin_to_fahrenheit()

Absolute Zero Validation
Scale	Limit	Validation Rule
Celsius	-273.15°C	temperature >= -273.15
Fahrenheit	-459.67°F	temperature >= -459.67
Kelvin	0K	temperature >= 0

🛠️ API Integration
Ready for Backend Integration

python

# Example usage
result = convert_api(temperature=25, from_unit='C')
print(result)

# Output:
{
  'success': True,
  'input': {'temperature': 25, 'unit': 'C', 'unit_name': 'Celsius'},
  'results': {'celsius': 25.0, 'fahrenheit': 77.0, 'kelvin': 298.15},
  'formatted_results': {'celsius': '25.00°C', 'fahrenheit': '77.00°F', 'kelvin': '298.15K'}
}
Flask Integration Example

python

from flask import Flask, jsonify, request
from temperature_converter import convert_api

app = Flask(__name__)

@app.route('/api/convert', methods=['POST'])
def api_convert():
    data = request.json
    return jsonify(convert_api(data['temperature'], data['unit']))
📁 Project Structure
bash

PRODIGY_SD_01_Temperature_Converter/
├── temperature_converter.py       # Console program
├── temperature_converter.html     # Web UI
├── README.md                      # This file
└── screenshots/                   # UI Previews
    ├── console_demo.png
    ├── web_desktop.png
    └── web_mobile.png
🧪 Testing Examples
✅ Valid Tests
0°C → 32.00°F, 273.15K

212°F → 100.00°C, 373.15K

0K → -273.15°C, -459.67°F

25°C → 77.00°F, 298.15K

❌ Error Handling
-300°C → ❗ Error: below absolute zero

25°X → ❗ Error: invalid unit input

🎨 Design Highlights
Console Interface
🎨 Beautiful ASCII + emoji formatting

📊 Structured, readable layout

🌈 Color-coded sections

📋 Reference points included

Web Interface
🎨 Modern gradients + glass morphism

📱 Fully responsive layout

⚡ Real-time conversion logic

📊 Conversion history

🎯 Intuitive and animated interface

🏆 Project Achievements
✅ Core Requirements
 Temperature input + validation

 Unit selection (C/F/K)

 Two-unit conversion logic

 Absolute zero enforcement

 Professional output

 Loop for multiple conversions

🌟 Bonus Features
 Beautiful web interface

 OOP-based Python code

 API-ready design

 Full documentation

 Mobile responsive

 Conversion history

 Real-time validation

👨‍💻 About
Developer: [Gaurav Patel]
Internship: Prodigy InfoTech Software Development
Task: PRODIGY_SD_01 - Temperature Conversion Program
Completion Date: August 2, 2025
Tech Stack: Python 3.7+, HTML5, CSS3, JS, Tailwind CSS

📧 Email: [gaurav8296p@gmail.com]
💼 LinkedIn: https://www.linkedin.com/in/gaurav-patel-3b516a241
🐱 GitHub: https://github.com/gpatel8785

📄 License
This project is created as part of the Prodigy InfoTech Software Development Internship program.

⭐ If you found this project helpful, please give it a star! ⭐
Made with ❤️ for Prodigy InfoTech
