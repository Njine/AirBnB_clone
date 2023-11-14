## Description
	To construct our initial full-fledged web application: the AirBnB clone. During this initial stage, a fundamental console has been developed using the Cmd Python module. This console serves as the command-line interface for managing objects throughout the entire project. It encompasses the implementation of essential methods such as create, show, update, all, and destroy for both the existing classes and their subclasses.


##Files



├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
├── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py


## Usage
***Methods***

1. create
Creates an object of a given class.

**Description:**
Creates a new instance of the specified class.

*Usage:*

create <class_name>

2. show
Prints the string representation of an instance based on the class name and id.

**Description:**
Displays the details of a specific instance.

*Usage:*

show <class_name> <instance_id>

3. all
Prints all string representations of instances based on the class name or lists all instances.

**Description:**
Displays all instances of a given class or all instances if no class is specified.

*Usage:*

all [class_name]

4. update
Updates an instance based on the class name and id by adding or updating an attribute. The change is saved into the JSON file.

**Description:**
Modifies the attributes of a specific instance and saves the changes.

*Usage:*

update <class_name> <instance_id> <attribute_name> <new_value>

5. destroy
Deletes an instance based on the class name and id. The change is saved into the JSON file.

**Description:**
Removes a specific instance from the storage and saves the changes.

*Usage:*

destroy <class_name> <instance_id>

6. count
Retrieves the number of instances of a class.

**Description:**
Counts and displays the number of instances of a specified class.

*Usage:*

count <class_name>

7. help
Prints information about a specific command.

**Description:**
Provides detailed information about the usage and purpose of a command.

*Usage:*

help <command>

8. quit / EOF
Exits the program.

**Description:**
Closes the console and exits the program.

*Usage:*

quit or EOF
