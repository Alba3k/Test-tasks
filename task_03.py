# Пример входных данных:                                                                        
names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo"]
birthday_years = [1962,1995,2000,None,None,None,None,1998,2001]
genders = ["Male","Female","Male","Female","Male",None,None,None,None]

def get_inductees(names, birthday_years, genders):
	year = 2021
	age = []

	# определяю возраст при наличии данных
	for i in birthday_years:
		if type(i) == int:
			age.append(year - i)
		else:
			age.append(None)
		 
	# преобразуем в общий список c использованием итерации zip
	list_common = list(zip(names, birthday_years, genders, age))

	# создадим пустые списки для армии и для неизвестных лиц 
	list_army = []
	list_x = []

	# заполним неизвестный список и армейский список по критериям
	for i in list_common:
		if ((i[1] == None) or (i[2] == None)) and (i[2] != 'Female'):
			list_x.append(i)

	for i in list_common:
		if i[2] == 'Male' and (i[1]) and (18 <= i[3] < 30):
			list_army.append(i[0])

	return list_x, list_army

# вызываем функцию и получаем требуемый результат
# print(get_inductees(names, birthday_years, genders))