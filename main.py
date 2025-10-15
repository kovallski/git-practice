import requests

def get_weather(city_name):
    """
    Получает текущую погоду для указанного города.
    """
    # URL для запроса погоды с указанием формата вывода
    url = f'https://wttr.in/{city_name}?format=%C+%t'
    
    try:
        # Выполняем GET-запрос
        response = requests.get(url)
        
        # Проверяем, успешен ли запрос
        response.raise_for_status()
        
        # Выводим результат
        print(f"Погода в городе {city_name.capitalize()}: {response.text}")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

if __name__ == "__main__":
    print('Hi')
    # Запрашиваем у пользователя название города
    city = input("Введите название города: ")
    get_weather(city)
