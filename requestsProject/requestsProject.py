"""
Project Name: [Pokemon Shiny Comparison]
Developer: [Gabriel Arias]
Date: 2026-02-11
Purpose: This app manages [Pokemon sprites] by persisting data to [shiny.txt] in order to display them and save the order that the user last looked at them in.
"""

import time
import requests
from io import BytesIO
from PIL import Image
import random
def main():
    base_url = "https://pokeapi.co/api/v2/"
    def get_pokemon_info(name):
        url = f"{base_url}/pokemon/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            return pokemon_data
        else:
            print(f"Failed to retrieve data {response.status_code}")
    def pokemon_user(): #write function
        loopy = int(input('how many pokemon?\n'))
        for i in range(loopy):
            pokemon_name = input('Pokemon name?')
            with open('shiny.txt','a') as file:
                file.write(pokemon_name+'\n')
    def pokemon_placement(file): #read function 
         for line in file: 
            val = line.strip("\n")
            pokemon_name = str(val)
            pokemon_info = get_pokemon_info(pokemon_name)
            print(f"Name: {pokemon_info['name'].capitalize()}")
            print(f"ID: {pokemon_info['id']}")
            imgUrl = pokemon_info["sprites"]
            default = requests.get(imgUrl["front_default"])
            normalImg = Image.open(BytesIO(default.content)).convert("RGBA")
            shiny = requests.get(imgUrl["front_shiny"])
            shinyImg = Image.open(BytesIO(shiny.content)).convert("RGBA")
            w, h = normalImg.size
            canvas = Image.new("RGBA", (w * 2, h), (255, 255, 255, 0))
            canvas.paste(normalImg, (0, 0), mask=normalImg) 
            canvas.paste(shinyImg, (w, 0), mask=shinyImg)
            canvas.show()
    try:
        skip = int(input('Do you want to use previous list? (put 1 for yes, anything else for no)'))
        if skip == 1:
            with open ('shiny.txt','r') as file:
              pokemon_placement(file)
        else:
             with open('shiny.txt','w') as file:
                pass
             pokemon_user()
             with open('shiny.txt', 'r') as file:
                pokemon_placement(file)
    except FileNotFoundError: 
        print('whoopsie no file found try again')
    except ValueError:
        print('wrong value try again')
main()