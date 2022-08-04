import random


class Hangman:


    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
        self.list_letters = []
        
        print(f'The mystery word has {len(self.word)} characters.')
        print(f'{self.word_guessed}')



    def check_letter(self, letter):

        if letter.lower() in self.word:
            
            for letter_position in range(len(self.word)):
                
                if self.word[letter_position] == letter.lower():
                    self.word_guessed[letter_position] = letter.lower()
            
            self.num_letters-=1
        
        else:      
            self.num_lives-=1



    def ask_letter(self):
        
        while True:         
            letter = input('Guess a letter. \n')
            
            if len(letter) == 1 and ord(letter.lower()) in range(97,123):
                
                if letter.lower() not in self.list_letters:
                    break
                else:
                    print(f'{letter} has already been tried.')
                
            else:
                print('Please, enter just one character')
                
        self.list_letters.append(letter.lower())
        self.check_letter(letter)



def play_game(word_list):

    game = Hangman(word_list, num_lives=5)
    
    while True:
        game.ask_letter()
        print(game.word_guessed)
        
        if game.num_lives == 0:
            print(f'You ran out of lives. The word was {game.word}')
            break
        
        if game.num_letters == 0:
            print(f'Congratulations, you won!')
            break



if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
