import pandas
data = pandas.read_csv("NATO_alphabet_start/project18.py/nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
word = input("Enter a word: ").upper()
new_data = [new_dict[letter] for letter in word ]
print(new_data)