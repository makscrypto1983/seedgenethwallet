import random
from eth_account import Account
from eth_account.messages import encode_defunct
import xlwt

# Включение экспериментальных функций HD Wallet
Account.enable_unaudited_hdwallet_features()

# Считываем имена из файла
with open('first_names.txt', 'r') as f:
    first_names = f.read().splitlines()

# Считываем фамилии из файла
with open('last_names.txt', 'r') as f:
    last_names = f.read().splitlines()

# Запрос количества мнемонических фраз
num_mnemonics = int(input("Введите количество мнемонических фраз для генерации: "))

# Генерация мнемонических фраз и сохранение их в файл
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("Мнемонические фразы")
row = 0
for i in range(num_mnemonics):
    # Создание аккаунта с мнемонической фразой
    acct, mnemonic = Account.create_with_mnemonic()

    # Получение адреса аккаунта
    address = acct.address

    # Генерация случайного имени и фамилии
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # Формирование строки с именем и фамилией
    name = f"{first_name} {last_name}"

    # Проверка, что аккаунт создан правильно
    assert acct == Account.from_mnemonic(mnemonic)

    # Запись мнемонической фразы и имени в файл
    worksheet.write(row, 0, f"Мнемоническая фраза {i+1}:")
    worksheet.write(row, 1, mnemonic)
    row += 1
    worksheet.write(row, 0, f"Адрес Кошелька {i+1}:")
    worksheet.write(row, 1, address)
    row += 1
    worksheet.write(row, 0, "Имя:")
    worksheet.write(row, 1, name)
    row += 2

workbook.save("mnemonics.xls")

print(f"Сгенерировано {num_mnemonics} мнемонических фраз. Результаты сохранены в файле mnemonics.xls.")