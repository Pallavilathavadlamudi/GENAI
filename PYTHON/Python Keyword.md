# Python keywords

| `False`      | `def`        | `if`         | `raise`      |
| `None`       | `del`        | `import`     | `return`     |
| `True`       | `elif`       | `in`         | `try`        |
| `and`        | `else`       | `is`         | `while`      |
| `as`         | `except`     | `lambda`     | `with`       |
| `assert`     | `finally`    | `nonlocal`   | `yield`      |
| `break`      | `for`        | `not`        |              |
| `class`      | `from`       | `or`         |              |
| `continue`   | `global`     | `pass`       |              |

Explanation:

| **Keyword** | **Definition**                                                                     |
| ----------- | ---------------------------------------------------------------------------------- |
| `False`     | Boolean value representing false.                                                  |
| `None`      | Represents the absence of a value.                                                 |
| `True`      | Boolean value representing true.                                                   |
| `and`       | Logical AND operator.                                                              |
| `as`        | Used to create an alias, especially in `import` statements and exception handling. |
| `assert`    | Used to debug code by checking conditions.                                         |
| `break`     | Exits the current loop prematurely.                                                |
| `class`     | Defines a new class.                                                               |
| `continue`  | Skips the rest of the current loop and moves to the next iteration.                |
| `def`       | Declares a function.                                                               |
| `del`       | Deletes a variable or object.                                                      |
| `elif`      | Used in conditional statements, meaning "else if".                                 |
| `else`      | Executes a block if the condition in `if` or `elif` is false.                      |
| `except`    | Catches exceptions in try-except blocks.                                           |
| `finally`   | Block that always runs after try-except, used for cleanup.                         |
| `for`       | Starts a for loop.                                                                 |
| `from`      | Used with `import` to specify the module to import from.                           |
| `global`    | Declares a variable as global (outside all functions).                             |
| `if`        | Starts a conditional statement.                                                    |
| `import`    | Imports a module.                                                                  |
| `in`        | Checks for membership (e.g., if element exists in a list).                         |
| `is`        | Checks for object identity (whether two references point to the same object).      |
| `lambda`    | Creates an anonymous function.                                                     |
| `nonlocal`  | Refers to variables in the nearest enclosing scope that is not global.             |
| `not`       | Logical NOT operator.                                                              |
| `or`        | Logical OR operator.                                                               |
| `pass`      | A placeholder that does nothing; used where code is syntactically required.        |
| `raise`     | Raises an exception.                                                               |
| `return`    | Exits a function and optionally returns a value.                                   |
| `try`       | Starts a block to catch exceptions.                                                |
| `while`     | Starts a while loop.                                                               |
| `with`      | Used to wrap the execution of a block with methods defined by a context manager.   |
| `yield`     | Returns a generator from a function.                                               |

# Identifiers & Variables

    Python Identifiers:

        Python Identifier is the name we give to identify a variable, function, class, module or other object.

        Sometimes variable and identifier are often misunderstood as same but they are not

    Variable:

        A variable, as the name indicates is something whose value is changeable over time. 
        In fact a variable is a memory location where a value can be stored. 
        Later we can retrieve the value to use. 
        But for doing it we need to give a nickname to that memory location so that we can refer to it. 
        That’s identifier, the nickname.

        Example:

        myVariable = "hello world"
            print(myVariable)

        explanation:

        myVariable -> Identifier
        "hello world" -> Value Stored
        print(my variable) -> This outputs the value by using the identifier

        var1 = 1
            print(var1)

        explanation:

        var1 -> Identifier
        "1" -> Value Stored
        print(var1) -> This outputs the value by using the identifier


| Term       | Description                            | Example                             |
| ---------- | -------------------------------------- | ----------------------------------- |
| Identifier | The name used to identify a variable   | `myVariable`                        |
| Variable   | A memory location holding the value    | `myVariable` stores `"hello world"` |
| Value      | The actual data stored in the variable | `"hello world"`                     |

Types of Variable

| Type                | Where it's defined   | Where it's accessible     |
| ------------------- | -------------------- | ------------------------- |
| **Local Variable**  | Inside a function    | Only inside that function |
| **Global Variable** | Outside any function | Anywhere in the program   |

# Rules for writing Identifiers?

    1. Python is a case sensitive
        
        example:
            Name and name are 2 different identifiers in python.

Rules:

