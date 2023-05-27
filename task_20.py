rus = {("А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"): 1,
       ("Д", "К", "Л", "М", "П", "У"): 2, ("Б", "Г", "Ё", "Ь", "Я"): 3,
       ("Й", "Ы"): 4, ("Ж", "З", "Х", "Ц", "Ч"): 5,
       ("Ш", "Э", "Ю"): 8, ("Ф", "Щ", "Ъ"): 10}
russian = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И',
           'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
           'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
eng = {("A", "E", "I", "O", "U", "L", "N", "S", "T", "R"): 1,
       ("D", "G"): 2, ("B", "C", "M", "P"): 3,
       ("F", "H", "V", "W", "Y"): 4, ("K",): 5,
       ("J", "X"): 8, ("Q", "Z"): 10}
english = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
count = 0
word = input("Введите слово: ")
if word[0] in english:
    for letter in word:
        for key, value in list(eng.items()):
            lst = list(key)
            if letter.upper() in lst: count += value
else:
    for letter in word:
        for key, value in list(rus.items()):
            lst = list(key)
            if letter.upper() in lst: count += value
print(count)