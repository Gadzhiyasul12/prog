#numbers = (input("Введите числа:"))
#numbers_list = numbers.split(" ")
#for i in numbers_list:
   # n = 0
  #  numbers_list[0] = int(i)
 #   n += 1


#print(numbers_list)

#print(len(numbers_list))
#print(min(numbers_list))
#print(max(numbers_list))

numbers2 = [20, 15, 21, 99]

guess = int(input("Отгадай число: "))
# print(guess in numbers2)
if guess in numbers2:
	print("Ты чертов экстрасенс!!")
else:
	print("Ты облажайся, парень!")