1. Identifiers can be combination of uppercase and lowercase letters, digits or an underscore(_). 
    So myVariable,variable_1, variable_for_print all are valid python identifiers.

2. An Identifier can not start with digit. 
    So while variable1 is valid, 1variable is not valid.

3. We can’t use special symbols like !,#,@,%,$ etc in our Identifier.

4. Identifier can be of any length.

Do consider;

    Absolutely! Below is a well-structured example program that demonstrates:

    ✅ Class names with uppercase
    ✅ Identifiers starting with lowercase
    ✅ Private identifiers with leading underscore (_name)
    ✅ Language-defined special method (__init__)
    ✅ Meaningful variable names (count, not just c)
    ✅ Underscore to separate multiple words (this_is_a_variable)

Example: 

    # Class name starts with uppercase letter
    class Student:
        
        # Language-defined special method (constructor)
        def __init__(self, name, age):
            # Private attribute (by convention, starts with underscore)
            self._name = name
            self.age = age

    # Regular method
    def display_info(self):
        print("Student Name:", self._name)
        print("Student Age:", self.age)

    # Using meaningful variable names
    student_count = 1

    # Multiple words in identifier separated with underscore
    first_student = Student("Alice", 20)

    # Call a method on the object
    first_student.display_info()

    # Print count
    print("Total students:", student_count)

Explanation:

| Identifier       | Type              | Why it's used                 |
| ---------------- | ----------------- | ----------------------------- |
| `Student`        | Class Name        | Starts with uppercase         |
| `student_count`  | Variable          | Meaningful & descriptive      |
| `first_student`  | Variable          | Uses underscores, descriptive |
| `_name`          | Private attribute | Convention for "private"      |
| `__init__`       | Special method    | Built-in method in Python     |
| `display_info()` | Method            | Verb-based, clear meaning     |

# Python Naming Conventions

| **Element**           | **Convention**                       | **Example**                         |
| --------------------- | ------------------------------------ | ----------------------------------- |
| **Variables**         | lowercase\_with\_underscores         | `student_name`, `total_count`       |
| **Functions**         | lowercase\_with\_underscores         | `calculate_total()`, `print_info()` |
| **Classes**           | CapitalizedWords (PascalCase)        | `Student`, `BankAccount`            |
| **Constants**         | ALL\_UPPERCASE\_WITH\_UNDERSCORES    | `PI = 3.14`, `MAX_USERS = 100`      |
| **Private variables** | \_single\_leading\_underscore        | `_password`, `_temp_value`          |
| **Strongly private**  | \_\_double\_leading\_underscore      | `__secret_key` (name mangling)      |
| **Special methods**   | **double\_leading\_and\_trailing**   | `__init__`, `__str__`               |
| **Modules / files**   | lowercase\_with\_underscores         | `user_profile.py`                   |
| **Packages**          | lowercase (no underscores preferred) | `mypackage`, `utils`                |

# Instructions:

    1. Comment: 
        A comment is a short note in the code that explains what the code is doing.
        It starts with a # and is ignored by Python when the code runs.

        Example:

            # This adds two numbers
            a = 5 + 3


    2. Docstring:
        A docstring is a special message placed at the beginning of a function, class, or program to describe what it does.
        It uses triple quotes """ """ and can be read by tools like help().

        Example:

            def greet(name):
            """This function prints a greeting message."""
            print("Hello", name)

Comments vs Docstrings:

| Feature   | Comments          | Docstrings                            |
| --------- | ----------------- | ------------------------------------- |
| Symbol    | `#`               | `""" """` or `''' '''`                |
| Scope     | Anywhere in code  | Only inside functions/classes/modules |
| Purpose   | Brief explanation | Formal documentation                  |
| Execution | Ignored by Python | Stored in `__doc__`                   |
| Style     | Short & informal  | Full sentences, formal tone           |

Summary

| Use            | When                                                           |
| -------------- | -------------------------------------------------------------- |
| **Comments**   | To explain tricky parts of logic, short notes                  |
| **Docstrings** | To explain what a function/class/module does, its input/output |

# Indentation

Indentation means adding spaces at the beginning of a line to show that it belongs to a block of code.
Python uses indentation to group code — it's required, not just for style

    Example: 

        if age >= 18:
        print("You are an adult")  # This line is indented — part of the if block

Without indentation, Python will show an error.