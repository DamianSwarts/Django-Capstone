# Django Capstone Project

This is a Django capstone project that showcases the skills and knowledge acquired in the Advanced Software Engineering course. It is a web application that allows users to view and interact with a fictional band.

## Features

- User authentication and authorization
- Band member profiles and contact information
- User-friendly documentation generated with Sphinx

## Installation

To install and run this project, you need to have Python 3.9 and Git installed on your computer. You also need to have Docker or venv to create a virtual environment for the project.

### With Docker:

- Clone the repository from GitHub:

```bash
git clone https://github.com/DamianSwarts/Django-Capstone

- Change to the project directory:
cd Django-Capstone

- Build the Docker image for the project:
docker build -t Django-Capstone .

- Run the Docker container for the project:
docker run -p 8000:8000 django-capstone

- Access the project from your browser at http://localhost:8000

With venv:

- Clone the repository from GitHub:
git clone https://github.com/DamianSwarts/Django-Capstone

- Change to the project directory:
cd Django-Capstone

- Create a virtual environment for the project:
python -m venv venv

- Activate the virtual environment:
source venv/bin/activate # for Linux or macOS
venv\Scripts\activate.bat # for Windows

- Install the required packages for the project:
pip install -r requirements.txt

- Run the Django development server for the project:
python manage.py runserver

- Access the project from your browser at http://localhost:8000

Testing and Debugging
To test and debug the project, you can use the following tools and commands:

- To run the unit tests for the project, you can use pytest:
pytest

- To see the logs and errors for the project, you can use logging:
python manage.py runserver --verbosity 2

- To inspect the requests and responses for the project, you can use Django debug toolbar:
pip install django-debug-toolbar

Contributing
To contribute to the project, you can follow these steps:

- Fork the repository on GitHub
- Clone your forked repository to your local machine
- Create a new branch for your feature or bug fix
- Make your changes and commit them with a descriptive message
- Push your branch to your forked repository
- Create a pull request from your branch to the original repository
- Wait for the code review and feedback

Contact
If you have any questions or suggestions, please feel free to contact me:

Name: Damian Swarts
Email: damianswarts2019@gmail.com
GitHub: https://github.com/DamianSwarts
