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

Input: 25 degrees Celsius
Output:
🧊 Celsius:    25.00°C
🌡️ Fahrenheit: 77.00°F

🔬 Kelvin:     298.15K


---

## 🌟 Features

### 🐍 Python Console Application
- **Interactive Command-Line Interface** with beautiful formatting
- **Comprehensive Input Validation** including absolute zero limits
- **Error Handling** for invalid inputs and edge cases
- **Continuous Operation** with option for multiple conversions
- **Professional Output** with emojis and clear formatting
- **Reference Points** showing water freezing/boiling temperatures

### 🌐 Web Interface (Bonus)
- **Stunning Visual Design** with gradient backgrounds and glass effects
- **Real-time Conversion** as you type
- **Responsive Layout** works on desktop, tablet, and mobile
- **Conversion History** tracks your recent calculations
- **Interactive Animations** and smooth transitions
- **Temperature Cards** with visual indicators and reference points

### 🔧 Technical Excellence
- **Object-Oriented Design** with clean, maintainable code
- **Type Hints** for better code quality and IDE support
- **Comprehensive Documentation** with detailed docstrings
- **API-Ready Functions** for easy web integration
- **Physical Accuracy** respects absolute zero for all scales
- **Production-Ready** code following best practices

---

## 🚀 Demo

### Console Interface

============================================================
🌡️  TEMPERATURE CONVERSION PROGRAM
Prodigy InfoTech Software Development Internship
Task-01: Temperature Conversion Program

🌡️  Enter temperature value: 100
📋 Available Temperature Units:
[C] Celsius (°C)
[F] Fahrenheit (°F)
[K] Kelvin (K)

📐 Enter unit (C/F/K): C

==================================================
🎯 CONVERSION RESULTS

📥 Input: 100.00°C (Celsius)

📤 Converted Values:
🧊 Celsius:    100.00°C
🌡️  Fahrenheit: 212.00°F
🔬 Kelvin:     373.15K

📚 Reference Points:
• Water Freezing: 0°C = 32°F = 273.15K
• Water Boiling:  100°C = 212°F = 373.15K
• Absolute Zero:  -273.15°C = -459.67°F = 0K


