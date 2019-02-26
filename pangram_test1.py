from string import ascii_lowercase as ascii

def is_pangram(sentence):
    return all(char in sentence.lower() for char in ascii)
