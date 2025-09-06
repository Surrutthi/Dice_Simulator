import random

dice_faces = {
1: (
"┌───────┐",
"│       │",
"│   ●   │",
"│       │",
"└───────┘"
),
2: (
"┌───────┐",
"│ ●     │",
"│       │",
"│     ● │",
"└───────┘"
),
3: (
"┌───────┐",
"│ ●     │",
"│   ●   │",
"│     ● │",
"└───────┘"
),
4: (
"┌───────┐",
"│ ●   ● │",
"│       │",
"│ ●   ● │",
"└───────┘"
),
5: (
"┌───────┐",
"│ ●   ● │",
"│   ●   │",
"│ ●   ● │",
"└───────┘"
),
6: (
"┌───────┐",
"│ ●   ● │",
"│ ●   ● │",
"│ ●   ● │",
"└───────┘"
)
}

def roll_dice():
    return random.randint(1, 6)

print("🎲 Dice Rolling Simulator 🎲")

while True:
    input("Press Enter to roll the dice...")
    result = roll_dice()
    for line in dice_faces[result]:
        print(line)
    print("You rolled:", result)
    again = input("Roll again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")






