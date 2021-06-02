# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  ╔═╗╦═╗╦ ╦╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔╦╗                       #
#  ║  ╠╦╝╚╦╝╠═╝ ║ ║ ║║ ╦╠╦╝╠═╣║║║                       #
#  ╚═╝╩╚═ ╩ ╩   ╩ ╚═╝╚═╝╩╚═╩ ╩╩ ╩                       #
#  ╔═╗╔═╗╦ ╦  ╦╔═╗╦═╗                                   #
#  ╚═╗║ ║║ ╚╗╔╝║╣ ╠╦╝                                   #
#  ╚═╝╚═╝╩═╝╚╝ ╚═╝╩╚═                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                       #
# Licensed under the GNU GENERAL PUBLIC LICENSE v3.0    #
#                                                       #
# 29 May 2021                                           #
#                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# APPROACH:
#
# 1. ACCEPT THE CIPHER (VHB) (DONE – TESTING NEEDED)
# 2. ACCEPT THE CLUE (VHB)
# 3. DUPLICATE THE CIPHER (VHB)
# 4. PARSE THE CIPHER AT SPACES OR PUNCTUATION INTO AN ARRAY (SS)
# 5. ORDER ARRAY ELEMENTS BY LENGTH (SS)
# 6. COMPARE ORIGINAL ARRAY AND ORDERED ARRAY AND BUILD A DICTIONARY TO REMEMBER ORIGINAL ORDERING (SPK)
# 7. DUPLICATE THE ARRAY (S)
# 8. SUBSTITUTE THE CLUE INTO ALL ARRAY ELEMENTS (S)
# Here on: protect the substituted letter from step 8
# 9(a). COMPARE WITH DICTIONARY TO FIND WORD MATCHES IN ASCENSION OF ELEMENT LENGTH (ARATHI)
# 9(b). RESTART AT ARRAY 0 FOR EVERY FAILED MATCH ENCOUNTERED (ARATHI)
# 10. ONCE ALL ARRAY ELEMENTS HAVE BEEN MATCHED COMPARE ELEMENTS TO THE DICTIONARY AND RE-ORDER ARRAY (SKK)
# 11. CONCATENATE ARRAY INTO A PROPER SENTENCE (SKK)
#
# ISSUES are to be handled on Github.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# IMPORTS
import re  # RegEx to make sure the user entered a cryptogram

# GLOBAL VARIABLES
cipher: str  # Declaring a string but not giving it a value
# Prepping two variables for key and value e.g. h=b where h is the key and b is the value
clue_key: str  # Declaring a string but not giving it a value (see comment in the next line)
clue_value: str  # Python doesn't have char type: a char is a string of length 1


def cipher_acceptor():
    # The line below tells Python we're going to use the same
    # global variable called cipher and that we are not creating
    # a new function-specific one also called cipher
    global cipher
    # Get an input from the user
    cipher = input("Enter the cipher:\n")
    # Make sure the user does not want to not quitting, and quit if a cipher is not entered
    if not (cipher == 'X' or cipher == 'x' or cipher is None or cipher == ''):
        # Check if input follows RegEx for a typical cryptoquip
        if not re.search(r'^(?!.*/)(?!.*\\)(?!.*_)[a-zA-Z\s\D.,\-\'\"?!]+$', cipher):
            # If it does not follow RegEx inform the user and restart the function
            # and give the user an option to quit
            print('\nInvalid cryptogram. Please retry or hit X to quit.\n\n')
            cipher_acceptor()
        else:
            # If the RegEx is fine, replace double spaces with single spaces and remove trailing spaces
            cipher = re.sub(r'(\s\s+)', " ", cipher.rstrip())  # rstrip() removes trailing spaces
    else:
        # Be courteous
        quit("\nThank you for trying out this program.")


def clue_acceptor():
    # Ask the user to give us x=y type clue for our cipher
    global clue_key
    global clue_value
    clue = input("\nEnter the clue (e.g. w=c) for the cipher:\n")
    # Make sure the clue is not empty
    if not (clue is None or clue == ''):
        # Strip all spaces and convert to lowercase
        clue = re.sub(r'(\s+)', "", clue.rstrip()).lower()  # rstrip() removes trailing spaces
        # RegEx to check the clue is of the form x=y that we need
        if re.search(r'^[a-z]+=+[a-z]$', clue):
            # Split at '=' and save the first part [0] as key and the second part [1] as value
            clue_key = re.split("=", clue)[0]
            clue_value = re.split("=", clue)[1]
        elif not (clue == 'X' or clue == 'x'):
            # If the clue is not of the format we need
            print("\nSomething is wrong with your clue. Please re-enter the clue.\n\n")
            clue_acceptor()
        else:
            # If the user wants to quit, let's be courteous
            quit("\nThank you for trying out this program.")
    elif clue == 'X' or clue == 'x':
        # Again, be courteous
        quit("\nThank you for trying out this program.")
    else:
        # If the clue is blank
        print("\nYou have not entered a clue. Please retry or hit 'X' to quit.\n\n")
        clue_acceptor()


def main():
    # Call acceptor() to accept an input cipher
    cipher_acceptor()
    clue_acceptor()
    # DELETE THE LINE BELOW WHEN THE PROGRAM IS COMPLETE
    print('\nCryptogram: ' + cipher + '\nClue: ' + clue_key + '=' + clue_value + '.')


if __name__ == '__main__':
    main()
