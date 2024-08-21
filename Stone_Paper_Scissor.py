import random

def determine_winner(comp, you):
    if comp == you:
        return "It's a tie!"
    
    # Winning conditions for the player
    if (comp == 'stone' and you == 'paper') or \
       (comp == 'paper' and you == 'scissor') or \
       (comp == 'scissor' and you == 'stone'):
        return "You win!"
    
    return "You lose!"

def get_choice_name(choice_number):
    choices = {1: 'scissor', 2: 'paper', 3: 'stone'}
    return choices.get(choice_number, None)


comp_choice = random.choice(['stone', 'paper', 'scissor'])


try:
    user_choice_number = int(input("Enter 1 for scissor, 2 for paper, or 3 for stone: "))
    user_choice = get_choice_name(user_choice_number)

    if not user_choice:
        print("Invalid choice! Please enter 1, 2, or 3.")
    else:
        print(f"Computer chose: {comp_choice}")
        print(f"You chose: {user_choice}")
        
        result = determine_winner(comp_choice, user_choice)
        print(result)

except ValueError:
    print("Invalid input! Please enter a number (1, 2, or 3).")
