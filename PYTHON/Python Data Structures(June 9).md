# Data Structures

1. What is Data Structure?

        A data structure is a way to store and organize data so that it can be accessed and modified efficiently.

        Python provides several built-in data structures, each suited for different types of tasks.

    Built-in Data Structures in Python:

    1. List: List is a collection which is ordered and changeable. Allows duplicate members.  
    2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    4. Dictionary is a collection which is ordered** and changeable. No duplicate members. 

# Built-in Data Types:

1. List:

    List items are ordered, changeable, and allow duplicate values.
    List items are indexed, the first item has index [0], the second item has index [1] etc.

|      Feature            |                Description                 |
| ----------------------- | ------------------------------------------ |
|      Ordered            | Items maintain the order you add them      |
|      Mutable            | You can change, add, remove items          |
|      Indexed            | Access items by position (starting from 0) |
|   Allows duplicates     | Same value can appear multiple times       |

        Example:

            my_list = [item1, item2, item3, ...]


2. Tuple: 

    Tuples are used to store multiple items in a single variable.
    A tuple is a collection which is ordered and unchangeable.

| Feature           | Description                                               |
| ----------------- | --------------------------------------------------------- |
| Ordered           | Items maintain the order you add them                     |
| Immutable         | Once created, you **cannot** change, add, or remove items |
| Indexed           | Access items by position (starting from 0)                |
| Allows duplicates | Same value can appear multiple times                      |

        Example:

            thistuple = ("apple", "banana", "cherry")
            print(thistuple)

3. Set: 

    Sets are used to store multiple items in a single variable.
    A set is a collection which is unordered, unchangeable, and unindexed.

| Feature       | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| Unordered     | Items do **not** maintain any specific order                       |
| Mutable       | You can add or remove items after creation                         |
| Not Indexed   | You **cannot** access items by position (no indexing)              |
| No duplicates | Only unique items are stored; duplicates are automatically removed |

        Example:

            thisset = {"apple", "banana", "cherry", "apple"}
            print(thisset)

4. Dictionary:

    Dictionaries are used to store data values in key:value pairs.
    A dictionary is a collection which is ordered, changeable and do not allow duplicates.

| Feature           | Description                                            |
| ----------------- | ------------------------------------------------------ |
| Ordered\*         | Items maintain insertion order (Python 3.6+ and later) |
| Mutable           | You can add, change, or remove key-value pairs         |
| Not Indexed       | Access is by **keys**, not by position                 |
| No duplicate keys | Keys must be unique; values can be duplicated          |

    Before Python 3.6, dictionaries were unordered.

    Example:

        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }
        print(thisdict)