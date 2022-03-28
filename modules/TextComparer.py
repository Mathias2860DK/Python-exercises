import requests
class TextComparer:
  

    def __init__(self, url_list):
         self.url_list = url_list
        
    
    def download(self, url):
        #url = 'https://api.github.com/users/Thomas-Hartmann'
        #r = requests.get(url)
        print(url)

        r = requests.get(url)

        return r.status_code