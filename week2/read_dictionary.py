from string import ascii_lowercase

def read_dictionary(filename, length):
    words = []
    for word in open(filename):
        word = word.strip()
        if len(word) == length:
            if word.islower() & word.isalpha():
                if word not in words:
                    words.append(word)
    return words