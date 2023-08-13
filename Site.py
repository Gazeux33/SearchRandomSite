import random
import requests
import json
import os 



class Site:
    def __init__(self):
        
        self.search = True
        
        self.data_word = self.get_data("word.json")
        self.data_name = self.get_data("name.json")
        self.data = self.data_name + self.data_word
        
        self.data_site = self.get_data("site.json")
        
        self.search_site()
        
        
    def get_data(self,filename:str):
        with open(f"data/{filename}","r") as file:
            data = json.load(file)
            return data
        
    def update(self,filename,data):
        self.data_site.append(data)
        with open(f"data/{filename}","w") as file:
            json.dump(self.data_site,file,indent=2)
            
        
    def get_url(self):
        name = random.choice(self.data)
        url = f"https://www.{name}.com/"
        return url
          
          
    def search_site(self):
        
        while self.search == True:
            self.url = self.get_url()
            try:
                request = requests.get(self.url)
                if request.status_code == 200:
                    print(f"Site trouvé:{self.url}")
                    self.update("site.json",self.url)
                    self.search = False
            except:
                print(f"echec:{self.url}")

        
if __name__ == "__main__":
    r = Site()
