def count_letters(s): #Фукнция для подсчета букв
    vowels = "аеёиоуыэюя" #Гласные
    not_vowels = "бвгджзйклмнпрстфхцчшщ" #Согласные
    vowels_amount = 0 #Инициализация количества гласных
    not_vowels_amount = 0 #Инициализация количества согласных
    for char in s.lower(): #Перевод к строчному виду
        if char in vowels: #Проверка на гласную
            vowels_amount+=1 #Добавление к счетчику гласных
        elif char in not_vowels: #Проверка на согласную
            not_vowels_amount +=1 #Добавление к счетчику согласных
    return vowels_amount, not_vowels_amount #Возвращение значений
string = input("Введите строку: ") #Ввод строки
length= len(string) #Определение длины строки
vowels, not_vowels = count_letters(string) #Выполнение функции
print(f"Длина всей строки: {length}") #Вывод длины строки
print(f"Количество гласных в строке: {vowels}") #Вывод количества гласных
print(f"Количество согласных в строке: {not_vowels}") #Вывод количества согласных
