# Resume Detector App

An application to detect whether an uploaded file is a resume based on its content.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Resume Detector App is designed to analyze text content in various file formats, such as PDF, DOCX, and TXT, to determine if it contains information typically found in a resume.

## Features

- File format support: PDF, DOCX, TXT
- Detection of resume-related keywords: education, experience, skills

## Installation

To set up the Resume Detector App locally, ensure you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

Follow these steps to install and run the application:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ResumeDetector.git
    cd ResumeDetector
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

6. **Open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/).**

Now, you're ready to use the Resume Detector App locally. Upload a file using the provided form to check if it is a resume.

## Usage

To use the application, follow the steps outlined in the [Installation](#installation) section. Once the application is running, open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/). Upload a file using the provided form to check if it is a resume.

## Contributing

If you would like to contribute to the development of the Resume Detector App, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
