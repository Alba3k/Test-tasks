<div align="center">

# Test-tasks.
Тестовые задачи и решение.
</div>


![GitHub](https://img.shields.io/badge/Alba3k-Test--tasks-brightgreen?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/Alba3k/Test-tasks?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Alba3k/Test-tasks?style=for-the-badge)




## Task_01. Гордость университета :classical_building:

- У студентов-программистов шел последний год обучения, и близилась выдача дипломов. 
К этой знаменательной дате было решено подготовить символические подарки трем студентам, 
которые имеют максимальный средний балл по итогам обучения. 
Но задача осложнялась тем, что нужно предоставить эти данные в бухгалтерию, 
причем так, чтобы главный бухгалтер Ольга Петровна, 
списывающая деньги на подарки, смогла открыть это в своём любимом Excel.

- Впрочем, для Вас, человека который работает не первый год в данном учреждении, 
это не казалось невыполнимой задачей.
Вам нужно написать функцию make_report_about_top3

- Функция make_report_about_top3 принимает словарь (students_avg_scores), 
в котором ключами являются имена студентов, а значениями — средний балл за всю учебу. 
Функция находит ТОП-3 студентов, чей средний балл выше, чем у других. 
Функция возвращает ссылку на эксель-файл, в котором упомянуты 3 студента и который 
потом будет передан в бухгалтерию. Сам файл необходимо создать внутри функции. 
Важно сохранить совместимость с Excel, чтобы Ольга Петровна смогла без проблем получить 
всю нужную информацию.                                        

### Пример входных данных:

```python
students_avg_scores = {
'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 
'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 
'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}
```

***

## Task_02. Соревнования :medal_sports:

- Знакомые вам студенты-программисты уже пережили не одну сессию. 
Кое-кто из них продемонстрировал потрясающие способности в учебном процессе. 
Другим только предстояло проявить себя во всей красе. 
Однажды в Ваш кабинет уверенно постучался и вошел физрук. 
Начал он свою историю издалека, что, мол, университету нужны таланты, 
что некому представлять ваше учебное заведения на международных соревнованиях по плаванию. 
И словно невзначай спросил - "А нет ли у Вас на примете подходящих кандидатур? 
Да еще чтоб хотя бы немного знали английский. 
Ах да, еще и возрастное ограничение — не младше 20 лет". 

- Немного порывшись в памяти вы вспомнили тройку широкоплечих студентов-программистов, 
которые могли бы быть хорошими кандидатами. 
Но вот имен их, как ни старались, припомнить не смогли. 

- Однако вы знали, что при поступлении будущие студенты заполняли анкету. 
Потом же на основании этих анкет были созданы списки для разделения 
по изучаемому языку (чтобы учитывать ранее приобретенные знания и не 
смешивать языковые группы в одну кучу) и списки, описывающие хобби студентов. 
Дело оставалось за малым — взять тех, кто знает английский и 
одновременно имеет интерес к спорту. Ну и совместить это дело со списком тех, 
кто перешагнул черту 20-летия, который был получен загодя
Вам нужно написать функцию find_athlets

- Функция find_athlets принимает 3 списка с именами студентов. 
В первом списке (know_english) — список тех, кто хорошо владеет английским языком. 
Второй (sportsmen) — содержит имена тех, кто увлекается спортом. 
Ну и третий (more_than_20_years) — предоставляет информацию о тех, кто старше 20 лет. 
Функция возвращает список имен студентов, которые подходят под все три критерия.         

### Пример входных данных:

```python
know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]
```

***

## Task_03. Военнообязанные :guard:

- Шел 2021 год. Большая часть студентов, которых Вы когда-то помогли отобрать для 
поступления в университет, успешно учится. В знак благодарности вам выделили личный кабинет, 
поскольку помощь оказалась неоценимой. Отношения с коллегами стали крепче после тех дней. 
Кстати, о коллегах…

- Однажды утром возле двери кабинета Вы встретились с зам. декана, который выглядел озадаченно. 
После недолго объяснения стало понятно, что местный военкомат интресуется, сколько 
студентов мужского пола являются военнообязанными (достигшими 18 лет). 
Нужно сформировать список этих студентов. 

- В качестве исходных данных вам предлагают лист, на котором написаны имена студентов, 
их пол и возраст. К несчастью,  где-то по центру этого листа расположено 
огромное пятно от пролитого кофе, что испортило часть записей. 
Единственное, что осталось нетронутым — имена.

- Вам нужно написать функцию get_inductees
Функция get_inductees принимает 3 списка одинаковой длины. В первом списке (names) — имена студентов, 
позволяющие их точно идентифицировать. Во втором (birthday_years) — год рождения. 
В третьем (genders) — пол студента.Частично они отсутствуют ввиду испорченного листа бумаги. 
Функция возвращает список с именами студентов мужского пола, которые достигли или могут 
достигнуть 18 лет в 2021 году, но при этом не старше 30 лет. Cтуденты, по которым невозможно 
точно установить - попадают они в список или нет (из-за порчи данных), должны быть выведены отдельно.

### Пример входных данных:

```python
names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo"]
birthday_years = [1962,1995,2000,None,None,None,None,1998,2001]
genders = ["Male","Female","Male","Female","Male",None,None,None,None]
```                                                                        

***

## Task_04. Набор новых студентов :man_student:

- Подходило 1 сентября, университет готовился к наплыву абитуриентов. Так вышло, что Вы, 
как программист, должны были помочь в отборе тех абитуриентов, кто поступит в университет 
на конкурсной основе на специальность программиста. 

- Схема была проста: есть абитуриент, у него есть результаты сданных экзаменов по математике, 
русскому и информатике. Соответственно, у каждого потенциального студента есть сумма баллов 
по этим экзаменам. Также есть дополнительные (extra_scores) баллы: за волонтерство, 
участие в олимпиадах и другие активности. 

- Вам нужно отобрать 20 человек, у которых суммарный балл выше, чем у других. В случае, 
если не получается однозначно определить 20 человек (например, 2 человека набрали одинаковое 
СУММАРНОЕ количество баллов и претендуют на 20 место в списке, стоит их ранжировать 
по "профильным" дисциплинам - "информатике" и "математике").
Напишите функцию find_top_20

- Функция принимает на вход список сводной информации по абитуриентам (candidates) 
и возвращает список с  именами 20 человек, набравших наибольшее СУММАРНОЕ количество баллов 
(с учетом extra баллов), которые станут студентами университета.                                                                                      
### Пример входных данных:

```python
candidates = [
{"name": "Vas", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
{"name": "Fed", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores":2},
{"name": "Pit", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores":1}
]
```