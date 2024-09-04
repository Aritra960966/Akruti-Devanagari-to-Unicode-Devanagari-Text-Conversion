import re
from character_mapping import get_character

def pattern(text):  # Regular pattern operation module.
    return {
        "vowel_signs": re.findall(r'[िीुूेैोौ]', text),
        "halant_placement": re.findall(r'([क-ह])्([क-ह])', text),
        "compound_consonants": re.findall(r'[Ž]', text),
        "nasalization": re.findall(r'ं', text),
        "aspiration": re.findall(r'ः', text),
    }

def substitude_pattern(text):
    character_map = get_character()
    for akruti_char, unicode_char in character_map.items():
        text = re.sub(akruti_char, unicode_char, text)
    return text
