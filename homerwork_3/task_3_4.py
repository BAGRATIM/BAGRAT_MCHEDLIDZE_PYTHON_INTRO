# შემთხვევითი კარტის დაბეჭდვა 52 კარტიდან

from random import choice

def generate_random_card():
    
    colors = ['clubs', 'diamonds', 'hearts', 'Spades']
    ranks = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    
    color = choice(colors)
    rank = choice(ranks)
    
    print("Your card is", rank, color)

generate_random_card()
