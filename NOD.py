import random
# Импортируем модуль для определения количества времени потраченого для выполнения программы 
from datetime import datetime
def myNod_first(first_i, second_i):
# Проверяем является ли первое число больше второго, если да то выполняем следующее  
	if first_i<second_i:
		if second_i%first_i == 0 :
			print("Первый вход = Общий делитель = " + str(first_i))
			return ferst_i
		else:
			#Создается счетчик перебирающий все цифры в загаданном числе от большего к меньшему
			for i in range(first_i):
			#Проверяем делится ли оба числа  на одно и тоже число 
				if (first_i % (first_i - i)) == 0 and (second_i %(first_i - i)) == 0 :
					print("Второй вход  = Общий делитель = " + str(first_i - i))
					print (i)
					print("Второй вход  = Общий делитель = " + str(first_i - i))
					return first_i - i
	else:
		if first_i%second_i == 0 :
			print("Третий вход  = Общий делитель =" + str(second_i))
			return second_i
		else:
			#Создается счетчик перебирающий все цифры в загаданном числе от большего к меньшему
			for i in range(second_i):
				#Проверяем делится ли оба числа  на одно и тоже число 
				if (first_i % (second_i - i)) == 0 and (second_i %(second_i - i)) == 0 :
					print("Четвертый вход = Общий делитель = " + str(second_i - i))
					return second_i - i

print("Это программа вычисляет средний делитель 3-мя способами \n")
print("Первый способ опредялем общий делитель путем перебора цифр в числе")
# Генерируем первое случайное число 
first_int =int(random.randint(1, 1000000))
# Генерируем второе случайное число 
second_int = int(random.randint(1, 1000000))
#Засекаем время 
start_time = datetime.now()
nom = myNod_first(first_int,second_int)
end_time = datetime.now()

print(str(nom) + " мое число ")
print('Время работы первого способа: {}'.format(end_time - start_time))