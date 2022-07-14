import requests
import json
from rich import inspect

class FecRequest:
    def __init__(self, url, params):
        self.url = url
        self.params = params
        self.data = self.get_request()
        self.pagination = self.get_pagination()
        self.results = self.get_results()
        # self.pages = self.pagination.get("pages")
        
    def inspect_results(self):
        inspect(self.results)
        

    def get_request(self):  
        session = requests.Session() 
        r = session.get(self.url, params=self.params).json()    
        return r

    def get_pagination(self):    
        dump = json.dumps(self.data.get("pagination"))
        pagination = json.loads(dump)      
        return pagination
    
    def get_results(self):
        dump = json.dumps(self.data.get("results"))
        results = json.loads(dump)    
        return results  
    
    def get_pages(self):
        return self.get_pagination().get("pages")


if __name__ == "__main__": 
    pass

