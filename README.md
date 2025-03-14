Project Overview
This is a simple Django REST API that allows you to manage user data. The API provides CRUD (Create, Read, Update, and Delete) operations for user records, which include name, email, and age.

Tech Stack
•	Programming Language: Python
•	Backend Framework: Django, Django Rest Framework (DRF)
•	Database: SQLite3

Installation & Setup
1) Clone the Repository
t clone [https://github.com/Rahemat-12/Crud_Operation/upload/main](https://github.com/Rahemat-12/Crud_Operation.git)

2) Database Migration
python manage.py makemigrations
python manage.py migrate

3) Run the Server
API will be available at: http://127.0.0.1:8000/


API Endpoints
Method	Endpoint	Description
POST 	/users/create/	Create a new user
GET	/users/	Retrieve all users
GET	/users/{user_id}/	Retrieve a single user
PUT	/users/{user_id}/update/	Update user details
DELETE	/users/{user_id}/delete/	Delete a user



How to Use the API

1) Create a User
	POST http://127.0.0.1:8000/users/create/
{"name": "Virat",  "email": "Virat18@gmail.com", "age": 34}

Output:
{
    "message": "User created successfully",
    "data": {
        "name": "Virat",
        "email": "Virat18@gmail.com",
        "age": 34
    }
}

2) Retrieve All Users
 	GET http://127.0.0.1:8000/users/

3) Retrieve a Single User by ID
GET http://127.0.0.1:8000/users/1/

4) Update a User
	http://127.0.0.1:8000/users/1/update/
{"name": "Virat  Kohli", "email": "Kohli@gmail.com", "age": 30}

5) Delete a User
DELETE http://127.0.0.1:8000/users/1/delete/