### Web Interface
![Web Interface Preview](https://via.placeholder.com/800x400/667eea/ffffff?text=Beautiful+Web+Interface+with+Real-time+Conversion)

---

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- Modern web browser (for web interface)

### Quick Start
1. **Clone or Download** the project files
2. **No additional dependencies** required - uses only Python standard library!

```bash
# Download the files
git clone [your-repo-url]
cd PRODIGY_SD_01_Temperature_Converter

# Run the Python program
python temperature_converter.py

# Open web interface
# Double-click temperature_converter.html or open in browser

💻 Usage

Python Console Application

python temperature_converter.py

Interactive Flow:

Enter temperature value (e.g., 
25
)
Select unit (
C
, 
F
, or 
K
)
View conversion results
Choose to convert another temperature or exit
Web Interface

Open
 
temperature_converter.html
 in any web browser
Enter
 temperature value in the input field
Select
 the original unit from dropdown
Click
 "Convert Temperature" or wait for auto-conversion
View
 results in beautiful temperature cards
Check
 conversion history for recent calculations
🔬 Conversion Formulas

Mathematical Implementation

| From → To | Formula | Implementation |
|-----------|---------|----------------|
| 
Celsius → Fahrenheit
 | 
F = (C × 9/5) + 32
 | 
celsius_to_fahrenheit()
 |
| 
Celsius → Kelvin
 | 
K = C + 273.15
 | 
celsius_to_kelvin()
 |
| 
Fahrenheit → Celsius
 | 
C = (F - 32) × 5/9
 | 
fahrenheit_to_celsius()
 |
| 
Fahrenheit → Kelvin
 | 
K = (F - 32) × 5/9 + 273.15
 | 
fahrenheit_to_kelvin()
 |
| 
Kelvin → Celsius
 | 
C = K - 273.15
 | 
kelvin_to_celsius()
 |
| 
Kelvin → Fahrenheit
 | 
F = (K - 273.15) × 9/5 + 32
 | 
kelvin_to_fahrenheit()
 |

Absolute Zero Validation

| Scale | Absolute Zero | Validation |
|-------|---------------|------------|
| 
Celsius
 | -273.15°C | 
temperature >= -273.15
 |
| 
Fahrenheit
 | -459.67°F | 
temperature >= -459.67
 |
| 
Kelvin
 | 0K | 
temperature >= 0
 |

🛠️ API Integration

Ready for Backend Integration

The code includes API-ready functions for easy web service integration:

# Example API usage
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

from flask import Flask, jsonify, request
from temperature_converter import convert_api

app = Flask(__name__)

@app.route('/api/convert', methods=['POST'])
def api_convert():
    data = request.json
    result = convert_api(data['temperature'], data['unit'])
    return jsonify(result)

📁 Project Structure

PRODIGY_SD_01_Temperature_Converter/
├── 📄 temperature_converter.py      # Main Python program
├── 🌐 temperature_converter.html    # Web interface
├── 📖 README.md                     # This documentation
└── 📸 screenshots/                  # Interface screenshots
    ├── console_demo.png
    ├── web_desktop.png
    └── web_mobile.png

🧪 Testing Examples

Valid Test Cases

# Test Case 1: Water freezing point
Input: 0°C → Output: 32.00°F, 273.15K

# Test Case 2: Water boiling point  
Input: 212°F → Output: 100.00°C, 373.15K

# Test Case 3: Absolute zero
Input: 0K → Output: -273.15°C, -459.67°F

# Test Case 4: Room temperature
Input: 25°C → Output: 77.00°F, 298.15K

Error Handling

# Invalid temperature (below absolute zero)
Input: -300°C → Error: "Temperature cannot be below absolute zero (-273.15°C)"

# Invalid unit
Input: 25°X → Error: "Invalid unit 'X'. Use C, F, or K."

🎨 Design Highlights

Console Interface

🎨 
Beautiful ASCII art
 and emoji integration
📊 
Structured output
 with clear sections
🌈 
Color-coded information
 hierarchy
📋 
Reference tables
 for educational value
Web Interface

🎨 
Modern gradient design
 with glass morphism effects
📱 
Fully responsive
 layout for all devices
⚡ 
Real-time conversion
 with smooth animations
📊 
Interactive history
 tracking
🎯 
Intuitive user experience
 with clear visual feedback
🏆 Project Achievements

✅ Core Requirements

[x] Temperature input with validation
[x] Unit selection (C/F/K)
[x] Conversion to other two units
[x] All conversion combinations supported
[x] Absolute zero validation
[x] Clear, formatted output
[x] Continuous operation capability
🌟 Bonus Features

[x] Beautiful web interface
[x] Object-oriented design
[x] Comprehensive error handling
[x] API-ready architecture
[x] Professional documentation
[x] Mobile-responsive design
[x] Conversion history tracking
[x] Real-time validation
👨‍💻 About

Developer:
 [Gaurav Patel]

Internship:
 Prodigy InfoTech Software Development

Task:
 PRODIGY_SD_01 - Temperature Conversion Program

Completion Date:
 [08/02/2025]

Technologies:
 Python 3.7+, HTML5, CSS3, JavaScript, Tailwind CSS

For questions about this project or internship tasks:

📧 
Email:
 [gaurav8296p@gmail.com]
💼 
LinkedIn:
 [www.linkedin.com/in/gaurav-patel-3b516a241]
🐱 
GitHub:
 [(https://github.com/gpatel8785)]
📄 License

This project is created as part of the Prodigy InfoTech Software Development Internship program.

⭐ If you found this project helpful, please give it a star! ⭐

Made with ❤️ for Prodigy InfoTech Software Development Internship

🎯 Key Features of This README

✅ Professional Structure:

Clear sections with navigation
Beautiful badges and formatting
Comprehensive documentation
Visual hierarchy with emojis
✅ Complete Information:

All requirements clearly marked as fulfilled
Technical specifications
Usage examples
API integration guide
✅ Visual Appeal:

Professional badges
Structured tables
Code examples
Screenshot placeholders
✅ Internship Focus:

Clearly identifies this as Prodigy InfoTech Task-01
Shows requirements fulfillment
Demonstrates professional documentation skills
