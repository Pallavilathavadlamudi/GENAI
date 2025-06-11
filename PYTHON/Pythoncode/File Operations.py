#File Operations for .txt files 

# Opening a file in write mode

with open("File Operations.txt","w") as file:
    file.write("This is a test file. \n")
    file.write("This file is used to demonstrate file operations in python. \n")

    #opening the file in read mode
with open ("File Operations.txt","r") as file:
    content = file.read()
    print("Output:1")
    print(content)

    #Opening the file in append mode
with open("File Operations.txt","a") as file:
        file.write("This is an appended line. \n")
    
    #Reading the file again to see the appended content
with open("File Operations.txt","r") as file:
        content = file.read()
        print("Output:2")
        print(content)
    
    # Writing to a binary file
with open("Binary File Operations.txt","wb") as file:
    file.write(b"This is a binary file. \n")
    file.write(b"This file is used to demonstrate binary file operations in python. \n")

    #Reading the binary file again to see the content
with open("Binary File Operations.txt", "rb") as file:
    binary_content = file.read()
    print("Output:4")
    print(binary_content)

    # Appending to a binary file
with open("Binary File Operations.txt", "ab") as file:
    file.write(b"This is an appened line in binary file. \n")

    #Raeding the binary file again to see the appended content
with open("Binary File Operations.txt", "rb") as file:
    binary_coontent=file.read()
    print("Output:5")
    print(binary_content)
 
    #Reading a file line by line
with open("File Operations.txt","r") as file:
    for line in file:
        print("Output:6")
        print(line.strip()) # Using strip() to remove newline characters

# Reading a file line by line
with open("File Operations.txt","r") as file:
    for line in file:
        print("Output:7")
        print(line) 





