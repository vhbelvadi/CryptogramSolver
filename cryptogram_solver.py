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


def acceptor():
    # The line below tells Python we're going to use the same
    # global variable called cipher and that we are not creating
    # a new function-specific one also called cipher
    global cipher
    # Get an input from the user
    cipher = input("Enter the cipher:\n")
    # Make sure the user does not want to not quitting
    if not (cipher == 'X' or cipher == 'x'):
        # Check if input follows RegEx for a typical cryptoquip
        if not re.search(r'^[a-zA-Z\s\D.,\-\'\"?!]+$', cipher):
            # If it does not follow RegEx inform the user and restart the function
            # and give the user an option to quit
            print('\nInvalid cryptogram. Please retry or hit X to quit.\n\n')
            acceptor()
        else:
            # If the RegEx is fine, replace double spaces with single spaces and remove trailing spaces
            cipher = re.sub(r'(\s\s+)', " ", cipher.rstrip())  # rstrip() removes trailing spaces
    else:
        # Be courteous
        quit("\nThank you for trying out this program.")


def main():
    # Call acceptor() to accept an input cipher
    acceptor()
    print('\nCryptogram: ' + cipher)  # DELETE THIS LINE WHEN THE PROGRAM IS COMPLETE


if __name__ == '__main__':
    main()
