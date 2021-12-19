from enum import Enum

# Токент бота
TOKEN = '5029500189:AAFBXXZSWdoNWfDJD-m9Cz5FAjBOuuCxFmI'

# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
#CURRENT_STATE = "CURRENT_STATE"

# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_NAME = "STATE_NAME"
    STATE_AGE = "STATE_AGE"
    STATE_OPERATION = "STATE_OPERATION"
