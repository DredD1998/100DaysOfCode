import pandas
data = pandas.read_csv("NATO_alphabet_start/project18.py/nato_phonetic_alphabet.csv")

new_dict = {value.letter:value.code for (key,value) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        new_data = [new_dict[letter] for letter in word ]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_data)

generate_phonetic()