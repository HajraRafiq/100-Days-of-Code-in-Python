import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv").to_dict()


#TODO 1. Create a dictionary in this format:
df = pd.DataFrame(data)

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_string = input("Enter a word: ").upper()
phonetic_list = [phonetic_dict[word] for word in phonetic_string]
print(phonetic_list)