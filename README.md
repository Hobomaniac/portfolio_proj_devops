# DevOps Project
This is a project for the DevOps bootcamp course. It is a store app, that in which you can sell products, add/remove employees, add/remove products, and keeps tracks of orders. It's going to be pretty basic. It uses django, psql, and docker

## Getting Started
These instructions will get you a copy of the project up and running on your local machine, with access to the admin. This is all it'll be doing for now until I get some functionality into it.

## Prerequisites
* Python 3
* Docker
* pip

## Installation
1. Clone the repository: git clone https://github.com/Hobomaniac/portfolio_proj_devops.git

2. Navigate to the project directory with the docker-compose.yml file.

3. Run the docker compose command: docker compose up -d

4. Navigate to the project directory with the manage.py and run: docker compose exec web python manage.py createsuperuser

5. Enter a username, email(optional), and password

The application should now be running at http://localhost:8000.

## Usage
Once the server is running, you can navigate to http://localhost:8000 in your web browser to use the django-admin. Enter in your username and password.
Also run tests with the pytest command.
