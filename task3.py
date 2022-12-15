salary = int(input('Введите зп: '))

count_25r = salary // 25
count_10r = (salary - count_25r * 25) // 10
count_3r = (salary - count_25r * 25 - count_10r * 10) // 3
count_1r = salary - count_25r * 25 - count_10r * 10 - count_3r * 3

print(f'Для выдачи зп понадобится:\n\t{count_25r} 25-руб.,\n\t{count_10r} 10-руб.,\n\t{count_3r} 3-руб.,\n\t{count_1r} 1-руб.')