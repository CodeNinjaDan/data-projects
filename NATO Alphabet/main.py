import pandas

#Read the CSV file into DataFrame
words_file = pandas.read_csv("nato_phonetic_alphabet.csv")

#{key_expression: value_expression for item in iterable if condition}

words_dict = {row.letter:row.code for (index, row) in words_file.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        nato_codes = [words_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only words in the alphabet please.")
        generate_phonetic()

    else:
        print(nato_codes)

generate_phonetic()


