########################################
# Name: ryland hawkins
# Collaborators (if any): chat gpt
# GenAI Transcript (if any): https://chatgpt.com/share/66fae239-85cc-8008-a63b-202969b37ea0
# Estimated time spent (hr): 4.5
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
from english import *  # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # Function to generate a random five-letter word
    def random_five_letter_word() -> str:
        five_letter_words = [word for word in ENGLISH_WORDS if len(word) == 5]
        print("Available five-letter words:", five_letter_words)  # Debugging to see available words
        return random.choice(five_letter_words).upper()

    # Generate the random answer word
    answr_str = random_five_letter_word()  # Call it after it's defined
    print("Answer Word:", answr_str)  # Debugging to see the word

    def enter_action():
        print("ENTER pressed!")  # Debugging to see if ENTER is working
        current_row = gw.get_current_row()  # Get the current row index
        guess_str = word_from_row(current_row).upper()  # Get the guessed word from the row
        print(f"User guessed: {guess_str}")  # Debugging to see the guess
        
        # Color the guess
        color_row(current_row, guess_str, answr_str)

        # Check if the guess matches the answer
        if guess_str == answr_str:
            gw.show_message("Congratulations! You guessed the word!")
            print("User guessed correctly!")  # Debugging to indicate success
            gw.set_current_row(N_ROWS)  # Stop further input
        else:
            print(f"Guess '{guess_str}' did not match the answer.")  # Debugging incorrect guess
            # Move to the next row
            if current_row + 1 < N_ROWS:
                gw.set_current_row(current_row + 1)
                print(f"Moving to row {current_row + 1}")  # Debugging row change
            else:
                gw.show_message(f"Game over! The word was: {answr_str}")
                print(f"Game over! The word was: {answr_str}")  # Debugging game over message

    def word_from_row(row: int) -> str:
        word = ""
        for col in range(5):
            letter = gw.get_square_letter(row, col)
            print(f"Letter at row {row}, col {col}: {letter}")  # Debugging to see letters
            word += letter
        print(f"Constructed word from row {row}: {word}")  # Debugging constructed word
        return word

    def word_to_row(word: str, row: int):
        print(f"Setting word '{word}' to row {row}")  # Debugging word setting
        for col, letter in enumerate(word):
            gw.set_square_letter(row, col, letter)  # Set each letter in the row
            print(f"Set letter '{letter}' at row {row}, col {col}")  # Debugging each letter set

    def color_row(row: int, guess: str, answer: str):
        print(f"Coloring row {row} for guess '{guess}' against answer '{answer}'")  # Debugging coloring
        answer_list = list(answer)
        guess_list = list(guess)
        correct_markers = [False] * 5  # Track correct (green) letters
        present_markers = [False] * 5  # Track present (yellow) letters
        
        # Step 1: Mark green letters (correct position)
        for i in range(5):
            if guess_list[i] == answer_list[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                gw.set_key_color(guess_list[i], CORRECT_COLOR)
                correct_markers[i] = True
                answer_list[i] = None  # Remove the correct letter from answer list
                print(f"Letter '{guess_list[i]}' is correct at position {i}")  # Debugging correct letters

        # Step 2: Mark yellow letters (present but wrong position)
        for i in range(5):
            if not correct_markers[i]:  # Skip already correctly marked letters
                if guess_list[i] in answer_list:
                    gw.set_square_color(row, i, PRESENT_COLOR)
                    gw.set_key_color(guess_list[i], PRESENT_COLOR)
                    answer_list[answer_list.index(guess_list[i])] = None  # Mark this letter as used
                    present_markers[i] = True  # Mark as present (yellow)
                    print(f"Letter '{guess_list[i]}' is present but in the wrong position")  # Debugging present letters

        # Step 3: Mark gray letters (not present in the answer)
        for i in range(5):
            if not correct_markers[i] and not present_markers[i]:  # Only mark missing letters
                gw.set_square_color(row, i, MISSING_COLOR)
                gw.set_key_color(guess_list[i], MISSING_COLOR)
                print(f"Letter '{guess_list[i]}' is not present in the answer")  # Debugging missing letters

    # Set the first row to be active at the start of the game
    gw.set_current_row(0)
    gw.add_enter_listener(enter_action)  # Add the listener for ENTER
    print("Enter listener added")  # Debugging to confirm listener setup

# Initialize the game window
gw = WordleGWindow()

# Start the game
if __name__ == "__main__":
    wordle()
