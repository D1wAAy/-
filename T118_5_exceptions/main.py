def share_cost(total,people):
    return total/people
def read_integer(prompt, minimum):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Введите целое число")
        else:
            if number < minimum:
                print("Минимальное допустимое значение", minimum)
            else:
                return number
total = read_integer("Стоимость поездки, тенге: ", 0)
people = read_integer("Количество участников: ", 1)
result = share_cost(total, people)
print("С каждого участника:", round(result, 2), "тенге")