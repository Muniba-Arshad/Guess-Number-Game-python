print("="*35)
print("----GUESS NUMBER GAME PYTHON----")
print("="*35)
import random 
num=random.randint(1,100)
guess=int(input("Guess number between 1 and 100"))
if guess>100 or guess<1:
  print("Please enter between 1 and 100")
  guess=int(input("Guess Again!"))
attempt=1
score=3
while attempt<=3:
   if guess==num:
    print("CONGRATULATIONS!! Your guessed in ",attempt,"attempts")
    print("Your score is ",score,"/3")
    break
   elif guess > num:
     print("TOO High!Guess a smaller number.") 
   else:
     print("TOO Low!Guess a larger number.")  
   attempt=attempt+1
   score=score-1  
   guess=int(input( "Guess again")  ) 
if guess!=num:
 print("OOPS!! You failed .The correct number is ",num)
print("="*35)
print("---Thank you for playing game---")
print("="*35)
