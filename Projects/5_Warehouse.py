"""Program do obsługi magazynu
Porządek:
1. importy
2. listy
3. funkcje
4. program"""

import logging, sys

items= [
        {ware:'456_Longneck', qnt:100000, unit:1000, price:99.00}, 
        {ware:'454_Bier', qnt:25000, unit:1000, price:180.00}, 
        {ware:'155_Bordeaux', qnt:50000, unit:1000, price:150.00}
]

item = [i for i in items]
sold = None
sold_items = []
sold_items = sold_items.append(sold)

def menu():
    ask = input("""Co chcesz zrobić?
show - aktualny stanu magazynowego
add  - dodaj nową pozycję w magazynie
sell - nowa sprzedaż
income - przychody
cost - wartosc towarów w magazynie
revenue - zysk
save - zapisz stan jednego z powyższych do pliku
load - wgraj dane z pliku
exit - wyjscie z programu
: """)
    #while ask != exit
    if ask == 'exit':
        print('Do zobaczenia.')
        quit()
        exit()
    elif ask == 'show':
        get_items()
    elif ask == 'add':
        add_item()
    elif ask == 'sell':
        sale()
    elif ask == 'cost':
        get_cost
        
def get_items():
    ware = 'Article'
    qnt = 'Quantity'
    unit = 'Unit'
    price = 'Price'
    
    print('| {:^15}| {:^9}| {:^6}| {:^7} |' .format(ware, qnt, unit, price))
    print('-'*(17+11+8+11))
    for i in items:
        print('|', i[0],' '* (13-len(i[0])),'|', i[1], ' '*(7-len(str(i[1]))) \
,'|', i[2],' '*(4-len(str(i[2]))),'|', i[3],' '*(6-len(str(i[3]))), '|' )

    menu()
    
def add_item():
    ware = input('Nazwa towaru: ')
    qnt = int(input('Ilosć: '))
    unit = int(input('Jednostka: '))
    price = float(input('Cena: '))
    together = [ware, qnt, unit, price]
    items.append(together)
    print('\nZaktualizowano stan magazynu:\n')
    get_items()


def sale(ware = input('Nazwa towaru: '), qnt = input('Ilosć: ')):
    
    to_substraction = None

    for item in items:
        if ware == item[0]:
            to_substraction = item[1]
            #TODO:Uwzględnić dostępny stan magazynowy
            new_stock = to_substraction - int(qnt)
            item[1] = new_stock
    
    sold = [ware,qnt,item[2],item[3]]
    sold_items.append(sold)
    
    
    print('\nZaktualizowano stan magazynu:\n')
    #return(new_stock)
    
    get_items()
    
    menu()
    
def get_cost():
    wares_cost = [(item[1]*item[3])/item[2] for item in items]
    
    menu()
    
def income():
       

    
if __name__=='__main__':
    menu()
