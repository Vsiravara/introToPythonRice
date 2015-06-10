
# Mini Project 2 
# Vishwas Siravara

# import libraries 
import random
import simplegui

# define global variables
# number of guesses remaining,secret number
secret_number = 0
num_of_guesses = 7
num_range = 100

# helper function to start and restart the game
def new_game():
    """ initialize a random number so that game can begin """
    global num_of_guesses
    global secret_number 
    global num_range
    print
    secret_number = random.randrange(0, num_range)
    
    if num_range == 1000:
        num_of_guesses = 10
    
    else: 
        num_of_guesses = 7
       
    print "New game range is from 0 to " + str(num_range)
    print "Number of remaining guesses is " + str(num_of_guesses)
        
    
# define event handlers for control panel
def range100():
    """ Reset game to 7 tries and number range between 0 - 100"""
    
    print
    global num_range 
    num_range = 100 
    new_game()

def range1000():
    """ Reset game to 10 tries and number range between 0 - 1000"""
    print
    global num_range
    global num_of_guesses
    num_range = 1000
    new_game()
 
def input_guess(guess):
    """ handler for textbox , takes input from user ,checks it 
    against computer choice and takes necessary action based on the guess"""
    
    # convert string to float   
    user_input = float(guess)
    global secret_number
    global num_of_guesses
    global num_range
    # check if out of guesses , if so call newgame to reset 
   
    
    num_of_guesses -= 1
    print "Guess was " + guess
    print "Number of remaining guesses is " + str(num_of_guesses)
    
    if user_input < secret_number :
        print "Higher"
        
       
    elif user_input > secret_number :
        print "Lower"
        
       
    else:
        print "Correct"
        print
        new_game()
       
     
    if num_of_guesses == 0:
        print "You lost , lets start a new game"
        new_game()
       
        
    
    print
    
# create frame

fr = simplegui.create_frame("Guess the Number",300,300)

# register event handlers for control elements and start frame
# register button handlers 

button1 = fr.add_button("Range is [0,100)", range100, 100)
button2 = fr.add_button("Range is [0,1000)", range1000, 100)

# register textbox input handler for guess

inp1 = fr.add_input(" Enter a Guess ", input_guess, 100)

# start the frame
fr.start()


# call new_game 
new_game()



# always remember to check your completed program against the grading rubric
