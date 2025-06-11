# File Handling

    File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and closing it, through a programming interface. 

    It involves managing the data flow between the program and the file system on the storage device

| **Mode** | **Description**                       | **Behavior**                                                                                    |
| -------- | ------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `r`      | Read-only mode                        | Opens the file for reading. File **must exist**; otherwise, raises an error.                    |
| `rb`     | Read-only in binary mode              | Opens the file for reading **binary** data. File must exist.                                    |
| `r+`     | Read and write mode                   | Opens the file for **both reading and writing**. File must exist.                               |
| `rb+`    | Read and write in binary mode         | Opens the file for **both reading and writing binary** data. File must exist.                   |
| `w`      | Write mode                            | Opens the file for writing. **Creates a new file** or **truncates** the existing one.           |
| `wb`     | Write in binary mode                  | Opens the file for writing **binary** data. Creates or truncates file.                          |
| `w+`     | Write and read mode                   | Opens the file for **writing and reading**. Creates or truncates file.                          |
| `wb+`    | Write and read in binary mode         | Opens the file for **writing and reading binary** data. Creates or truncates file.              |
| `a`      | Append mode                           | Opens the file for **appending**. Creates new file if it doesn’t exist.                         |
| `ab`     | Append in binary mode                 | Opens the file for **appending binary** data. Creates new file if it doesn’t exist.             |
| `a+`     | Append and read mode                  | Opens the file for **appending and reading**. Creates new file if it doesn’t exist.             |
| `ab+`    | Append and read in binary mode        | Opens the file for **appending and reading binary** data. Creates new file if it doesn’t exist. |
| `x`      | Exclusive creation mode               | **Creates a new file**. Raises error if file already exists.                                    |
| `xb`     | Exclusive creation in binary mode     | Creates new **binary** file. Raises error if file exists.                                       |
| `x+`     | Exclusive creation with read/write    | Creates new file for **reading and writing**. Error if file exists.                             |
| `xb+`    | Exclusive creation in binary with r/w | Creates new **binary** file for reading and writing. Error if file exists.                      |

