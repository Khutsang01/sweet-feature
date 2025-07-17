#Guessing game while loop practice

secret_number = 7
guess_count = 0
guess = 0

#guess = int(input("Guess a number that is between (1-10): "))

while guess != secret_number:
    guess_count += 1
    guess = int(input("Guess a number that is between (1-10): "))

print(f"You have guessed it correctly on the {guess_count}th tries")

#Broken code practice
