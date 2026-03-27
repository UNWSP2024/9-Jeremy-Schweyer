# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).
import random
Amount = int(input("Enter how many random numbers you want to generate: "))
if Amount > 1000:
    print("Too high of a value try again")
else:
    Random_number = open('random.txt', 'w')

    for count in range(1, Amount + 1):
        Random = random.randint(1, 500)
        Random_number.write(str(Random) + ' ')
    Random_number.close()
    Random_number = open('random.txt', 'r')
    Number = Random_number.readlines()
    Random_number.close()
    print(Number)
    print("Random numbers generated successfully!")
