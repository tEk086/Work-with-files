
import os
from pprint import pprint


def read_data():
    current_folder = os.getcwd()
    file = 'cook_book.db'
    path = os.path.join(current_folder, file)
    cook_book = {}
    with open(path, 'rt', encoding='utf-8') as file:
        for line in file:
            name_dish = line.strip()
            ingredient_count = int(file.readline())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            file.readline()
            cook_book[name_dish] = ingredients
    return cook_book


def get_shopping_list(dishes, person_count):
    cook_book = read_data()
    buy_list = {}
    for dish in dishes:
        if dish not in cook_book.keys():
            return f'Oops! Указанное блюдо: {dish} - отсутствует в книге рецептов. =('
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name in buy_list.keys():
                buy_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                buy_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
    return buy_list


if __name__ == '__main__':
    pprint(get_shopping_list(['Запеченный картофель', 'Омлет'], 2), sort_dicts=False)
