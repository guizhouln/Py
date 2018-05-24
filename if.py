# if.py
number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # new fuction
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # End
elif guess > number:
    # other function
    print('No, it is a little higher than that!')
else:
    print('No, it is a little lower that that!')

print('Done^_^')

while True:
    s = input ("Enter something :")
    if s =="quit":
        break
    print("Length of the string is", len(s))
print('Done')