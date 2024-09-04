import re

def transformation(text):
    text = re.sub(r'([ि])([क-ह])', r'\2\1', text)  
    # Rule for vowel sign that precedes consonants.

    compound_consonants = {
        "Ž": "क्ष",
        "": "त्र",
        "": "ज्ञ"
    }
    for akruti_char, unicode_char in compound_consonants.items():
        text = text.replace(akruti_char, unicode_char)
    
    text = re.sub(r'([क-ह])्([क-ह])', r'\1्\2', text)  # Handle halant character
    nasalization_aspiration = {
        "´": "ं",
        "µ": "ः"
    }
    for akruti_char, unicode_char in nasalization_aspiration.items():
        text = text.replace(akruti_char, unicode_char)

    return text
