# Задание 1
number = int(input("Enter a number: "))

positive_number = 0
negative_number = 0

while number != 0:
    if number > 0:
        positive_number += 1
    else:
        negative_number += 1

    number = int(input("Enter a next number: "))

print('Позитивные: ', positive_number)
print('Негативные: ', negative_number)

# Задание 2

hour = 0
task_sum = 0
go_to_store = False

print('8-мичасовой рабочий день')

while hour !=8:
    hour += 1
    print(hour, 'час')

    tasks = int(input('Сколько задач решит Максим? '))
    task_sum += tasks
    call = int(input('Звонит жена. Взять трубку? (1 - да; 0 - нет): '))

    if call == 1:
        go_to_store = True
    print('Paбочий день кончился, выполненно ', task_sum, ' задач')
if go_to_store:
    print('Нужно зайти в мазагин')

# Задание 3

number = 7
guess_count = 0

while True:
    guess_num = int(input('Enter a number: '))
    guess_count += 1

    if guess_num > number:
        print('Число больше чем нужно')
    elif guess_num < number:
        print('Число меньше чем нужно')
    else:
        print('Ты угадал! Ответ = ', number)
        break

print('Количество попыток: ', guess_count)

# Задание 4

salary_year = 0
for month in range(1, 13):
    salary_month = int (input('Введите зп сотрудника за месяц {}:  '.format(month)))
    salary_year += salary_month

salary = salary_year / 12
print('Средняя зп за год: ', salary)

# Задание 5

total_cards = int(input('Введите количество карточек: '))