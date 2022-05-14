candidates = [
 {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores":2},
 {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores":1},
 {"name": "Vasyl", "scores": {"math": 57, "russian_language": 61, "computer_science": 47}, "extra_scores":2},
 {"name": "Fed", "scores": {"math": 31, "russian_language": 88, "computer_science": 21}, "extra_scores":3},
 {"name": "Pet", "scores": {"math": 98, "russian_language": 28, "computer_science": 31}, "extra_scores":1},
 {"name": "Vasya2", "scores": {"math": 58, "russian_language": 62, "computer_science": 41}, "extra_scores":0},
 {"name": "Fedya2", "scores": {"math": 33, "russian_language": 85, "computer_science": 40}, "extra_scores":2},
 {"name": "Petya2", "scores": {"math": 92, "russian_language": 33, "computer_science": 30}, "extra_scores":1},
 {"name": "Vasyl2", "scores": {"math": 57, "russian_language": 61, "computer_science": 40}, "extra_scores":2},
 {"name": "Fed2", "scores": {"math": 31, "russian_language": 88, "computer_science": 7}, "extra_scores":3},
 {"name": "Pet2", "scores": {"math": 98, "russian_language": 28, "computer_science": 3}, "extra_scores":1},
 {"name": "Vasya3", "scores": {"math": 51, "russian_language": 62, "computer_science": 41}, "extra_scores":0},
 {"name": "Fedya3", "scores": {"math": 27, "russian_language": 85, "computer_science": 40}, "extra_scores":2},
 {"name": "Petya3", "scores": {"math": 85, "russian_language": 33, "computer_science": 30}, "extra_scores":1},
 {"name": "Vasyl3", "scores": {"math": 50, "russian_language": 61, "computer_science": 40}, "extra_scores":2},
 {"name": "Fe", "scores": {"math": 24, "russian_language": 88, "computer_science": 7}, "extra_scores":3},
 {"name": "Pe", "scores": {"math": 97, "russian_language": 28, "computer_science": 3}, "extra_scores":1},
 {"name": "Va", "scores": {"math": 51, "russian_language": 62, "computer_science": 41}, "extra_scores":0},
 {"name": "Fedya4", "scores": {"math": 30, "russian_language": 85, "computer_science": 40}, "extra_scores":2},
 {"name": "Petya4", "scores": {"math": 15, "russian_language": 33, "computer_science": 30}, "extra_scores":1},
 {"name": "Vasy4", "scores": {"math": 16, "russian_language": 61, "computer_science": 40}, "extra_scores":2},
 {"name": "Fed4", "scores": {"math": 17, "russian_language": 88, "computer_science": 7}, "extra_scores":3},
 {"name": "Pet4", "scores": {"math": 18, "russian_language": 28, "computer_science": 3}, "extra_scores":1}
]

from operator import itemgetter, attrgetter
def find_top_20(candidates):
    
    cand_list = []
    score_list = []
    info_scores = []
    math_scores = []

    # создадим четыре списка: имя, итоговый рез-т, рез-т по информатике и математики
    for i in candidates:
        cand_list.append(i['name'])
        score_list.append((i['scores']['math']) + (i['scores']['russian_language']) + \
        (i['scores']['computer_science']) + (i['extra_scores']))
        info_scores.append(i['scores']['computer_science'])
        math_scores.append(i['scores']['math'])

    candidates_scores = list(zip(cand_list, score_list, info_scores, math_scores))

    candidates_scores = sorted(candidates_scores, key=itemgetter(1,2,3), reverse=True)[0:20]

    return candidates_scores
    # проверка результата
    # for i in candidates_scores:
    #     print(i)

# вызываем функцию и получаем требуемый результат, реализована многоуровневая
# сортировка сначала все баллы, затем с учетом информатики и затем по математике.
# print(find_top_20(candidates))