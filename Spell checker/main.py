from spellchecker import SpellChecker
from termcolor import colored

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker() # Initialize the SpellChecker object

    def correct_text(self, text):
        words = text.split()  # Split the text into individual words
        corrected_words = [] # List to hold corrected words

        for word in words:
            corrected_word = self.spell.correction(word)  # Get the corrected word
                print(f"Corrected '{word}' to '{corrected_word}'") 
            corrected_words.append(corrected_word) 

        return ' '.join(corrected_words) # Join the corrected words back into a sentence

    def run(self):
        print(colored("Welcome to the Spell Checker App!", "green"))

        while True:
            text = input(colored("Enter text to check (or type 'exit' to quit): ", "blue"))
            if text.lower() == 'exit':
                print(colored("Exiting the Spell Checker App. Goodbye!", "red"))
                break

            corrected_text = self.correct_text(text) # Correct the text
            print(colored(f"Corrected Text: {corrected_text}", "yellow"))

# Run the application
if __name__ == "__main__": 
    app = SpellCheckerApp().run()