import os
from conversion import convert_akruti_to_unicode, process_text_into_folder

def get_input():
    """Prompt user for input choice."""
    print("\nChoose an Option: ")
    print("1: Import Text File")
    print("2: Convert Text From a Folder")
    print("3: Real-Time Conversion")
    return input("Enter Your Choice (1, 2 or 3): ")

def real_time_conversion():
    """Handle real-time conversion from user input."""
    print("Enter text to convert (type 'exit' to quit):")
    while True:
        input_text = input("Input: ")
        if input_text.lower() == 'exit':
            break
        
        converted_text = convert_akruti_to_unicode(input_text)
        print(f"Converted: {converted_text}\n") 

def convert_into_single_file(file_path, output_folder):
    """Convert a single input file and save the converted output."""
    text = process(file_path)  
    if text is not None:
        converted = convert_akruti_to_unicode(text)  
        output_file_path = os.path.join(output_folder, f"converted_{os.path.basename(file_path)}")
        save_output(converted, output_file_path) 

def save_output(text, output_file_path):
    """Save the Converted Text to an output file with UTF-8 encoding."""
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        print(f"Saved Converted file: {output_file_path}")
    except Exception as e:
        print(f"Error Saving File {output_file_path}: {str(e)}")

def process(file_path):
    """Read the text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Error While Reading the file {file_path}: {str(e)}")
        return None

def main():
    while True:
        choice = get_input()
        if choice == '1':
            file_path = input("Enter the Path of the Text File: ")
            output_folder = input("Enter The Output Folder Path: ")
            if os.path.isfile(file_path):
                convert_into_single_file(file_path, output_folder)
            else:
                print("Invalid file path. Please try again.")

        elif choice == '2':
            folder_path = input("Enter the Path of the Folder: ")
            output_folder = input("Enter The Output Folder Path: ")
            if os.path.isdir(folder_path):
                process_text_into_folder(folder_path, output_folder)
            else:
                print("Invalid folder path. Please try again.")

        elif choice == '3':
            real_time_conversion()  # Call the real-time conversion function

        else:
            print("Invalid Choice, Please Reenter")  # Clear message for invalid input
        
        continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()  
