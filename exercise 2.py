def procenty(sum, prc, mnth):
    procenty = prc / 100
    print(procenty)
    for i in range(mnth):
        sum = (procenty / 12 * (sum)) + sum
        print(f'Ваш вклад будет {sum} на {i + 1} месяц')


prc = int(input('Введите процент: '))
vklad = int(input('Введите сумму вклада: '))
month = int(input('Введите количество месяцев: '))
procenty(vklad, prc, month)
