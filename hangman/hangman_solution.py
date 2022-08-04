'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
        self.list_letters = []
        
        print(f"The mystery word has {len(self.word)} characters.")
        print(f"{self.word_guessed}")



    def check_letter(self, letter):

        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        if letter.lower() in self.word:
            
            for letter_position in range(len(self.word)):
                
                if self.word[letter_position] == letter.lower():
                    self.word_guessed[letter_position] = letter.lower()
            
            self.num_letters-=1
        
        else:      
            self.num_lives-=1
           
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A word can contain the same letter more than once. TIP: Take a look at the index() method in the string class



    def ask_letter(self):
        
        while True:         
            letter = input('Guess a letter. \n')
            
            if len(letter) == 1 and ord(letter.lower()) in range(97,123):
                
                if letter.lower() not in self.list_letters:
                    break
                else:
                    print(f"{letter} has already been tried.")
                
            else:
                print("Please, enter just one character")

        self.check_letter(letter)



def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"



if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
