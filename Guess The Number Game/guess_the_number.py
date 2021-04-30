from random import randint

start = 1
end = 1000
value=randint(start,end)
print("The computer has chosen a number between ",start," and ",end)
guess=None

while guess !=value:
    text = input("Guess the number: ")
    guess = int(text)
    
    if guess<value:
        print("The number is Higher!")
    elif guess>value:
        print("The number is Lower!")
print("Congratulations!! You guessed the number.You won!")    
            
