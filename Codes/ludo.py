import random

position = 0
home = 57
game_over = False

print("🎲 Welcome to One-Player LUDO 🎲")

while not game_over:
    input("Press Enter to roll the dice... ")
    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")

    if position == 0:
        if dice == 6:
            position = 1
            print("🎉 You got a 6! You're out of the block and on position 1.")
        else:
            print("❌ You need a 6 to start. Try again.")
    else:
        steps_needed = home - position

        if dice < steps_needed:
            position += dice
            print(f"You moved to position {position}.")
        elif dice == steps_needed:
            position += dice
            print(f"🏁 You moved to {position}. You've reached HOME! Game Over. 🎉")
            game_over = True
        else:
            print(f"⚠️ You need exactly {steps_needed} to reach home. Try again.")

print("Thanks for playing!")
