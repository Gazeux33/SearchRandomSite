import random
import requests
import json
import os


PATH_NAME = os.getcwd()
search = True


with open(os.path.join(PATH_NAME,"data/name.json"),"r") as file:
    data_name = json.load(file)
    

with open(os.path.join(PATH_NAME,"data/word.json"),"r") as file:
    data_words = json.load(file)
    
data = data_name + data_words


while search == True:
    name = random.choice(data)
    url = f"https://www.{name}.com/"
    try:
        request = requests.get(url)

        if request.status_code == 200:
            print(f"Site trouvé:{url}")
            search = False
    except:
        print(f"echec:{url}")


