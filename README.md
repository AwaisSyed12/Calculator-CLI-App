# Calculator CLI App

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: PEP 8](https://img.shields.io/badge/Code%20Style-PEP%208-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

A professional command-line calculator application built with Python, featuring basic arithmetic operations with robust error handling and an intuitive user interface.

## 🎯 Project Overview

This calculator application demonstrates professional Python development practices while providing essential arithmetic functionality through a clean command-line interface. Built following software engineering best practices including modular design, comprehensive error handling, and user-friendly interaction patterns.

### ✨ Key Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division
- **Robust Error Handling**: Input validation and division-by-zero protection
- **Continuous Operation**: Loop-based menu system for multiple calculations
- **Professional Interface**: Clean CLI with formatted menus and clear feedback
- **Modular Architecture**: Well-structured functions following single responsibility principle
- **Input Validation**: Comprehensive validation for both numbers and menu choices

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Terminal/Command Prompt

### Installation & Usage

1. **Clone the repository:**                                                                                                                                        
git clone https://github.com/AwaisSyed12/Calculator-CLI-App.git                                                                                        
cd python-command-line-calculator

3. **Run the calculator:**                                                                                                                                          
python calculator.py

5. **Follow the interactive menu:**

==================================================

COMMAND-LINE CALCULATOR
Select an operation:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Exit

Enter your choice (1-5):

## 💻 Usage Examples

### Basic Calculation
Enter your choice (1-5): 1

You selected: Addition
Enter first number: 25
Enter second number: 30

Result: 25.0 + 30.0 = 55.0
Do you want to perform another calculation? (y/n): n

### Error Handling
Enter your choice (1-5): 4

You selected: Division
Enter first number: 10
Enter second number: 0

Error: Division by zero is not allowed!

## 🏗️ Project Structure

Calculator-CLI-App/
│
├── calculator.py # Main application file
├── README.md # Project documentation
├── screenshots/ # Application screenshots
│ ├── menu-interface.png
│ ├── calculation-demo.png
│ └── error-handling.png
└── docs/
└── task1-submission.pdf # Complete documentation


## ⚙️ Technical Implementation

### Architecture

The application follows a **modular architecture** with clear separation of concerns:

- **Operation Functions**: Dedicated functions for each arithmetic operation
- **Input Handling**: Robust validation and error recovery
- **User Interface**: Clean menu system with professional formatting
- **Control Flow**: Main loop with graceful exit handling

### Key Functions

| Function | Purpose |
|----------|---------|
| `add(x, y)` | Addition operation |
| `subtract(x, y)` | Subtraction operation |
| `multiply(x, y)` | Multiplication operation |
| `divide(x, y)` | Division with zero-division protection |
| `get_number()` | Input validation for numeric values |
| `display_menu()` | Professional menu interface |
| `perform_calculation()` | Execute operations and display results |

### Error Handling Features

- ✅ **Input Validation**: Handles non-numeric inputs gracefully
- ✅ **Menu Validation**: Ensures valid menu choice selection
- ✅ **Division Protection**: Prevents division by zero errors
- ✅ **Exception Management**: Comprehensive try/catch error handling
- ✅ **User Guidance**: Clear error messages and recovery instructions

## 🛠️ Development Practices

### Software Engineering Standards
- **PEP 8 Compliance**: Professional Python coding standards
- **Modular Design**: Single responsibility principle applied
- **Documentation**: Comprehensive docstrings and comments
- **Error Resilience**: Robust exception handling throughout
- **User Experience**: Intuitive interface with clear feedback

### Agile Development Approach
- **Iterative Development**: Core functionality first, enhancements added
- **User-Centered Design**: Focused on ease of use and clarity
- **Quality Assurance**: Extensive testing of edge cases and error conditions

## 📊 Features Demonstration

### Core Requirements Met ✅
- [x] Functions for each operation (+, -, *, /)
- [x] User input using `input()`
- [x] Loop until user chooses to exit
- [x] Well-structured code schema

### Professional Enhancements ✅
- [x] Comprehensive error handling and input validation
- [x] Professional CLI interface with visual formatting
- [x] Modular architecture following best practices
- [x] Detailed documentation and code comments

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Awais Syed**
- 🔗 GitHub: [@AwaisSyed12](https://github.com/AwaisSyed12)
- 📧 Email: awaissyed1212@gmail.com

## 🙏 Acknowledgments

- Built as part of Python Developer role assessment
- Follows industry best practices for software development
- Demonstrates proficiency in Python fundamentals and professional coding standards

---

⭐ **Star this repository if you found it helpful!**
