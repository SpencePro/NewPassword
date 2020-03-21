password = "STR123"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while True:
    if guess_count == guess_limit:
        out_of_guesses = True
        break
    if guess != password and not out_of_guesses:
        guess = input("Enter your password: ")
    else:
        print("Access granted")
        break
if out_of_guesses:
    print("You are out of guesses")