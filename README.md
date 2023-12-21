# Flask Web Application Deploy to Google APP Engine

## Description
This repository contains a Flask web application showcasing a modern, responsive single-page design. The app displays a static webpage with a vibrant color scheme and an animated button.

## Features
Modern UI Design: A clean and responsive user interface.
Interactive Elements: Animated button with a "breather" effect.
## Test Suite: 
Basic unit tests for application functionality.
Tech Stack
## Flask: 
Web framework for serving the HTML page.
## HTML/CSS: 
Frontend design with gradient background and modern typography.
## Google App Engine:
 Deployment platform for hosting the web application.
Setup and Installation
Clone the repository.
## Install dependencies: 
`pip install -r requirements.txt`
Run the application: `python app.py`
## GitHub Workflow
## CI/CD Pipeline: 
The `app_engine_deploy.yml` file defines a GitHub Actions workflow named "Build, Test, and Deploy to Google App Engine." It triggers on pushes to the main branch or via manual workflow dispatch.<br> 
The workflow consists of three jobs:

### Build: 
1. Checks out the code
2. sets up Python 3.8
3. installs dependencies
4. runs a build test script. 
   
The success of this step is outputted for later use.

### Test: 
Depends on the build job's success. It repeats the setup steps and then runs application-specific tests.

### Deploy: 
Activates only if the test job succeeds. It again checks out the code, sets up Google Cloud SDK with provided credentials, and deploys the application to Google App Engine using gcloud app deploy.

This workflow ensures that every push to main or manual dispatch is built, tested, and, if successful, deployed automatically.

## Testing
To run the Flask application defined in `app.py`, follow these steps:

### Prerequisites
1. **Python**: Ensure you have Python installed on your system. This project requires Python 3.6 or higher. You can download Python from [python.org](https://www.python.org/downloads/).

2. **pip**: Ensure you have pip, the Python package installer, which usually comes with Python.

3. **Virtual Environment (Optional but Recommended)**: It's a good practice to use a virtual environment to manage dependencies for your project. You can create one using Python's built-in `venv` module:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
   This command creates a new virtual environment named `venv` and activates it.

### Installation Steps
1. **Clone the Repository**

   ```bash
   git clone https://github.com/kunalworldwide/python-deployment-demo.git
   cd python-deployment-demo

2. **Install Dependencies**: Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. **Set Environment Variables**: Before running the app, you need to set the `FLASK_APP` environment variable to tell Flask which file to run. In your terminal, execute:
   ```bash
   export FLASK_APP=app.py  # On Windows, use `set FLASK_APP=app.py`
   ```

2. **Run the Flask Application**: Now, you can start the Flask application by running:
   ```bash
   flask run
   ```
   Alternatively, you can directly run `app.py` if it has an executable script at the bottom:
   ```bash
   python app.py
   ```

3. **Access the Application**: Once the application is running, you can access it by navigating to `http://localhost:5000` in your web browser (or the port you have configured, if different).

### Notes
- Ensure that the `app.py` file is in the root of your project directory or specify the correct path while setting the `FLASK_APP` environment variable.
- If you encounter any issues, check the console for error messages which can help in troubleshooting.
  
## Collaborators

- [Santanu Kumar Das](https://github.com/santanukumardas) - Contributed to the project's development and design.
- [Kunal Das](https://github.com/kunalworldwide) - Assisted in refining features and testing.