student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

alphabet = pd.read_csv("nato_phonetic_alphabet.csv",header=None, names=['letter', 'code'])

alphabet_dictionary = dict(zip(alphabet['letter'], alphabet['code']))
print(alphabet_dictionary)

word = input("Enter a word: ").upper()

word_list = [letter for letter in word]
print(word_list)

word_dict = [alphabet_dictionary[letter] for letter in word_list if letter in alphabet_dictionary.keys()]
print(word_dict)
