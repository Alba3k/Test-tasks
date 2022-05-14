# Пример входных данных:
students_avg_scores = {
'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 
'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 
'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}

import csv 

def make_report_about_top3(students_avg_scores):

	# сортируем словарь и получаем топ 3
	top_3 = sorted(students_avg_scores.values(), reverse=True)[0:3]
	top_3_dict = {}

	# проходим циклом по словарю основному и добавляем в новый топ 3
	# только те значения которые соответствую нашим параметрам
	for i in top_3:
		for k in students_avg_scores.keys():
			if students_avg_scores[k] == i:
				top_3_dict[k] = students_avg_scores[k]
				break

	with open("Top_3.csv", mode="w") as csvfile:
        # создаем csv writer
		csvWriter = csv.writer(csvfile)
        # пишем заголовки
		csvWriter.writerow(["Student", "Scores"])
        # заполняем строками данных из словаря
		for i, j in top_3_dict.items():
			csvWriter.writerow([i, j])

# вызываем функцию и получаем требуемый результат
# make_report_about_top3(students_avg_scores)