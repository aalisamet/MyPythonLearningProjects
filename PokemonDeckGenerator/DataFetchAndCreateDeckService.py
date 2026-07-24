import aiohttp
import aiohttp as request
import PokemonModel as Pokemon
import random
import asyncio






async def fetch_pokemon(session: request.ClientSession, index: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{index}/"

    # await ile HTTP isteğinin cevabı beklenirken diğer işlere izin verilir
    async with session.get(url) as response:
        data = await response.json()

        # İstediğin alanları süzme (Abilities)
        abilities = [x["ability"]["name"] for x in data["abilities"]]

        # Nesneyi döndürme
        return Pokemon.Pokemon(data["name"], abilities)

async def create_deck():
    pokemon_deck: list = []
    pokemon_indecies: list = []

    for i in range(1, 6):
        pokemon_index = random.randint(1, 1025)
        pokemon_indecies.append(pokemon_index)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_pokemon(session, index) for index in pokemon_indecies]
        pokemon_deck = await asyncio.gather(*tasks)

    for pokemon in pokemon_deck:
        print(pokemon.__str__())


