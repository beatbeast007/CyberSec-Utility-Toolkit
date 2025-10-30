# CyberSec-Utility-Toolkit
A collection of beginner-friendly cybersecurity Python utilities.
# CyberSec-Utility-Toolkit 🔒
A collection of beginner-friendly cybersecurity Python utilities for learning and educational purposes.
## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tools Included](#tools-included)
- [Contributing](#contributing)
- [License](#license)
## 🎯 About
CyberSec-Utility-Toolkit is a curated collection of Python-based cybersecurity utilities designed for beginners and enthusiasts. These tools demonstrate fundamental security concepts and provide hands-on learning opportunities for understanding various cybersecurity domains.
**⚠️ Disclaimer**: These tools are for educational purposes only. Always ensure you have proper authorization before using any security testing tools.
## ✨ Features
- **Beginner-Friendly**: Simple, well-commented code suitable for learning
- **No Dependencies (mostly)**: Most tools use Python standard library
- **Educational**: Each tool demonstrates specific security concepts
- **Open Source**: MIT licensed for learning and modification
## 🚀 Installation
### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)
### Clone the Repository
```bash
git clone https://github.com/beatbeast007/CyberSec-Utility-Toolkit.git
cd CyberSec-Utility-Toolkit
```
### Install Dependencies (if needed)
Some tools may require additional libraries:
```bash
pip install pillow  # For metadata_remover.py
```
## 📖 Usage
Navigate to the `tools` directory and run any tool:
```bash
cd tools
python tool_name.py
```
Each tool will prompt you for the required inputs.
## 🛠️ Tools Included
### 1. **DNS Lookup Tool** (`dns_lookup_tool.py`)
Resolve domain names to IP addresses using DNS queries.
```bash
python dns_lookup_tool.py
```
### 2. **Hash Identifier** (`hash_identifier.py`)
Identify the type of hash algorithm based on hash length (MD5, SHA1, SHA256, etc.).
```bash
python hash_identifier.py
```
### 3. **Metadata Remover** (`metadata_remover.py`)
Remove EXIF metadata from image files for privacy protection.
```bash
python metadata_remover.py
```
*Requires: Pillow library*
### 4. **Password Strength Checker** (`password_strength_checker.py`)
Analyze password strength based on length, complexity, and character variety.
```bash
python password_strength_checker.py
```
### 5. **Port Scanner** (`port_scanner.py`)
Scan network ports to identify open services on a target host.
```bash
python port_scanner.py
```
*Note: Only use on networks you own or have permission to test*
### 6. **URL Phishing Detector** (`url_phishing_detector.py`)
Analyze URLs for common phishing indicators and suspicious patterns.
```bash
python url_phishing_detector.py
```
### 7. **WiFi Password Extractor** (`wifi_password_extractor.py`)
Extract saved WiFi passwords from Windows systems (Windows only).
```bash
python wifi_password_extractor.py
```
*Note: Requires administrator privileges on Windows*
## 🤝 Contributing
We love contributions! This project is perfect for Hacktoberfest and first-time contributors.
Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.
## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## 🌟 Acknowledgments
- Thanks to all contributors who help improve this toolkit
- Inspired by the cybersecurity community's commitment to education
## 📞 Contact
For questions or suggestions, please open an issue on GitHub.
---
**Happy Hacking! (Ethically, of course! 😊)**
