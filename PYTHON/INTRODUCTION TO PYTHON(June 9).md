
# Programming

1. Programming:

    Programming is the process of writing instructions (called code) that a computer can understand and follow to perform tasks. These instructions are written using programming languages like Python, JavaScript, C++, etc.

    In simple words:

    Programming is how humans tell computers what to do.

# Why Do we need Programming?

    We need programming because it allows us to:

    1. Automate Tasks

        Repetitive or time-consuming jobs (like sorting data, sending emails, processing images) can be automated.
    Example: Automate monthly invoice generation.

    2. Build Software

        Apps, websites, video games, operating systems, and more are built with code.
    Example: WhatsApp, Google, Microsoft Excel — all built using programming.

    3. Control Machines

        Robots, smart devices, cars, washing machines – all use code to function.
    Example: A thermostat uses programming to control temperature based on user input.

    4. Analyze Data

        In data science, programming helps you clean, analyze, and visualize data.
    Example: Python is used to detect trends in sales data or predict future stock prices.

    5. Solve Problems

        Programming allows you to create logical solutions to real-world problems.
    Example: Build a system to match job seekers with employers using matching algorithms.


# Python

    Python is a high-level, easy-to-read, general-purpose programming language used to build websites, software, automate tasks, and analyze data.

    Python is open source, so it's free for everyone to use, learn, improve, and share.

1. Why do we choose Pyhon over many other languages?

    1. Easy to Read and Learn – Python looks like English, so it’s great for beginners.
    2. Works Everywhere – You can use Python to build websites, apps, games, do data analysis, machine learning, and more.
    3. Saves Time – It has lots of built-in tools and libraries, so you write less code to do more work.

2. 🧰 Rich Libraries and Tools
    
    Python comes with thousands of libraries and tools to help you do more with less effort.

    For data: Pandas, NumPy.
    For machine learning: Scikit-learn, TensorFlow.
    For web apps: Django, Flask.
    For automation: Selenium, PyAutoGUI.

3. Why do we use python for DataScience, Machine Learning, AI?

    1. 🧠 It Reduces Complexity
    
    Python lets you focus on logic and algorithms, not complicated syntax.
    This is important in ML/AI where the concepts are already hard.
    
    Why this matters: You spend more time solving problems and less time writing code.


# Import 

The import keyword in Python is used to bring in code from another file or library so you can use it in your program.

import lets you use tools made by others, so you don’t have to write everything from scratch. 

# Packages

| **Package Name**    | **Used In**                | **Definition / Purpose**                                                            |
| ------------------- | -------------------------- | ----------------------------------------------------------------------------------- |
| `math`              | Basic Math                 | Provides basic mathematical functions like `sqrt`, `sin`, `log`, etc.               |
| `os`                | System Operations          | Interacts with the operating system (files, folders, environment variables).        |
| `sys`               | System-Specific Parameters | Accesses system-specific parameters and functions (e.g., `sys.argv`, `sys.exit()`). |
| `datetime`          | Date and Time Handling     | Used to work with dates and times (`datetime.now()`, formatting, time differences). |
| `random`            | Random Data Generation     | Generates random numbers, shuffles, selects random elements.                        |
| `numpy`             | Numerical Computing        | Fast array operations, linear algebra, Fourier transforms, etc.                     |
| `pandas`            | Data Handling & Analysis   | Powerful data structures like DataFrames for data manipulation and analysis.        |
| `openpyxl`          | Excel File Handling        | Reads and writes Excel `.xlsx` files.                                               |
| `csv`               | CSV File Handling          | Reads and writes data in CSV format using reader/writer objects.                    |
| `matplotlib`        | Data Visualization         | Basic plotting library for line graphs, bar charts, histograms, etc.                |
| `seaborn`           | Statistical Visualization  | Built on top of matplotlib for more attractive and informative statistical plots.   |
| `requests`          | Web Scraping / APIs        | Sends HTTP requests to interact with web pages or APIs.                             |
| `beautifulsoup4`    | Web Scraping               | Parses HTML/XML documents, useful for extracting data from web pages.               |
| `selenium`          | Browser Automation         | Automates web browsers (used for testing or scraping dynamic content).              |
| `sklearn`           | Machine Learning           | Provides simple and efficient tools for data mining and ML algorithms.              |
| `tensorflow`        | Deep Learning              | End-to-end open-source platform for machine learning and neural networks.           |
| `matplotlib.pyplot` | Plotting                   | A part of matplotlib, provides state-based interface for creating visualizations.   |

# Flowchart

    Flowcharts are the visual representations of an algorithm or a process. 
    Flowcharts use symbols/shapes like arrows, rectangles, and diamonds to properly explain the sequence of steps involved in the algorithm or process. 
    Flowcharts have their use cases in various fields such as software development, business process modeling, and engineering.

| **Symbol Name**          | **Symbol**  | **Shape**      | **Usage / Description**                                                     |
| ------------------------ | ----------  | -------------- | --------------------------------------------------------------------------- |
| **Start / End**          | 🟠          | Oval / Ellipse | Marks the beginning or end of a process.                                    |
| **Input / Output**       | ⬛          | Parallelogram  | Used for receiving input or displaying output.                              |
| **Process / Operation**  | 🔲          | Rectangle      | Represents a task, calculation, or action to be performed.                  |
| **Decision / Condition** | ◇           | Diamond        | Indicates a decision point (Yes/No, True/False).                            |
| **Flowline / Arrow**     | ➡️          | Arrow          | Shows the direction or sequence of the steps.                               |
| **Connector (Optional)** | ⚪          | Circle         | Used to connect flow when it continues elsewhere (especially across pages). |

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

<img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/PYTHON/Assets/Functions.jpeg">

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

