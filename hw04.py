# ------------------------------------------------------
#        Name: (put your name here)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food" 

# Task 1

def check_text():
    """
       Ask the user to enter a sentence.
       Check if this sentence contains the secret word.
       If it does, print "You used the secret word".
       If it dose not, print "Try again".
       Check if this sentence contains "dog" or "Dog".
       If it dose, print "You used the works "dog" or "Dog"!"
       If it dose not, print "Try again".
       """    
    text = input("Give me a sentence: ")

    while (secret_word not in text
           and "dog" not in text
           and "Dog" not in text):

        print("Try again")
        text = input("Give me a sentence: ")

    if secret_word in text:
        print("You used the secret word!")

    else:
        print('You used the word "dog" or the word "Dog"!')
    



# Task 2
def check_greater():
    """ Ask the user to enter 2 integers.
        If these 2 intergers are equal, print "Try again."
        If the first interger is greater, print "First one is Greater"
        If the seconf interger is greater, print "Second one is Greater "
    """
    num_1 = int(input("Give me the first interger "))
    num_2 = int(input("Give me the second interger "))
    
    # Repeat when the two integers are equal
    while num_1 == num_2:
        print("Try again")
        num_1 = int(input("Give me the first interger "))
        num_2 = int(input("Give me the second interger "))
        
    # Compare the two integers      
    if num_1 > num_2:
        print("First is Greater")
    else:
        print("Second is Greater")
        
    print("Done")



# Task 3
def get_special_numbers():
    """ Get a list of intergers from 1 to 40.
        Exam these integers that whether they satisfy 3 criteria
        If they satisfy, skip them.
        If they not satisfy, print them out.
    """
    for num in range(1,41):
        if num % 2 != 0 and num % 3 == 0 and num % 5 != 0:
            print(num)
        


# Task 4.a
def my_for_loop():
    """ Ask for a string from the user.
        If the string length is not in the range [2,5], or if the string has spaces,
        Then the function should immediately return.
        If the word is of a valid length, then the function should print one of the following things:
        if the letter is a vowel, it should print: "letter <let> is a vowel" 
        if the letter is a consonant, it should print: "letter <let> is a consonant"
    """
    word = input("Give me a instring: ")
    # Check the length
    if len(word) < 2 or len(word) > 5:
        print("bad word")
        return
    # Check for spaces
    if " " in word:
        print("bad word")
        return
     # Check each letter
    for each_letter in word:
        if each_letter in "aeiou":
            print(f"{each_letter} is a vowel")
        else:
            print(f"{each_letter} is a consonant")
            
        
        
        
        

# Task 4.b
def my_while_loop():
    """ Repeat the menu until the user chooses to leave. """
    while True:
        choice = input("Choose one option: a, b, or c: ")
        
        if choice not in ["a", "b", "c"]:
            print("try again")
            
        elif choice == "a":
            continue
        
        elif choice == "b":
            print("Goodbye")
            return
            
        else:
            sys.exit()

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():
   


    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
