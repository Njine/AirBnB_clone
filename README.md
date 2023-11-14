## Description
To construct our initial full-fledged web application:
The AirBnB clone. During this initial stage, a fundamental console has been developed using the Cmd Python module.
This console serves as the command-line interface for managing objects throughout the entire project. It encompasses the implementation of essential methods such as create, show, update, all, and destroy for both the existing classes and their subclasses.


## Files

## Files

| File/Folder                    | Description                         |
| ------------------------------ | ----------------------------------- |
| `AUTHORS`                       | Authors of the project              |
| `console.py`                   | Main console script                 |
| `models/`                      | Directory for Python modules        |
| ├── `amenity.py`                | Amenity class module                |
| ├── `base_model.py`             | BaseModel class module              |
| ├── `city.py`                   | City class module                   |
| ├── `engine/`                   | Engine directory                    |
| │   ├── `file_storage.py`       | FileStorage class module            |
| │   └── `__init__.py`           | Initialization script for engine    |
| ├── `__init__.py`               | Initialization script for models    |
| ├── `place.py`                  | Place class module                  |
| ├── `review.py`                 | Review class module                 |
| ├── `state.py`                  | State class module                  |
| └── `user.py`                   | User class module                   |
| `README.md`                     | Project README file                 |
| `tests/`                        | Directory for test scripts           |
| ├── `__init__.py`               | Initialization script for tests     |
| └── `test_models/`              | Directory for model tests           |
| ├── `__init__.py`               | Initialization script for model tests |
| ├── `test_amenity.py`           | Amenity class test script           |
| ├── `test_base_model.py`        | BaseModel class test script         |
| ├── `test_city.py`              | City class test script               |
| ├── `test_engine/`              | Directory for engine tests          |
| │   ├── `__init__.py`           | Initialization script for engine tests |
| │   └── `test_file_storage.py`  | FileStorage class test script       |
| ├── `test_place.py`             | Place class test script             |
| ├── `test_review.py`            | Review class test script            |
| ├── `test_state.py`             | State class test script             |
| └── `test_user.py`              | User class test script              |



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
