def read_scores(count):
    scores = []
    while len(scores) < count:
        try:
            score = int(input(f"Оценка {len(scores) + 1} (0-100): "))
        except ValueError:
            print("Введите целое число")
        else:
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Допустимо от 0 до 100")
    return scores
def show_statistics(scores):
    if len(scores) == 0:
        print("Нет результатов")
        return
    passed = 0
    for i in scores:
        if i >= 70:
            passed += 1
    print("Количество:", len(scores))
    print("Сумма:", sum(scores))
    print("Среднее:", round(sum(scores) / len(scores), 2))
    print("Мин:", min(scores), "Макс:", max(scores))
    print("Прошли:", passed, "Остальные:", len(scores) - passed)
def retest_scores(scores):
    result = []
    for i in scores:
        if i < 70:
            result.append(i)
    return sorted(result)
def replace_score(scores, number, value):
    if number < 1 or number > len(scores):
        return False
    if value < 0 or value > 100:
        return False
    scores[number - 1] = value
    return True
scores = read_scores(5)
print(scores)
show_statistics(scores)
print("На пересдачу:", retest_scores(scores))
if len(scores) > 0:
    while True:
        try:
            number = int(input("Номер оценки для исправления: "))
            value = int(input("Новая оценка: "))
        except ValueError:
            print("Введите целые числа")
            continue
        if replace_score(scores, number, value):
            break
        print("Ошибка: неверный номер или оценка")
    print(scores)
    show_statistics(scores)
    print("На пересдачу:", retest_scores(scores))