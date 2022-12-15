# Coding Challenge 2
# Rohan Shrestha

# A Morse code encoder/decoder

#MORSE_CODE = (
#    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
#    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
#    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
#    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
#    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
#    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
#    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
#    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
#)

#def print_intro():
#    pass


#def get_input():
#    pass


#def encode(message):
#    pass


#def decode(message):
 #   pass

# ---------- Challenge Functions (Optional) ----------


#def process_lines(filename, mode):
#    pass


#def write_lines(lines):
#    pass


#def check_file_exists(filename):
#    pass


#"""
#MAIN DRIVER FUNCTION
#----------------------------------------------------------------------------------------------
#Requirements:
#    • Prompt users to select a mode: encode (e) or decode (d).
#    • Check if the mode the user entered is valid.
#    If not, continue to prompt the user until a valid mode is selected.
#    • Prompt the user for the message they would like to encode/decode.
#   • Encode/decode the message as appropriate and print the output.
#   • Prompt the user whether they would like to encode/decode another message.
#       • Check if the user has entered a valid input (y/n).
#         If not, continue to prompt the user until they enter a valid response.
#         Depending upon the response you should either:
#           • End the program if the user selects no.
#           • Proceed directly to step 2 if the user says yes.
#    • Your program should be as close as possible to the example shown in the assessment specification.

#Hints:
#    • Use the tuple MORSE_CODE above to convert between plain text/Morse code
#   • You can make use of str.split() to generate a list of Morse words and characters
# • You will also find str.join() useful for constructing a string from a list of strings.
#  • You should use a loop to keep the programming running if the user says that would like to
#    encode/decode another message after the first.
  #  • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
  #    and str.lower() to convert a message to that case.
  #  • Check the assessment specification for code examples.
#"""
#def main():
#    pass


# Program execution begins here
#if __name__ == '__main__':
#   main()


#only prints welcome message and goes to 'get_input' function.
def print_intro():
    print('Welcome to Wolmorse')
    print('This program encodes & decodes morse code.')
    get_input()

#takes user input whether to encode or decode, either from console or file.
def get_input():
    morse_code={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
                    'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
                    'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
                    'Y':'-.--','Z':'--.-', ' ': ' ','.':'.-.-.-',
                      '-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5',
                      '-....':'6','--...':'7','---..':'8','----.':'9','-.--.':'(','-.--.-':')',
                      '.-...':'&','---...':':','-.-.-.':';','-...-':'=','.-.-.':'+','-....-':'-',
                      '..--.-':'_','.-..-.':'"','...-..-':'$','.--.-.':'@','..--..':'?','-.-.--':'!',' ':' '}
    #asking the user for input
    #the user wants to encode or decode.                 
    p = str(input("Would you like to encode(e) or decode(d): "))
    #condition if user wants to encode.
    if(p=='e'):
        f_or_c = input("Would you like to read from a file(f) or console(c)? ")
        #if user wants to encode from console.
        if(f_or_c == 'c'):
            message = input("What message would you like to encode: ")   
            encode(message, morse_code)
        #if user wants to encode from file.
        elif(f_or_c == 'f'):
            f = open("morse_input.txt", "r")
            message = []
            for x in f:
                message.append(x)
            listToStr = ''.join([str(elem) for elem in message])
            encode(listToStr, morse_code)
        #in case of invalid input.
        else:
            print('Invalid Input!')
            get_input()
    #condition if user wants to decode.
    elif(p == 'd'):
        f_or_c = input("Would you like to read from a file(f) or console(c)? ")
        #if user wants to decode from console.
        if(f_or_c == 'c'):
            message = input("What message would you like to decode: ")   
            message = Convert(message)
            decode(message, morse_code)
        #if user wants to decode from file.
        elif(f_or_c == 'f'):
            f = open("filemorse_input.txt", "r")
            message = []
            for x in f:
                message.append(x)
            listToStr = ' '.join([str(elem) for elem in message])
            message = Convert(listToStr)
            decode(message, morse_code) 
    #in case of invalid input.
    else:
        print("Invalid Input!")
        get_input()

#function to encode any message that is sent as parameter, second parater is the dictionary of morse codes.
def encode(message, codes):
    message = message.upper()
    for x in range(0, len(message)):
        print(codes[message[x]], end=' ')#ends a string character with a space which helps to read a string seperately. 
    confirmRerun()

#function to decode any message that is sent as paramter, second parater is the dictionary of morse codes.
def decode(message, codes):
    for code in message:
        print(get_key(code, codes), end='')
    confirmRerun()
       
#function to ask the users if they want to re-run the program.
def confirmRerun():
    confirm = input("\nWould you like to encode/decode another message? (y/n)")
    if(confirm =='y'):
        get_input()
    elif(confirm=='n'):
        print("\nThanks for using this program!\nGood Bye!")
    else:
        print("Invalid Input!")
        confirmRerun()

#function to get the key of a certain value.
def get_key(val, codes):
    for key, value in codes.items():
         if val == value:
             return key
    return " "

#function to split a string in case they have spaces in between.
def Convert(string):
    li = list(string.split(" "))
    return li

#entry point of the program.      
print_intro()
