# RESTAPI 

## Project Overview
This project sets up a REST API for managing products using Django and Django REST Framework. The API allows users to interact with product data, including listing, creating, updating, and deleting products.

## Setting up the Environment
1. Clone the Repository
 -Open your terminal and navigate to the directory where you want to clone the repository
-Use the following command to clone the repository: 'git clone
https://github.com/CynthiaWKamau/RESTAPI.git

2. Create a virtual Environment
-Using 'python -m venv .venv'
'.\.venv\Script\Activate.ps1'
'pip install django'

3. Install Dependancies
-Use pip to install required dependancies: 'pip install -r requirements.txt'

 4. Set up database
 -Run 'python manage.py makemigrations' to create database


 ## Running the API server
 1. Start the Django Development Server
 -Run 'python manage.py runserver' to start the server
 -Open your web browser and navigate to 'http://localhost:8000/' or ' http://127.0.0.1:8000/' to view the API

 2. Accessing the Admin Panel
 -Open your web browser and navigate to 'http://127.0.0.1:8000/admin/' to access the admin panel.
 -Log in with the superuser credentials (As shown below)

 3. Creating a Superuser (Admin)
 -**Run 'python manage.py createsuperuser' to create a superuser**
 
 -Enter the required details to create a superuser
 Where one will be prompted to enter:

 -**Username: Enter a username for the superuser**

 -**Email: Enter an email for the superuser**

 -**Password: Enter a password for the superuser**

 -**Password (again): Confirm the password**

 -**Press Enter to confirm the details**

 ## Testing the API Endpoints
 # API Endpoints
 - **GET /api/products/**: Retrieves a list of all products
 - **POST/api/products/**: Creates a new product
 - **GET /api/products/{id}/**: Retrieves a product by id
 - **PUT /api/products/{id}/**: Updates a product by id
 - **DELETE /api/products/{id}/**: Deletes a product by id

 ## Testing with client.py
 -Create client.py file
 -Run 'python client.py' to test the API endpoints





