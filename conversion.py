import os
from character_mapping import get_character
from transformation import transformation
from reg_operations import pattern, substitude_pattern

def convert_akruti_to_unicode(text):
    character_map = get_character()
    converted_text = ""

    for char in text:
        if char in character_map:
            converted_text += character_map[char]
        else:
            converted_text += char

    converted_text = transformation(converted_text)
    
    patterns = pattern(converted_text)  # Ensure patterns function is defined correctly
    converted_text = substitude_pattern(converted_text)

    return converted_text

def process_text_into_folder(folder_path, output_folder):
    """Process text files in the output folder"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create output folder if it does not exist

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                convert_into_single_file(file_path, output_folder)  # Convert file 
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

def convert_into_single_file(file_path, output_folder):
    """Convert into a Single input File and Save the converted output"""
    text = process(file_path)
    if text is not None:
        converted = convert_akruti_to_unicode(text)  # Convert to Unicode
        output_file_path = os.path.join(output_folder, f"converted_{os.path.basename(file_path)}")
        save_output(converted, output_file_path)  # Saving the file

def process(file_path):
    """Reading the text file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Error While Reading the file {file_path}: {str(e)}")
        return None

def save_output(text, output_file_path):
    """Save the Converted Text to an output file with UTF-8 encoding"""
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        print(f"Saved Converted file: {output_file_path}")
    except Exception as e:
        print(f"Error Saving File {output_file_path}: {str(e)}")
