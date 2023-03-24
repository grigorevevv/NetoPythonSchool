# завести переменную с лучшим классом
# завести переменную с лучшей оценкой
# открываем файл
## итерируемся циклом по тройкам строк
### считаем среднее арифмитеческое оценок класса
### сравниваем среднее с лучшей оценкой
#### если среднее наилучшее - записываем лучший класс
   # и обновляем лучшую оценку
### переходим к следующей итерации
# закрываем файл
# печатаем результат

best_grade, best_rating = None, 0

with open('grades.txt') as f:
    while True:
        grade = f.readline().rstrip()
        ratings = f.readline().rstrip()
        f.readline()

        if not grade or not ratings:
            break

        split_ratings = ratings.split(' ')
        int_ratings = []
        for r in split_ratings:
            int_ratings.append(int(r))

        # int_ratings = [int(i) for i in ratings.split(' ')]

        avg_rating = sum(int_ratings) / len(int_ratings)
        print(f'Класс {grade}, оценки: {int_ratings}, '\
              f'средняя: {avg_rating}')

        if avg_rating > best_rating:
            print(f'Оценка {avg_rating} наилучшая на данный момент')
            best_rating = avg_rating
            best_grade = grade


print(f'Лучший класс {best_grade} с оценкой {best_rating}')

