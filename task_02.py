# Пример входных данных:
know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]

def find_athlets(a, b, c):

	# преобразуем все списки в кортежи
	eng_set = set(know_english)
	sport_set = set(sportsmen)
	more_20 = set(more_than_20_years)

	# используя пересечение множеств найдем искомое и возвратим в список
	result = list(eng_set & sport_set & more_20)
	return result

# вызываем функцию и получаем требуемый результат
# print(find_athlets(know_english, sportsmen, more_than_20_years))
