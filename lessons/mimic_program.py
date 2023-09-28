def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

def mimic_letter(my_words: str, idx: int) -> str:
    """Outputs the character of my_words at index letter _idx"""
    if idx >= len(my_words):
        return "Too high of an index"
    if idx < 0:
        return "Too low of an index"
    return my_words[idx]

x: str = ''' abc '''
print(x)