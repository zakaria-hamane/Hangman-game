import random


def wordChoice():
    return random.choice(['python', 'java', 'kotlin', 'javascript'])


def listToString(l):
    "".join(f'{i}' for i in l)


def resultPrinter(input_letter, word_choice):
    if input_letter not in word_choice:
        print("That letter doesn't appear in the word")


def listOfIndexs(word_choice, input_letter):
    return [index for index, item in enumerate(word_choice) if item == input_letter]


def gridLetterReplacer(empty_grid, list_index, input_letter):
    for index in list_index:
        empty_grid.pop(index)
        empty_grid.insert(index, input_letter)
    return empty_grid


def listToString(empty_grid):
    return "".join(f'{i}' for i in empty_grid)


def gameResult(input_letter, word_choice, empty_grid, list_index):
    empty_grid = gridLetterReplacer(empty_grid, list_index, input_letter)
    return listToString(empty_grid)


def finalResultPrinter(word_choice, result, attempts):
    if result == word_choice:
        print()
        print(result)
        print("You guessed the word!")
        print("You survived!")
        attempts -= attempts
    elif result != word_choice:
        print("You lost!")


def emptyGrid(word_choice):
    return list('-' * len(word_choice))


class RepeatedLetter(Exception):
    pass
class NotEnglishLetter(Exception):
    pass
class NotSingleLetter(Exception):
    pass

def checkPlayerInput(result):
    while True:
        try:
            input_letter = input("Input a letter: ")
            if len(input_letter) != 1:
                raise NotSingleLetter("You should input a single letter")
            if input_letter in result.replace('-', ''):
                raise RepeatedLetter("You've already guessed this letter")
            if input_letter not in "abcdefghijklmnopqrstuvwxyz" or input_letter.isupper():
                raise NotEnglishLetter ("Please enter a lowercase English letter")
            return input_letter

        except RepeatedLetter as RT:
            print(RT)
            print()
            print(result)
        except NotEnglishLetter as NEL:
            print(NEL)
            print()
            print(result)
        except NotSingleLetter as NSL:
            print(NSL)
            print()
            print(result)


def main():
    print("H A N G M A N")
    while True:
        play_game = input('Type "play" to play the game, "exit" to quit: ')
        if play_game == "play":
            global result, input_memory
            input_memory = []
            # word_choice = wordChoice()
            word_choice = 'javascript'
            empty_grid = emptyGrid(word_choice)
            result = listToString(empty_grid)
            
            attempts = 8
            while 0 < attempts <= 8 and "-" in result:
                print()
                print(result)
                input_letter = checkPlayerInput(result)
                if input_letter in input_memory:
                    print("You've already guessed this letter")
                elif input_letter not in word_choice:
                    print("That letter doesn't appear in the word")
                    input_memory.append(input_letter)
                    attempts -= 1
                else:
                    list_index = listOfIndexs(word_choice, input_letter)
                    result = gameResult(input_letter, word_choice, empty_grid, list_index)

            finalResultPrinter(word_choice, result, attempts)
            print()
        else:
            break


if __name__ == "__main__":
    main()
