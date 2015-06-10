# Rock-paper-scissors-lizard-Spock template
# Week 1 mini project
# Rock paper scissors lizard Spock 
# Vishwas Siravara 


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name== "rock" :
        number=0
        
    elif name=="Spock":
        number=1
     
    elif name=="paper":
        number=2
        
    elif name=="lizard":
        number=3
        
    elif name=="scissors":
        number=4
    
    else:
        print "Invalid Input"
        return
    
    return number


    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number== 0:
        name = "rock"
        
    elif number == 1:
        name="Spock"
        
    elif number == 2:
        name="paper"
        
    elif number == 3:
        name="lizard"
        
    elif number == 4:
        name="scissors"
        
    else:
        print "Invalid input in number_to_name"
        return
    
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print
    
    print "Player chooses " + player_choice
    
    player_number = name_to_number(player_choice)
    
    computer_number = random.randrange(0,5)
    
    
    
    print "Computer chooses " + number_to_name(computer_number)
    
    
    # print a blank line to separate consecutive games
    difference_in_num = player_number - computer_number
    
    if difference_in_num < 0 :
        difference_in_num = difference_in_num%5
        
    if difference_in_num == 0:
        print "Player and Computer tie! "
        
    elif difference_in_num < 3:
        print "Player wins!"
        
    else:
        print "Computer wins!"
    
   
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
#print name_to_number("scissors")
#print number_to_name(2)

# always remember to check your completed program against the grading rubric


