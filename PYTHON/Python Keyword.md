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
