#Получать все продукты в холодильнике
#перебрат ьи приготовить 
#дать название нашему блюду = взять первые буквы ингредиента

import random

def my_cook(*args, Major = " Мазик"):
    for product in args:
        making_food(product)
    print("Обильно нальём сверху" + Major)

def making_food(ingridient):
    print(random.choice(cook_variants) + " " + ingridient)



cook_variants = ("Пожарим", "Сварим", "Разгоним", "Похороним")

my_cook("яйца", "молоко", "процессор", "труп кошек", "корм для кошек")