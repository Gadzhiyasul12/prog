week = ("Monday", "Tuesday", "Wednasday") # картеж
print(week[1])
# week2 = "Thursday", "Friday"
# week3 = "Saturday",
# print(week3)
# full_week = []
# full_week.append(week)
# print(full_week)
#a, b = week2
# print(a, b)
# x, y, z, с = "ПН", "ВТ", "СР"
# print()

pupils = {"Карл Маркс", "Алиберт Эйнштен",\
"Султанмурад", "Ч. Дарвин", "Карл Маркс"}
print(pupils)
if "Карл Маркс" in pupils:
     print("Карл Маркс побудил!! Коммунизм по всей планете")
else:
    print("Забудь о коммунах!")

madteam = {"Карл Маркс", "Алиберт Эйнштен",\
"Джон Нэш", "Дональд Трамп", "Мальчик-ракета"}
print(pupils & madteam) # пересечение
print(pupils | madteam) # объединение
print(pupils - madteam) # вычитание
print(madteam - pupils)

print("_" * 50)

films = {
	"Люся": "Люся получает супермозг",
	"Безумный Маркс": "Земля превратилась в пустыню - коммунизм победил!"
	"Защитники": "Наш ответ Западу! Медведь, Узбек, деваха-невидимка - суперскуад"
}
print(films["Защитники"])
films["Люся"] = "Люся теряет костный мозг"
print(films)
films[7] = "жестокий фильм про семь смертных греков"
print(films[7])
films["Человек-паук 1", "Второй человек-паук"] = "Слив", "Шлак"
print(films["Человек-паук 1", "Второй человек-паук"])

if key in films:
	print((films[film]))
 