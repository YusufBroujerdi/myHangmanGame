# Documentation Guideline

> The Goal of this project is to create a python script for a basic hangman game.

## Milestone 1

- I downloaded VScode to write my python code. As the industry standard IDE, it provides a wide range of functionality to aid the development of our game, including and not limited to: extensions for linting and colouring code, a debugger, and direct access to the terminal.

- I also downloaded gitbash. In addition to providing a more industry-authentic terminal experience, gitbash also includes git, facilitating more sophisticated version control. I cloned AiCore's Hangman repository to take advantage of the template.

## Milestone 2

- For this milestone, I made headway with the ask_letter method. In addition to asking for user input, basic flow control was implemented to ensure the user input was a single letter. I exploited the ord function to ensure the inputted character is a letter. This is the major code:

```python
    def ask_letter(self):
        while True:
            letter = input('Guess a letter. \n')
            if len(letter) == 1 and ord(letter.lower()) in range(97,123):
                break
            else:
                print("Please, enter just one character")
```

- Below one can see a demonstration of the flow control in the console:

![picture](../pictures/milestone_2.png?raw=true)

- Of course, to commit the code and push it to git hub, the following commands were made use of:

```bash
git status
git add . 
git commit -m "informative commit message"
git push
```

- "git add ." stages all changes in the current directory, "git commit" commits those changes to the current branch. "git status" provides information on staged changes and whatnot. "git push" pushes the code to github. I actually made a separate branch for milestone 2 and merged it into the main branch to emulate the development style Harry outlines in his git video. While this was enlightening, it seemed a little too fiddly for a project of this scale, and I stuck with the main branch for subsequent milestones.

- In the process, I also made frequent use of the following basic terminal commands:

```bash
cd
ls
mv
pwd
cp
rm
```

## Milestone 3

- For this milestone, I initialized the core attributes that would be used for the Hangman class in the __init__ magic method. In order to initialize self.word (a random word to be found for the hangman game), I imported the random package. Its choice function was used to "randomly" choose a word from a list of words. Code below:

```python
    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
```

- Below we can see the messages " The mystery word has {x} characters. " and " ' \_ ', ' \_ ', ' \_ ', ' \_ ' " being printed. This demonstrates the __init__ method running upon instantiation of a Hangman object:

![picture](../pictures/milestone_3.png?raw=true)

## Milestone 4

- This milestone certainly required the most additions. The flow control for ask_letter was modified to ensure the same letter could not be guessed twice. This relied on the list_letters attribute added in milestone 3. Code below:

```python
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
```

- This milestone also involved the creation of the check_letter method. When the letter is in the word, a for loop cycles through the word and replaces a ' _ ' in the word_guessed attribute at each position where the guessed letter appears in the word. If the letter is not in the word, the num_lives attribute is decremented by 1. Code below:

```python
    def check_letter(self, letter):

        if letter.lower() in self.word:
            
            for letter_position in range(len(self.word)):
                
                if self.word[letter_position] == letter.lower():
                    self.word_guessed[letter_position] = letter.lower()
            
            self.num_letters-=1
        
        else:      
            self.num_lives-=1
```

- And here is another screenprint demonstrating the new flow control and the check_letter method in action:

![picture](../pictures/milestone_4.png?raw=true)

## Milestone 5

- This milestone involved the implementation of the play_game function. The play_game function instantiates a Hangman object under the moniker of "game". Then a while loop runs the ask_letter() method and prints the word_guessed attribute for "game" until the loop breaks, either by the num_letters attribute reaching 0 or the num_lives attribute reaching 0. Of course, this function relies on all the previous functionality we built in previous milestones. Code below:

```python
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

```

- Later, I also added a few extra lines to slowly generate a hangman picture as defeat draws nearer. A full game in the code's current state is screencapped below: 

![picture](../pictures/milestone_5.png?raw=true)

## Conclusions


- The most valuable skills I learnt from the project, in my opinion, were writing clean python code, familiarizing myself with git and github, and using the rich functionality of vscode to work more efficiently - particularly the debugger and the linting. I also appreciated learning about the terminal and developing my understanding of how python works.

- To go further, I would have enjoyed giving the user the ability to add and remove words from the list of possible words. Or to allow the user to bypass the random choice and choose a specific word, perhaps for someone else to play the game with.
