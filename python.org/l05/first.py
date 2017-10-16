#def my_func(name):
#	print("здрасти " + name)

#my func("ултанмурад")

#def my_sun(a, b):
	#print(a + b)
#	return a + b

#ab_sun = my_sun(25, 50)
#number1 = int(input("Введите первое число"))
#number2 = int(input("Введите второе число"))
#print(my_sun(number1, number2))


#def my_divide(n1, n2, n3, n4, n5, n6):
#  res = n1 / m + p * o + k / l
#   return res
    
#print(my_divide(n = 15, m =  5, o = 15, k = 20, p = 40, l = 18))

#def ground (name1 = "Саид", name2 = "Султанмурад", name3 = "Руслан"):
 #   ground_list = "в нашей группе есть: " + name1 + name2 + name3
#    return ground_list

#ground("Гаджи", "аслан", "шамиль", "Ахмед", "Залик")
#print(ground("Гаджи ", "Аслан ", "Ахмед"))

#print(15, 20)
#print(15, 20, 123, sep ="\n")
#print(15, 20, sep = "разбить")

def human_list(*args, **kwargs):
    for human in args:
	     print(human + " -grandfather ")
	     print( kwargs)


human_list("адам", "ева","Кайн", "Авель", gadfather = "Крестный отец", hogfather = "Лукман")
