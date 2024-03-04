import os
from dotenv import load_dotenv


load_dotenv()


class Data:                             # тут храним данные в скрытом формате

    # логин
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")

    LOGIN_A = os.getenv("LOGIN_A")
    PASSWORD_A = os.getenv("PASSWORD_A")