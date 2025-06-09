# Flowchart

    Flowcharts are the visual representations of an algorithm or a process. Flowcharts use symbols/shapes like arrows, rectangles, and diamonds to properly explain the sequence of steps involved in the algorithm or process. Flowcharts have their use cases in various fields such as software development, business process modeling, and engineering.

1. Symbols:

    1. Start / End

        Symbol: 🟠 Oval / Ellipse
    
    Use: Marks where the process begins and ends.

    2. Input / Output

        Symbol: ⬛ Parallelogram
    
    Use: For user input or system output (e.g., entering values, displaying results).

    3. Process / Operation

        Symbol: 🔲 Rectangle
    
    Use: Represents a calculation, assignment, or task.

    4. Decision / Condition

        Symbol: ◇ Diamond
    
    Use: Used for if/else, true/false, yes/no decisions.

    5. Arrows / Flowlines

        Symbol: ➡️ Arrow
    
    Use: Shows direction of flow.

    6. Connector (optional)

        Symbol: ⚪ Circle
    
    Use: Jump or connect flow when it continues on another page or is too complex.

<img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/PYTHON/Assets/Flowcharts.png">

# Statements vs Conditions 

1. Statement: 

    A statement is a line of code that tells the computer to do something. It is an instruction.

    Example:
        
            x = 10              # Assignment statement
            print(x)            # Output statement
            name = input()

    Statements perform actions.
    They do not return True or False.
    They are the steps of a program.

2. Condition:

    A condition is a logical expression that checks something and returns True or False.

    Example: 
            
            x > 0               # True if x is greater than 0
            x == 5              # True if x equals 5
            age >= 18           # True if age is 18 or more 

        if x > 0:
        print("Positive number")   # This runs only if the condition is True

    Conditions are used in decisions.
    They are written using comparison operators like ==, >, <, >=, <=, !=.
    Used in: if, while, for, etc.   

    1. What is if, else, elif?

        They are used to check conditions and run different code blocks based on whether conditions are True or False.

        1. if Statement : Checks a condition.
                If the condition is True, the code inside runs.
        
        2. else Statement : 
                Runs if the if condition is False.

        3. elif Statement : (short for else if)
                Checks another condition if the first if is False.
                You can have multiple elif blocks.
     
    | Keyword | Meaning                        | Runs when...                    |
    | ------- | ------------------------------ | ------------------------------- |
    | `if`    | Check first condition          | Condition is True               |
    | `elif`  | Else if – check next condition | Previous conditions were False  |
    | `else`  | Final fallback                 | All above conditions were False |


<img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/PYTHON/Assets/Comparision.png">

# loops 

    A loop is a programming structure that repeats a set of instructions as long as a condition is true or for a fixed number of times.

    | Type          | Purpose                                 | Common Use                                  |
    | ------------- | --------------------------------------- | ------------------------------------------- |
    | `for` loop    | Repeats for a **fixed number of times** | Loops through a list, string, range, etc.   |
    | `while` loop  | Repeats **while a condition is true**   | Loop until a certain condition is met       |
    | `nested` loop | A loop **inside another loop**          | Used in matrices, patterns, or combinations |

1. for loop:

    Used when you know how many times to loop.

    Example:

        for i in range(5):
        print(i)

2. While Loop:

    Used when you want to loop until a condition is false.

    Example:
         
        x = 1
        while x <= 5:
            print(x)
            x += 1

3. Nested Loops:

    A loop inside another loop.

    Example: 

        for i in range(2):
            for j in range(3):
                print(i, j)

4. Infinite Loops:

    An infinite loop is a loop that never ends because its condition always remains true.
    This can happen with both while and for loops (though most commonly with while).

    Example: 

        Infinite Loop
            x = 1
            while x < 5:
            print(x)
            # Forgot to increment x → this loop will never stop!

        Finite Loop
            x = 1
            while x < 5:
            print(x)
            x += 1   # Now it will stop when x = 5

# Functions

    A function is a block of reusable code that performs a specific task when called.

    Think of a function like a machine: you give it input, it does something, and may return an output.

    Why Use Functions?
        
        Avoid repeating code (reusability)
        Organize code better (modularity)
        Make programs easier to read and maintain

    | Type             | Description                         | Example                       |
    | ---------------- | ----------------------------------- | ----------------------------- |
    |   Built-in       | Ready-made by Python                | `print()`, `len()`, `input()` |
    |   User-defined   | Created by you for specific tasks   | `def greet(name):`            |
    |   Lambda         | Small, anonymous one-line functions | `lambda x: x + 2`             |

    1. Built-in Functions
    
        These are functions already provided by Python.
        You can use them directly — no need to define them yourself.

        Example:

            print("Hello")       # Displays text
            len("Python")        # Returns length → 6
            input("Enter name")  # Takes input from user
            type(5)              # Returns the data type → <class 'int'>

    2. User-Defined Functions
    
        Functions that you write yourself to do a specific task.
        Useful to organize, reuse, and simplify code.

        Example:

            def greet(name):
            print("Hello,", name)
    
            greet("Pallavi")    # Output: Hello, Pallavi

    3. Lambda Functions (Anonymous Functions)
        
        Short functions with no name.
        Defined using the lambda keyword.
        Used for simple one-line tasks.

        Example:

            lambda arguments: expression

            square = lambda x: x * x
            print(square(5))      # Output: 25

# Parameters & Arguments:

    Parameter:
    
        A parameter is a variable in the function definition.
        It receives a value when the function is called.

        Example:

            def greet(name):   # ← 'name' is a parameter
            print("Hello", name)

    Argument:

        An argument is the actual value you pass into the function when calling it.

        Example:

            greet("Pallavi")   # ← "Pallavi" is an argument

    1. Key Differences?

        | Feature     | Parameter                         | Argument                   |
        | ----------- | --------------------------------- | -------------------------- |
        | Where?      | In **function definition**        | In **function call**       |
        | What is it? | A **placeholder** for input value | The **actual input value** |
        | Example     | `def greet(name):`                | `greet("Pallavi")`         |

    2. When and where to use?

        | Use Case           | What You Do                                            |
        | ------------------ | ------------------------------------------------------ |
        | Writing a function | Use **parameters** to define the inputs needed         |
        | Calling a function | Pass **arguments** (actual values) to those parameters |


    Example: 

        # Define function (parameters)
            def add(a, b):
                return a + b 

        # Call function (arguments)
            result = add(5, 3)
            print(result)    # Output: 8

        Where a,b are parameters ; 5,3 are arguments

    3. Types of arguments :

        | Type                | Example                   | Description                           |
        | ------------------- | ------------------------- | ------------------------------------- |
        |   Positional        | `greet("Pallavi")`        | Based on the order of parameters      |
        |   Keyword           | `greet(name="Pallavi")`   | Use parameter name when passing value |
        |   Default           | `def greet(name="Guest")` | Uses default if no argument is passed |
        |   Variable-length   | `def add(*numbers):`      | Accepts multiple arguments            |

