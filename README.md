 # 0x00 - AirBnB clone - The Console

This is a command line interpreter to manage our Holberton AirBnB clone objects. Functionality includes:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database, etc...
* Do operations on objects (count, compute stats, etc..)
* Update attributes of an object
* Destroy an object

The command line interpreter puts in place a parent class (called [BaseModel](models/base_model.py)) to take care of the initialization, serialization, & deserialization of future instances. It creates a simple flow of serialization/deserialization: 

`Instance <-> Dictionary <-> JSON string <-> file`

The interpreter creates all classes used for AirBnB ([User](models/user.py), [State](models/state.py), [City](models/city.py), [Place](models/place.py)...) that inherit from [BaseModel](models/base_model.py).

In this project we also created the first abstracted storage engine for the project: [File Storage](models/engine/file_storage.py), as well as created [Unittests](/test/) to validate all the classes & storage engine.

 ## Usage

The interpreter works like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```

Task # | Short Description
-------|------------
[Task 0](AUTHORS) | Authors file & README for the project.
[Task 2](test/) | Unittests
[Task 3](models/base_model.py) | Class `BaseModel`, containing public instance attributes & methods.
[Task 4](models/base_model.py) | Class `BaseModel`, updated with __init__ to construct a `BaseModel` from a dictionary representation of an instance.
[Task 5](models/base_model.py) | Class `BaseModel`, updated to convert dict rep to a JSON string, & save that string to file, as well as load from file.
[Task 5](models/engine/file_storage.py) | Class `FileStorage` that serializes instances to a JSON file & deserializes JSON file to instances. 
[Task 6](console.py) | Command interpreter console, uses module `cmd`. Basic functionality of console in this step.
[Task 7](console.py) | Update console to add commands: `create`, `show`, `destroy`, `all`, `update`.
[Task 8](models/user.py) | Class `User` that inherits from `BaseModel` some public class attributes, as well as update to `FileStorage` to manage correctly serialization & deserialization of `User`. Update console to allow commands to be used with `User`.
[Task 9](models/state.py) | Class `State`.
[Task 9](models/city.py) | Class `City`.
[Task 9](models/amenity.py) | Class `Amenity`.
[Task 9](models/place.py) | Class `Place`.
[Task 9](models/review.py) | Class `Review`.
[Task 10](console.py) | Update `FileStorage` to manage correctly serialization & deserialization of the new classes from Task 9. Update console to allow commands to work with the new classes.
[Task 11]() | **ADVANCED** Coming soon!

 ## Lessons Learned
* How to create a Python package
* How to create a command interpreter in Python using the `cmd` module
* What is Unit testing & how to implement it in a large project
* How to serialize & deserialize a Class
* How to write & read JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` & how to use it
* What is `**kwargs` & how to use it
* How to handle named arguments in a function
