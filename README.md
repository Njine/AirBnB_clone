Description of the Project
This project is a command-line interface (CLI) designed for the Airbnb Clone project. The CLI interacts with a simple object-relational mapping (ORM) system and provides various commands to manipulate instances of different classes. The project includes a base model, and users can create, show, destroy, update, and list instances.

***Command Interpreter***

How to Start

To start the command interpreter, run the following command in your terminal:

***./console.py***

How to Use
Once the command interpreter is running, you can use the following commands:

create: Creates a new instance of a specified class and prints its ID.

---create <class>

show: Displays the string representation of a class instance based on the class name and ID.

---show <class> <id>

destroy: Deletes an instance based on the class name and ID.

---destroy <class> <id>

all: Prints string representations of all instances based on the class name.

---all <class>

count: Retrieves the number of instances of a given class.

---count <class>

update: Updates an instance based on the class name and ID by adding or updating an attribute key/value pair or dictionary.

---update <class> <id> <attribute_name> <attribute_value>

Examples

*Create a new instance of BaseModel and print its ID:

---create BaseModel

*Show the string representation of a BaseModel instance with a specific ID:

---show BaseModel 1234-5678

*Destroy an instance of BaseModel with a specific ID:

---destroy BaseModel 1234-5678

*Display string representations of all instances of BaseModel:

---all BaseModel

*Retrieve the number of instances of BaseModel:

---count BaseModel

*Update an attribute of a BaseModel instance:

---update BaseModel 1234-5678 name "New Name"
