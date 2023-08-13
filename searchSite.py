import random
import requests
import json
import os 


PATH_NAME = os.getcwd()




def get_data():
    with open(os.path.join(PATH_NAME,"data/name.json"),"r") as file:
        data_name = json.load(file)
        
    with open(os.path.join(PATH_NAME,"data/word.json"),"r") as file:
        data_words = json.load(file)
        
        return data_name + data_words  
    
def update(site:str):
    with open(os.path.join(PATH_NAME,"data/site.json"),"r") as site_json_r:
        liste_site = json.load(site_json_r)
    liste_site.append(site)
    with open(os.path.join(PATH_NAME,"data/site.json"),"w") as site_json_w:
        json.dump(liste_site,site_json_w,indent=2)
        
        


def main():
    search = True
    data = get_data()
    while search == True:
        
        name = random.choice(data)
        url = f"https://www.{name}.com/"
        try:
            request = requests.get(url)
            if request.status_code == 200:
                print(f"Site trouvé:{url}")
                search = False
                update(url)
        except:
            print(f"echec:{url}")
            

        
if __name__ == "__main__":
    main()


