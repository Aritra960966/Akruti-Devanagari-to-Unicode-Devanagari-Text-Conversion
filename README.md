# Akruti Devanagari to Unicode Converter

This Python console application converts Akruti Devanagari script to Unicode Devanagari script, with support for both single file and batch folder conversion. It features real-time conversion and error handling for unsupported characters.

## Features
- **User-Friendly Interface**: The application provides a simple command-line interface to handle text file conversion.
- **Model Integration**: A trained character mapping model for converting Akruti text to Unicode is integrated.
- **Real-Time Conversion**: Users can input text in real-time and see the converted results instantly in the console.
- **Error Handling**: Informative error messages guide the user in case of any invalid input or issues.
- **Batch Processing**: Convert multiple files in a folder at once.

## Directory Structure
├── character_mapping.py       # Character mapping for Akruti to Unicode conversion
├── conversion.py              # Main conversion module
├── transformation.py          # Rules for transformations (e.g., vowel positioning)
├── reg_operations.py          # Regular expression operations for specific patterns
├── main.py                    # Entry point for the console application
├── README.md                  # Documentation for the project
└── example_input               # Example input folder for testing
    ├── sample1.txt
    ├── sample2.txt


##Workflow
Start Application
       |
   User Input (Choose option)
       |
   +--------------------+
   |                    |
Option 1            Option 2
(Import File)      (Convert Folder)
   |                    |
 Read File         Read Files in Folder
   |                    |
 Convert Text       Convert Each File
   |                    |
 Save Output        Save Each Output
   |                    |
   +--------------------+
   |
Option 3 (Real-Time Conversion)
   |
 Enter Text (loop until 'exit')
   |
 Display Converted Text
   |
 Continue or Exit?


## Modules Description
- **character_mapping.py**: Contains the dictionary that maps Akruti characters to Unicode.
- **conversion.py**: Implements the core conversion logic, handling both single file and folder-based conversion.
- **transformation.py**: Provides transformation rules for reordering characters (e.g., placing vowels after consonants).
- **reg_operations.py**: Uses regex to handle specific patterns like compound consonants, halant placement, and nasalization.
- **main.py**: The main script that runs the application and interacts with the user through the command-line interface.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.x
- Git (for version control and uploading to GitHub)
- 

## How to Use

The application supports three modes of operation:

### Option 1: Convert a Single Text File
1. When prompted, choose option `1` to import a single text file.
2. Enter the file path of the text file you wish to convert.
3. Enter the path where you want the converted file to be saved.
4. The file will be converted and saved to the specified output location.

### Option 2: Batch Convert Text Files from a Folder
1. When prompted, choose option `2` to convert multiple text files from a folder.
2. Enter the folder path containing your `.txt` files.
3. Enter the output folder path where the converted files will be saved.
4. All files in the input folder will be converted and saved in the output folder.

### Option 3: Real-Time Conversion
1. Choose option `3` for real-time conversion.
2. Input your Akruti Devanagari text directly into the terminal.
3. The application will convert the input to Unicode Devanagari and display it instantly.
4. Type `exit` to quit real-time conversion mode.




