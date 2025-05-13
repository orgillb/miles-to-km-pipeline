# Miles to Kilometers CI/CD Project

A complete CI/CD pipeline for a GUI-based Python application, designed to demonstrate Windows software deployment, automated testing, and executable packaging — using industry-standard tools.

## 💡 Project Overview

This project simulates a real-world deployment scenario for a simple desktop utility app. It includes:

- Automated testing
- Executable packaging
- Jenkins-based continuous integration
- Test coverage reporting
- Windows installer generation

## 🧰 Tech Stack

- **Python** (Anaconda)
- **Tkinter** – for GUI
- **unittest** – for testing
- **coverage.py** – to measure test coverage
- **PyInstaller** – to package the app into a `.exe`
- **Inno Setup** – to create a Windows installer
- **Git + GitHub** – version control and hosting
- **Jenkins** – CI/CD orchestration

## 🚀 Pipeline Workflow

1. **Code pushed to GitHub**
2. **Jenkins Build Triggered**:
    - Clone repo from GitHub
    - Activate Anaconda environment
    - Run unit tests using `coverage`
    - Display test coverage in build logs
    - Build a `.exe` using PyInstaller
3. (Optional) Create a full installer using Inno Setup
4. (Optional) Archive `.exe` as Jenkins artifact

## 📁 Project Structure

```
miles-to-km-pipeline/
├── miles_to_km.py          # GUI entry point
├── converter.py            # Business logic
├── test_converter.py       # Unit tests
├── installer.iss           # Inno Setup script (optional)
├── dist/                   # PyInstaller output (.exe)
├── htmlcov/                # Coverage HTML report (optional)
├── screenshots/            # Images for documentation
```

## 🧪 Test Coverage Output

![Test Coverage](screenshots/test_coverage.png)

This project achieved 95% total test coverage across logic and tests.

## 📸 Screenshots

- Jenkins Dashboard  
  ![Jenkins Dashboard](screenshots/jenkins_dashboard.png)

- Build Output with Coverage  
  ![Build Output](screenshots/jenkins_console_output.png)

- Application GUI  
  ![App GUI](screenshots/app_gui.png)

- Windows Installer  
  ![Installer](screenshots/installer_wizard.png)

> 📍 Upload your screenshots into `/screenshots` folder in the repo.

## ✅ Key Takeaways

- Used Jenkins to orchestrate a full build-test-package workflow
- Demonstrated automated testing with real coverage metrics
- Built `.exe` and installer with zero manual steps
- Simulated a full deployment engineer workflow

---

## 🤝 Contact

Created by Brett Orgill  
[GitHub](https://github.com/orgillb) | *Deployment & Automated Testing Engineer Candidate*
