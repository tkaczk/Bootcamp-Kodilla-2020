shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    'chusteczki',
    'papier toaletowy'
]

def shopping(items):
    shopping_cart= 'Koszyk zawiera: '
    for item in shopping_items:
        shopping_cart+= item + '\n'
    return shopping_cart

basket = shopping(shopping_items)
print(basket)