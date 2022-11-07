alphabet_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def check_word():
    start_word = input("Enter your word: ").upper()
    if not start_word.isnumeric():
        code_direct = input("Enter code direct (right or left): ").lower()
        if not code_direct.isnumeric() and code_direct == 'left' or code_direct == 'right':
            step_count = input("Enter step count: ")
            if step_count.isnumeric():
                calculation(start_word, code_direct, step_count)
            else:
                print("Incorrect input!")
        else:
            print("Incorrect input!")
    else:
        print("Incorrect input!")


def calculation(start_word, code_direct, step_count):
    end_word = ''
    for char in start_word:
        if char in start_word and code_direct == 'right' and len(alphabet_str) > int(step_count) > 0:
            end_word = end_word + alphabet_str[alphabet_str.index(char) + int(step_count)]
        elif char in start_word and code_direct == 'left' and len(alphabet_str) > int(step_count) > 0:
            end_word = end_word + alphabet_str[alphabet_str.index(char) - int(step_count)]
        else:
            print("This is not a char!! Error! ")
    print("Your word is: " + end_word)


check_word()