# Lambda Function

    A lambda function in Python is a small anonymous function (a function without a name) that is defined using the lambda keyword.

    Syntax:

        lambda arguments: expression

    It can have any number of arguments but only one expression.
    The expression is evaluated and returned automatically.
    Typically used for short, simple functions, often as arguments to higher-order functions like map(), filter(), or sorted().

        # A lambda function to add 10 to a number
        
            add_ten = lambda x: x + 10
            print(add_ten(5))  # Output: 15
        
        # A lambda function with two arguments
            
            multiply = lambda x, y: x * y
            print(multiply(3, 4))  # Output: 12

            # Example with sorted()
    
            people = [('Alice', 25), ('Bob', 30), ('Charlie', 20)]
            sorted_people = sorted(people, key=lambda person: person[1])
            print(sorted_people)

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

        1. Positional Arguments:

            Order matters — the values are assigned to parameters based on their position.

            Example:

                def greet(name, age):
                    print(f"Hello {name}, you are {age} years old.")

                greet("Alice", 25)  # name = "Alice", age = 25

        2. Keyword Arguments:

            You specify the parameter name, so order doesn't matter.
            Makes the code more readable and flexible.          

            Example:

                greet(age=25, name="Alice")  # Same output as above

        3. Default Arguments:

            You assign default values to parameters in the function definition.
            If no argument is passed, the default is used.

            Example:

                def greet(name, age=18):
                    print(f"Hello {name}, you are {age} years old.")

                greet("Bob")         # Uses default age = 18
                greet("Alice", 25)   # Overrides default

        4. Variable-Length Arguments :

            These allow a function to accept any number of arguments.

                a. *args (Non-keyword Variable-Length Arguments)

                    Used to pass a variable number of positional arguments.
                    Inside the function, args is a tuple.

                    Example:

                        def total(*numbers):
                            print(sum(numbers))

                        total(10, 20)         # 30
                        total(5, 10, 15, 20)  # 50

                b. **kwargs (Keyword Variable-Length Arguments)

                    Used to pass a variable number of keyword arguments.
                    Inside the function, kwargs is a dictionary.

                    Example:

                        def display_info(**info):
                            for key, value in info.items():
                                print(f"{key}: {value}")

                        display_info(name="Alice", age=25, city="NY")

# Data Types:

    1. Numeric Types:

| Data Type | Description                      | Example        |
| --------- | -------------------------------- | -------------- |
| `int`     | Integer numbers                  | `10`, `-5`     |
| `float`   | Floating point (decimal) numbers | `3.14`, `-2.5` |
| `complex` | Complex numbers (with `j`)       | `3 + 4j`       |
    
    2. Sequence Type:

| Data Type | Description                 | Example              |
| --------- | --------------------------- | -------------------- |
| `str`     | String (text)               | `"hello"`, `'world'` |
| `list`    | Ordered, mutable sequence   | `[1, 2, 3]`          |
| `tuple`   | Ordered, immutable sequence | `(1, 2, 3)`          |
| `range`   | Sequence of numbers         | `range(5)`           |

    3. Set Type:

| Data Type   | Description                       | Example            |
| ----------- | --------------------------------- | ------------------ |
| `set`       | Unordered, mutable, no duplicates | `{1, 2, 3}`        |
| `frozenset` | Unordered, immutable set          | `frozenset({1,2})` |

    4. Mapping Type:

| Data Type | Description     | Example                        |
| --------- | --------------- | ------------------------------ |
| `dict`    | Key-value pairs | `{"name": "Alice", "age": 25}` |

    5. Boolean Type:

| Data Type | Description                   | Example         |
| --------- | ----------------------------- | --------------- |
| `bool`    | Boolean values: True or False | `True`, `False` |

    6. Binary Type:

| Data Type    | Description                 | Example               |
| ------------ | --------------------------- | --------------------- |
| `bytes`      | Immutable sequence of bytes | `b"hello"`            |
| `bytearray`  | Mutable sequence of bytes   | `bytearray([65, 66])` |
| `memoryview` | Memory view object          | `memoryview(b"abc")`  |
   
SUMMARY OF DATA TYPES:

| Category | Types                              |
| -------- | ---------------------------------- |
| Numeric  | `int`, `float`, `complex`          |
| Sequence | `str`, `list`, `tuple`, `range`    |
| Set      | `set`, `frozenset`                 |
| Mapping  | `dict`                             |
| Boolean  | `bool`                             |
| Binary   | `bytes`, `bytearray`, `memoryview` |
| Special  | `NoneType`                         |

# Operators

| **Operator Type** | **Operator(s)**                                  | **Description**                                 | **Example**                 |               |
| ----------------- | ------------------------------------------------ | ----------------------------------------------- | --------------------------- | ------------- |
| **Arithmetic**    | `+`, `-`, `*`, `/`, `//`, `%`, `**`              | Basic math operations                           | `5 + 3 = 8`                 |               |
| **Comparison**    | `==`, `!=`, `>`, `<`, `>=`, `<=`                 | Compare values, returns True/False              | `5 > 3` → `True`            |               |
| **Logical**       | `and`, `or`, `not`                               | Combine boolean expressions                     | `True and False` → `False`  |               |
| **Assignment**    | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=` , `**=` | Assign or update variable values                | `x += 2` means `x = x + 2`  |               |
| **Bitwise**       | `&`, \`                                          | `, `^`, `\~`, `<<`, `>>\`                       | Operate on bits of integers | `5 & 3` → `1` |
| **Membership**    | `in`, `not in`                                   | Check if value is (not) in a sequence           | `'a' in 'cat'` → `True`     |               |
| **Identity**      | `is`, `is not`                                   | Check if two variables refer to the same object | `a is b`                    |               |
