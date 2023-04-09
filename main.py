import logging
from config import Config
import requests


def activate_trainer():
    response = requests.post(
        url="https://pokemonbattle.me:9104/trainers/confirm_email",
        headers={"Content-Type": "application/json"},
        json={"trainer_token": "a5527c11d7bd9a20421aedfb9af5d60a"}
    )
    logging.log(
        level=logging.INFO,
        msg="Тренер активирован"
    )


def create_pokemon(pokemon_name):
    response = requests.post(
        url="https://pokemonbattle.me:9104/pokemons",
        headers={"trainer_token": Config.BEST_TRAINER_TOKEN,
                 "Content-Type": "application/json"},
        json={"name": pokemon_name,
              "photo": "https://dolnikov.ru/pokemons/albums/001.png"}
    )
    if response.ok:
        print(response.json())
        logging.log(
            level=logging.INFO,
            msg=f"Создан покемон: '{pokemon_name}'"
        )
    elif not response.ok:
        print(response.json())
        logging.log(
            level=logging.INFO,
            msg=f"Попытка создать покемона: '{pokemon_name}'"
        )


def info_trainer():  #Использовать для получения id покемона перед запросом на изменение его имени/ фото.
    response = requests.get(
        params={"trainer_id": Config.TRAINER_ID},
        url="https://pokemonbattle.me:9104/trainers",
    )
    print(response.json())
    logging.log(
        level=logging.INFO,
        msg=f"Запрос информации о тренере '{Config.TRAINER_ID}' для получения id покемона"
    )

def rename_newphoto_pokemon(pokemon_id, new_name):
    response = requests.put(
        url="https://pokemonbattle.me:9104/pokemons",
        headers={"trainer_token": Config.BEST_TRAINER_TOKEN,
                 "Content-Type": "application/json"},
        json={"pokemon_id": pokemon_id,
              "name": new_name,
              "photo": "https://dolnikov.ru/pokemons/albums/001.png"}
    )
    print(response.json())
    logging.log(
        level=logging.INFO,
        msg=f"Изменено имя и/или фото покемона '{pokemon_id}'"
    )

def set_to_pokeball(pokemon_id):
    response = requests.post(
        url="https://pokemonbattle.me:9104/trainers/add_pokeball",
        headers={"trainer_token": Config.BEST_TRAINER_TOKEN,
                 "Content-Type": "application/json"},
        json={"pokemon_id": pokemon_id}
    )
    print(response.json())
    logging.log(
        level=logging.INFO,
        msg=f"Покемон '{pokemon_name}' добавлен в покебол"
    )

if __name__ == '__main__':
    logging.basicConfig(level=Config.PROJECT_LOG_LEVEL)  # Уровень логирования
    pokemons_names = ["name1", "name2", "name3", "name4", "name5"]

    activate_trainer()

    for name in pokemons_names:
        create_pokemon(pokemon_name=name)

    rename_newphoto_pokemon(pokemon_id=8866, new_name="chu")
    set_to_pokeball(pokemon_id=8866)
