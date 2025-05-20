secret=5

guess=int(input("enter your guess : "))

if guess > secret:
    print("your guess is too high")
elif guess<secret:
    print("your guess is too low")
elif guess == secret:
    print("your guess is correct")