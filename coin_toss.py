# FILE NAME - coin_toss.py

# NAME: Antonio Santiago    
# DATE: 10/1/2025
# BRIEF DESCRIPTION:  This program is a simple application that will randomly return Heads or Tails. To calculate, 
# a random number between 1 and 100 (inclusive) is generated and if the number is 51 or greater then Tails is reported. Otherwise Heads is reported.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!

import random

def main():
    coin_toss()

def coin_toss():
    print("===== Coin Flipper =====")
    random_num = random.randrange(1,100)
    
    if random_num >= 51:
        print("Tails")
    else:
        print("Heads")

main()





########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
Figuring out how I want to generate a random number within a range. 






'''


########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[X] I'm solid. Totally got it.
'''
