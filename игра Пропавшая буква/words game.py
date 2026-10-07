words = ["колледж", "робот", "экран", "тест", "Астана"]
indexes = [4, 2, 2, 1, 2]
def hide_letter(word, index):
    return word[:index] + "_" + word[index+1:]
def check_word(answer, word):
    return answer.strip().lower() == word.strip().lower()
def show_progress(solved, total):
    print(f"Восстановление слов: {solved} из {total}")
def read_choice(prompt, allowed):
    while True:
        choice = input(prompt).strip()
        if choice in allowed:
            return choice
        print("Неизвестная команда! Попробуйте снова.")
def play_game():
    solved = 0
    total = len(words)
    for i in range(len(words)):
        word = words[i]
        idx = indexes[i]
        shown = hide_letter(word, idx)
        print("Слово:", shown)
        attempts = 2
        while attempts > 0:
            answer = input("Введите полное слово: ")
            if answer.strip() == "":
                print("Пустой ввод не считается!")
                continue
            if check_word(answer, word):
                print("Верно!")
                solved = solved + 1
                break
            attempts = attempts - 1
            if attempts > 0:
                print("Неверно. Осталась 1 попытка.")
            else:
                print("Неверно. Загаданное слово:", word)
        show_progress(solved, total)
    print("Игра окончена! Решено слов:", solved)
    if solved >= 4:
        print("Победа!")
    else:
        print("Поражение.")
def show_rules():
    print("=== Правила игры ===")
    print("Показывается слово, в котором одна буква заменена на _.")
    print("Вам нужно ввести полное слово.")
    print("На каждое слово — 2 попытки.")
    print("Победа — угадать минимум 4 слова из 5.")
def menu():
    while True:
        print("              МЕНЮ")
        print(" ╔════════ДОБРО ПОЖАЛОВАТЬ════════╗")
        print(" ║1.          Начать              ║")
        print(" ║2.          Правила             ║")
        print(" ║0.          Выход               ║")
        print(" ╚════════════════════════════════╝")
        choice = read_choice("Выбор: ", ["0", "1", "2"])
        if choice == "0":
            break
        elif choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        else:
            print("Неизвестная команда! Ход не засчитан. Попробуйте снова.")
menu()