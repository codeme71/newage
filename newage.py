import datetime

# Дата начала отсчета
start_date = datetime.datetime(2001, 1, 1, 0, 0, 0)

# Текущая дата
current_date = datetime.datetime.now()

# Разница в секундах
seconds_elapsed = (current_date - start_date).total_seconds()

# Преобразование в шестнадцатеричное представление
hex_seconds = hex(int(seconds_elapsed))

# Вывод результата
print(f"Число секунд с полуночи 1 января 2001 года: {hex_seconds}")
