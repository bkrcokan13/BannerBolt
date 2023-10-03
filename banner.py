import requests
import bs4
import time
class Banner:
    def __init__(self):
        self._headers = {
             'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                           'AppleWebKit/537.36 (KHTML, like Gecko)'
                           'Chrome/116.0.0.0 Safari/537.36'),
            'Accept-Language': 'en-US, en;q=0.5'
        }
        
        self._base_url = "https://www.gumtree.com"
        self._search_url = "https://www.gumtree.com/search?search_category=all&q="

        self._categoriesUrl = []
    
    def url_collect(self):

        data = None

        try:
            request_url = requests.get(self._base_url, headers=self._headers, timeout=1)
            print("Sending request waiting...")
            time.sleep(1.2)
            
            #Check status code
            if request_url.status_code == 200:
                print("Status: Ok !")
                data = request_url.content
            elif request_url.status_code == 403:
                print("Status: Forbidden ! ")
            elif request_url.status_code == 503:
                print("Status: Service Temporarily Unavailable ! (NGINX)")
            else:
                print("Status: Request is failed, check url and retry ! ")
            

            # Get Categories Url

            url_soup = bs4.BeautifulSoup(data, 'html.parser')

            container =  url_soup.find_all(
                'ul',attrs={
                    'class':'css-wwpisx e4qfz7d2'
                }
            )

            for containerData in container:
                liData = containerData.find_all(
                    'li', attrs={
                        'class':'css-14yx5j e1c1vrhj2'
                    }
                )

                for li in liData:
                    aData = li.find_all(
                        'a',attrs={
                            'class':'css-8z8t0 e1c1vrhj0'
                        }
                    )

                    for a in aData:
                        self._categoriesUrl.append(self._base_url + a.get("href"))
            
            print("Status: Url collected !")
        except Exception as exception:
            print(exception)

app = Banner()
app.url_collect()
