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
| Ordered           | Items maintain insertion order (Python 3.6+ and later) |
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

# Operations

1. List Operations :

    * Access: Retrieve items by their index.
    * Add: Insert new items using append, insert, or extend.
    * Modify: Change the value of an item at a specific index.
    * Remove: Delete items using remove, pop, or del.
    * Search: Check if an item exists or find its position.
    * Sort: Arrange items in ascending or descending order.
    * Reverse: Reverse the order of items.
    * Length: Get the number of items in the list.
    * Iterate: Loop through all items one by one.

| Operation    | Method/Statement                   | Description                    |
| ------------ | ---------------------------------- | ------------------------------ |
| Add item     | `append()`, `insert()`, `extend()` | Add elements to list           |
| Modify item  | `list[index] = value`              | Change value at index          |
| Remove item  | `remove()`, `pop()`, `del`         | Remove elements                |
| Access item  | `list[index]`                      | Get element by index           |
| Search item  | `in`, `index()`                    | Check existence, find position |
| Sort list    | `sort()`, `sorted()`               | Arrange items                  |
| Reverse list | `reverse()`                        | Reverse order                  |
| Length       | `len()`                            | Get number of items            |
| Iterate      | `for item in list`                 | Loop through items             |

2. Tuple Operations:

    * Add item: Not possible (tuples are immutable).
    * Modify item: Not possible (tuples are immutable).
    * Remove item: Not possible (tuples are immutable).
    * Access item: Retrieve items by their index.
    * Search item: Check if an item exists or find its position.
    * Sort: Not possible directly (tuples are immutable), but you can convert to a list to sort.
    * Reverse: Not possible directly, but can create a reversed tuple.
    * Length: Get the number of items in the tuple.
    * Iterate: Loop through all items one by one.

| Operation     | Method/Statement                 | Description                             |
| ------------- | -------------------------------- | --------------------------------------- |
| Access item   | `tuple[index]`                   | Get element by index                    |
| Search item   | `in`, `tuple.index()`            | Check existence, find position          |
| Sort tuple    | Use `sorted(tuple)`              | Returns a sorted list (tuple unchanged) |
| Reverse tuple | Use `reversed(tuple)` or slicing | Returns reversed iterator or new tuple  |
| Length        | `len(tuple)`                     | Get number of items                     |
| Iterate       | `for item in tuple`              | Loop through items                      |


3. Set Operations:

    * Add item: Add elements to the set.
    * Remove item: Remove elements from the set.
    * Access item: Not by index (sets are unordered).
    * Search item: Check if an element exists in the set.
    * Union: Combine two sets.
    * Intersection: Get common elements between sets.
    * Difference: Get elements in one set but not the other.
    * Symmetric Difference: Elements in either set but not both.
    * Length: Get number of elements.
    * Iterate: Loop through all items.

| Operation            | Method/Statement                                   | Description                                           |                                 |
| -------------------- | -------------------------------------------------- | ----------------------------------------------------- | ------------------------------- |
| Add item             | `add(item)`                                        | Add an element to the set                             |                                 |
| Remove item          | `remove(item)`, `discard(item)`                    | Remove an element (discard does not error if missing) |                                 |
| Clear set            | `clear()`                                          | Remove all elements                                   |                                 |
| Search item          | `in`                                               | Check if an element exists                            |                                 |
| Union                | `set1.union(set2)` or \`set1                       | set2\`                                                | Combine elements from both sets |
| Intersection         | `set1.intersection(set2)` or `set1 & set2`         | Get common elements                                   |                                 |
| Difference           | `set1.difference(set2)` or `set1 - set2`           | Elements in set1 not in set2                          |                                 |
| Symmetric Difference | `set1.symmetric_difference(set2)` or `set1 ^ set2` | Elements in either set, but not both                  |                                 |
| Length               | `len(set)`                                         | Get number of elements                                |                                 |
| Iterate              | `for item in set`                                  | Loop through elements                                 |                                 |

4. Dictionary: 

    * Add item: Insert a new key-value pair.
    * Modify item: Change the value of an existing key.
    * Remove item: Delete a key-value pair.
    * Access item: Retrieve value by key.
    * Search item: Check if a key exists.
    * Keys, Values, Items: Get lists of keys, values, or key-value pairs.
    * Clear: Remove all key-value pairs.
    * Length: Get number of key-value pairs.
    * Iterate: Loop through keys, values, or items.

| Operation        | Method/Statement                                    | Description                          |
| ---------------- | --------------------------------------------------- | ------------------------------------ |
| Add item         | `dict[key] = value`                                 | Add or update key-value pair         |
| Modify item      | `dict[key] = new_value`                             | Change value for existing key        |
| Remove item      | `del dict[key]`, `pop(key)`                         | Delete key-value pair                |
| Access item      | `dict[key]`                                         | Retrieve value by key                |
| Search item      | `key in dict`                                       | Check if key exists                  |
| Get keys         | `dict.keys()`                                       | Return all keys                      |
| Get values       | `dict.values()`                                     | Return all values                    |
| Get items        | `dict.items()`                                      | Return all key-value pairs as tuples |
| Clear dictionary | `dict.clear()`                                      | Remove all key-value pairs           |
| Length           | `len(dict)`                                         | Number of key-value pairs            |
| Iterate          | `for key in dict` or `for key, val in dict.items()` | Loop through dictionary              |


