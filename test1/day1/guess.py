age_of_old = 56
guess_age = int(input("guess age:"))

if guess_age == age_of_old:
    print("yes")
elif guess_age > age_of_old:
    print("big")
else:
    print("small")