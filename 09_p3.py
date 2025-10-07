# File I/O

# File I/O in Python: Notes on Reading, Writing, and Managing Files

# 1. INTRODUCTION
# File I/O (Input/Output) in Python allows reading from and writing to files.
# Files can be text (e.g., .txt, .csv) or binary (e.g., .jpg, .dat).
# Python provides built-in functions like open(), read(), write(), and close() for file operations.

# 2. OPENING A FILE
# Use open() to open a file. Syntax: open(filename, mode, encoding=None)
# - filename: Path to the file (e.g., 'example.txt' or 'path/to/file.txt').
# - mode: Specifies the mode of operation (read, write, append, etc.).
# - encoding: Specifies the file encoding (e.g., 'utf-8' for text files).

# Common file modes:
# - 'r'  : Read (default mode). Opens file for reading, raises error if file doesn't exist.
# - 'w'  : Write. Creates a new file or overwrites an existing file.
# - 'a'  : Append. Opens file for appending, creates file if it doesn't exist.
# - 'r+' : Read and write. File must exist, allows both reading and writing.
# - 'b'  : Binary mode (e.g., 'rb', 'wb'). Used for non-text files like images.
# - 't'  : Text mode (default, e.g., 'rt'). Used for text files.

# Example: Opening a file
# file = open('example.txt', 'r', encoding='utf-8')  # Opens file for reading

# 3. READING FROM A FILE
# After opening in read mode ('r'), use methods to read content:
# - read(): Reads the entire file as a single string.
# - readline(): Reads one line at a time (returns empty string at end of file).
# - readlines(): Reads all lines into a list, each line as a string.
# - for loop: Iterate over file object to read lines efficiently.

# Example: Reading a file
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()           # Reads entire file
#     line = file.readline()          # Reads one line
#     lines = file.readlines()        # Reads all lines into a list
#     for line in file:               # Iterates through lines
#         print(line.strip())         # strip() removes trailing newlines

# 4. WRITING TO A FILE
# Use 'w' mode to write (overwrites file) or 'a' mode to append.
# - write(str): Writes a string to the file.
# - writelines(lines): Writes a list of strings to the file (no automatic newlines).

# Example: Writing to a file
# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write('Hello, World!\n')   # Write a string
#     file.writelines(['Line 1\n', 'Line 2\n'])  # Write multiple lines

# Example: Appending to a file
# with open('output.txt', 'a', encoding='utf-8') as file:
#     file.write('Appended text\n')   # Adds text to the end of the file

# 5. USING THE 'with' STATEMENT
# The 'with' statement is a context manager that ensures proper file handling.
# - Automatically closes the file after operations, even if an error occurs.
# - Eliminates the need to call file.close() manually.
# - Preferred method for file I/O to avoid resource leaks.

# Example: Using 'with' for file operations
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()  # File is automatically closed after this block

# 6. CLOSING A FILE
# If not using 'with', manually close the file using close().
# - Ensures resources are freed and changes are saved.
# - Failing to close a file can lead to data loss or resource leaks.

# Example: Manual file closing
# file = open('example.txt', 'r', encoding='utf-8')
# content = file.read()
# file.close()  # Always close the file when done

# 7. ERROR HANDLING
# File operations can raise exceptions (e.g., FileNotFoundError, IOError).
# Use try-except blocks to handle errors gracefully.

# Example: Handling file-related errors
# try:
#     with open('nonexistent.txt', 'r', encoding='utf-8') as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Error: File not found.")
# except IOError:
#     print("Error: An I/O error occurred.")
# except Exception as e:
#     print(f"Unexpected error: {e}")

# 8. FILE POSITION AND SEEKING
# Files have a cursor (position) that tracks where reading/writing occurs.
# - tell(): Returns the current position of the cursor (in bytes).
# - seek(offset, whence): Moves the cursor to a specific position.
#   - offset: Number of bytes to move.
#   - whence: Reference point (0 = start of file, 1 = current position, 2 = end of file).

# Example: Using seek() and tell()
# with open('example.txt', 'r', encoding='utf-8') as file:
#     print(file.tell())         # Current position (starts at 0)
#     file.seek(10)              # Move cursor to byte 10
#     print(file.read())         # Read from byte 10 onward

# 9. WORKING WITH BINARY FILES
# Use 'b' mode for binary files (e.g., images, videos).
# Data is read/written as bytes, not strings.

# Example: Reading and writing a binary file
# with open('image.jpg', 'rb') as source:
#     data = source.read()  # Read binary data
# with open('copy.jpg', 'wb') as destination:
#     destination.write(data)  # Write binary data

# 10. FILE ENCODING
# For text files, specify encoding (e.g., 'utf-8', 'ascii') to handle special characters.
# Omitting encoding may cause errors with non-ASCII text.

# Example: Specifying encoding
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()

# 11. CHECKING FILE PROPERTIES
# Use os module to check file existence, size, or other properties.
# import os
# - os.path.exists(filename): Checks if file exists.
# - os.path.isfile(filename): Checks if path is a file.
# - os.path.getsize(filename): Returns file size in bytes.

# Example: Checking file properties
# import os
# if os.path.exists('example.txt'):
#     print(f"File exists, size: {os.path.getsize('example.txt')} bytes")
# else:
#     print("File does not exist.")

# 12. DELETING OR RENAMING FILES
# Use os module for file management.
# - os.remove(filename): Deletes a file.
# - os.rename(old_name, new_name): Renames a file.

# Example: Deleting and renaming files
# import os
# os.remove('example.txt')  # Deletes the file
# os.rename('old.txt', 'new.txt')  # Renames the file

# 13. WORKING WITH CSV FILES
# Use csv module for reading/writing CSV files.
# import csv
# Example: Reading a CSV file
# with open('data.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)  # Each row is a list of values
# Example: Writing to a CSV file
# with open('data.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Age'])  # Write a row
#     writer.writerows([['Alice', 25], ['Bob', 30]])  # Write multiple rows

# 14. WORKING WITH JSON FILES
# Use json module for reading/writing JSON files.
# import json
# Example: Writing to a JSON file
# data = {'name': 'Alice', 'age': 25}
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file)  # Write dictionary to JSON file
# Example: Reading from a JSON file
# with open('data.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)  # Load JSON into dictionary

# 15. BEST PRACTICES
# - Always use 'with' statement to ensure files are properly closed.
# - Specify encoding for text files to avoid encoding issues.
# - Handle exceptions to make your code robust.
# - Use appropriate file modes ('r', 'w', 'a', 'rb', 'wb') based on the task.
# - For large files, read line by line (using readline() or for loop) to save memory.
# - Close files explicitly if not using 'with' to free resources.

# 16. EXAMPLE: COMPLETE FILE I/O WORKFLOW
# try:
#     # Writing to a file
#     with open('example.txt', 'w', encoding='utf-8') as file:
#         file.write('Hello, Python!\n')
#         file.write('This is a test file.\n')
#
#     # Reading from the file
#     with open('example.txt', 'r', encoding='utf-8') as file:
#         content = file.read()
#         print("File content:")
#         print(content)
#
#     # Appending to the file
#     with open('example.txt', 'a', encoding='utf-8') as file:
#         file.write('Appended line.\n')
#
# except FileNotFoundError:
#     print("Error: File not found.")
# except IOError:
#     print("Error: An I/O error occurred.")
# except Exception as e:
#     print(f"Unexpected error: {e}")

# End of File I/O Notes