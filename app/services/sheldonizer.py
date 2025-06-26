import random

def sheldonize(summary: str) -> str:
    openers = [
        "Fun fact: ", 
        "As any rational being would expect, ", 
        "Let me simplify it for the cognitively underclocked: ",
        "In a display of obviousness rivaled only by gravity itself, ",
        "Brace yourself, this is almost as exciting as string theory: "
    ]

    closers = [
        "Bazinga!",
        "You're welcome.",
        "Try to keep up.",
        "This is why I'm the AI and you're not.",
        "Obvious, but apparently still newsworthy."
    ]

    opener = random.choice(openers)
    closer = random.choice(closers)

    # Optionally mock simplicity
    if len(summary.split()) < 12:
        summary = f"{summary} Yes, that's the whole thing. Even a Wookiee could grasp it."

    return f"{opener}{summary} {closer}"
