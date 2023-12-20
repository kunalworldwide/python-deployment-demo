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
Run the provided test suite with: `python test_app.py`