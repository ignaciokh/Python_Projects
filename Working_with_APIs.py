import requests

base_url = 'https://pokeapi.co/api/v2/'
 
def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("failed to retrive data")

pok_info = get_info('pikachu')


if pok_info:
    print(f"Name {pok_info["name"]}")
    print(f"Id {pok_info["id"]}")