import json
import difflib

#get access to whole data in the json file
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

#with the help of difflib, try to collect misspelling by suggesting words closer to the one typed
def suggest_word(word, dictionary):
    word = word.lower()
    suggestions = difflib.get_close_matches(word, dictionary.keys(), n=1, cutoff=0.8)
    if suggestions:
        return suggestions[0]
    return None

#find whether the word resides in the dictionary or not
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        #get the meaning, the key is the word
        return dictionary[word]
    else:
        suggestion = suggest_word(word, dictionary)
        if suggestion:
            return f"Did you mean '{suggestion}'? Here's the definition: {dictionary[suggestion]}"
        else:
            return "The word doesn't exist in the dictionary."

#main function
def main():
    dictionary = load_data('data.json')
    
    #allow user to prompt the system for definition
    while True:
        word = input("Enter a word to find its definition (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        else:
            definition = get_definition(word, dictionary)
            print(definition)

if __name__ == "__main__":
    main()
