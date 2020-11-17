def shopping(items, payment='card', shop= 'local'):
    result= ""
    result= result + f'Idę na zakupy {shop}\n'
    result= result + f'Kupię następujące rzeczy:\n'
    for item in items:
        result= result + f'{item}\n'
    result = result + f'By zapłacić, używam {payment}'
    return result

items= ['cola', 'whiskey', 'lód']
print(shopping(items, 'card', 'small local shop'))

