import requests  # Импорт библиотеки requests
from bs4 import BeautifulSoup  # Импорт класса BeautifulSoup из библиотеки BeautifulSoup


def get_text():

    url = 'https://lyrsense.com/blue_system/dr_mabuse?ysclid=lzjtpzhdax957559763#v1'  # Задание URL-адреса страницы с курсами валют
    response = requests.get(url)  # Отправка GET-запроса к указанному URL

    if response.status_code != 200:  # Проверка успешности запроса (код 200 означает успех).
        print(f"Ошибка: Невозможно получить доступ к странице. Код ошибки: {response.status_code}")
        return None
    # eng
    soup = BeautifulSoup(response.text, 'html.parser')  # Создание объекта BeautifulSoup для анализа HTML-кода страницы
    table = soup.find('p', {'class': 'hs'})  # Поиск таблицы с курсами валют на странице


    if not table:  # Проверка наличия таблицы с курсами валют
        print("Ошибка: Таблица с курсами валют не найдена на странице.")
        return None
    textEng = ""
    for data in table:
        textEng += data.getText() + "\n"

    # rus
    table = soup.find('p', {'id': 'ru_text'})  # Поиск таблицы с курсами валют на странице

    if not table:  # Проверка наличия таблицы с курсами валют
        print("Ошибка: Таблица с курсами валют не найдена на странице.")
        return None
    textRus = ""
    for data in table:
        textRus += data.getText() + "\n"


    mixedSong = []
    linesEng = textEng.split("\n")
    linesRus = textRus.split("\n")
    for lineEng,lineRus in zip(linesEng, linesRus):
        if lineEng:
            mixedSong.append(lineEng)
        if lineRus:
            mixedSong.append(lineRus)
    result = '\n'.join(mixedSong)
    result.replace('\n', '')
    return result

if __name__ == "__main__":

    rates = get_text()
    print(rates)
