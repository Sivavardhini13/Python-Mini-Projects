def ai_number_guesser():
    print("Think of a number between 1 and 100 and I will try to guess it!")
    
    low = 1
    high = 100
    attempts = 0
    
    while True:
        attempts += 1
        guess = (low + high) // 2
        print(f"My guess is: {guess}")
        
        feedback = input("Is it higher, lower, or correct? (h/l/c): ").strip().lower()
        
        if feedback == 'c':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
        else:
            print("Invalid input. Please respond with 'h', 'l', or 'c'.")

# Start the game
ai_number_guesser()