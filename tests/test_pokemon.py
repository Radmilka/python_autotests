import requests

from config import Config


def test_status():
    response_status = requests.get(
            url="https://pokemonbattle.me:9104/trainers"
        )
    assert response_status.status_code == 200

def test_trainer_name():
    response = requests.get(
            url=f"https://pokemonbattle.me:9104/trainers?trainer_id={Config.TRAINER_ID}"
        )
    trainer_info = response.json()
    trainer_name = trainer_info.get("trainer_name")  #.get - команда для поиска значения в словаре по ключу
    #словарь - пайтоновская структура данных, из которой можно получать значения по ключу (можно найти через дебаг)
    assert trainer_name == "best"




