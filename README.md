 # 0x00 - AirBnB clone - The Console
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
