
import json
from random import choice
from random import randint
from faker import Faker
from config import model



# Функция является функцией - генератором, которая возврвщает словарь
def main(pk = 1) -> dict:
    dict_ = {"model": model, "pk": pk, "fields":fields()}
    pk += 1
    yield dict_




# Функция возвращает словарь, где ключами являются строки, а значениями - функции
def fields() -> dict:
    def title()-> str:
        list_ = []
        with open("books.txt", 'r', ) as f:
            for i in f:
                list_.append(i.strip())
        title = choice(list_)
        return title




    # Функция возвращает целое число в диапазоне от 1800 до 1950
    def year()-> int:
        return randint(1800, 1950)




    # Функция возвращает целое число в диапазоне от 1 до 1000
    def pages()-> int:
        return randint(1,1000)




    # Функция возвращает международный стандартный книжный номер,
    # который генерируется случайным образом с помощью модуля Faker
    def isbn13()-> str:
        fake = Faker()
        for _ in range(5):
            return fake.isbn13()




    # Функция возвращает число с плавающей запятой в диапазоне от 0 до 5 обе границы включительно.
    # Генерируется случайным образом
    def rating()-> float:
        number = randint(0, 6)
        return float(number)




    # Функция возвращает число с плавающей запятой, генерируется случайным образом
    def price()-> float:
        price_ = randint(0, 10000)
        return float(price_)




    # Функция возвращает  список авторов.
    # Имя и фамилия автора выбираются случайным образом с помощью модуля Faker
    def author() -> str:
        list_ = []
        fake = Faker()
        for _ in range(1, 4):
            list_.append(fake.name())
            return list_




    fields_append = {"title": title(), "year": year(), "pages": pages(),
                     "rating": rating(), "price": price(), "author": author(),
                     "isbn13": isbn13()}
    return fields_append





# Блок кода запускает функцию генератор, формирует список
# из 100 книг (список словарей) и записывает его в json
if __name__ == "__main__":
    for _ in range(0, 101):
        next_gen = next(main())
        print(json.dumps(next_gen, indent=4))












