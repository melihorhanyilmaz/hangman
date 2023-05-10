from typing import List
import random

class Hangman():
    possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions', 'algorithm', 'software', 'python', 'thread', 'scrapy']
    def __init__(self) -> None:
        # list the letters of the word
        self.word_to_find: str = list(random.choice(self.possible_words)) 
        self.lives: int = 5
        # number of letters -> '_'
        self.correctly_guessed_letters: List[str] = ['_' for _ in range(len(self.word_to_find))] 
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def play(self):
        """
        This function asks the player to enter a letter. Be careful that the player shouldn't be allowed to type something 
        else than a letter, and not more than a letter. If the player guessed a letter well, add it to the `correctly_guessed_letters` 
        list. If not, add it to the `wrongly_guessed_letters` list and add 1 to `error_count`.
        """
        while self.lives > 0:
            letter: str = input(str("Please enter a single letter: ")).lower()
            print("*****************************")
            # if-else conditions ensures that alphabet and single character
            if len(letter) == 1 and letter.isalpha(): 
                if letter in self.correctly_guessed_letters or letter in self.wrongly_guessed_letters:
                    print("You already guessed the letter", letter)
                elif letter not in self.word_to_find:
                    print(letter, "is not in the word")
                    self.lives -= 1
                    self.wrongly_guessed_letters.append(letter)
                    self.error_count += 1
                    break
                else:
                    print("Yesss, '" + letter + "' is in the word")
                    # Place the letters according to the index in the word when you find the letter.
                    for i, char in enumerate(self.word_to_find):
                        if char == letter:
                            self.correctly_guessed_letters[i] = letter
                    break
            else:
                print("Invalid input, please enter a single letter.")
                return
            
        self.turn_count += 1
        
    def start_game(self):
        """
        Function that will call different functions until the game is over.
        :will call `play()` until the game is over (because the use guessed the word or because of a game over).
        :will call `game_over()` if `lives` is equal to 0.
        :will call `well_played()` if all the letter are guessed.
        :will print `correctly_guessed_letters`, `bad_guessed_letters`, `life`, `error_count` and `turn_count` at the end of each turn.
        """
        while True:
            print("".join(self.correctly_guessed_letters).upper())
            print("Wrong letters: " + ", ".join(self.wrongly_guessed_letters))
            print(f"Lives: {self.lives}, Errors: {self.error_count}, Turns: {self.turn_count}")
            self.play()
            if self.lives == 0:
                self.game_over()
                break

            elif "_" not in self.correctly_guessed_letters: # '_' ends when player knows all letters
                self.well_played()
                break

    def game_over(self):
        """
        Function that will stop the game and print `game over...`.
        """
        print("************")
        print("GAME OVER...")
        print("************")

    def well_played(self):
        """
        Function that will stop the game and print `You found the word: {word_to_find_here} in {turn_count_here} turns 
        with {error_count_here} errors!`.
        """
        word = "".join(self.word_to_find)
        print("************")
        print(f"You found the word: '{word.upper()}' in {self.turn_count} turns with {self.error_count} errors!")
        print("************")

while True:
    hangman = Hangman()
    hangman.start_game()
    response = input("Play Again? (Y/N) : ")
    if response.upper() == "Y":
        continue
    else:
        print("\nSee you later :)")
        break