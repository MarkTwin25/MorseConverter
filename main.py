import argparse

letter_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
    }

morse_to_text = {value:key for key,value in letter_to_morse.items()}

def convert_morse(text:str):
    new_s = ""
    for i in range(len(text)):
        if i == len(text)-1:
            new_s += letter_to_morse.get(text[i].upper(),"?")
            continue

        if text[i] != " ":
            new_s += letter_to_morse.get(text[i].upper(),"?") + " "
    return new_s

def convert_text(morse:str):
    new_s = ""
    morse = morse.split(" ")
    for i in range(len(morse)):
        if morse[i] not in morse_to_text:
            print("This is not a valid morse code")
            print("Please, Each letter in Morse must be separated by a space")
            break
        if morse[i] != " ":
            new_s += morse_to_text.get(morse[i],"?")
    return new_s

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text to Morse Code converter')
    parser.add_argument('-M', '--mode', type=str, choices=['text_to_morse', 'morse_to_text'],
                        help='text in some lenguage/Morse code')
    parser.add_argument("-V", "--value", type=str, help="Your text to convert")

    args = parser.parse_args()
    if args.mode == "text_to_morse":
        print(convert_morse(args.value))
    elif args.mode == "morse_to_text":
        print(convert_text(args.value))
    else:
        print(parser.print_help())