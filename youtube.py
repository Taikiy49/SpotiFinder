import os
import requests

class YoutubeQuery:
    def __init__(self, query):
        self._query = query
    def run(self):
        api_key = os.environ["YOUTUBE_API_KEY"]
        url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&part=snippet&q={self._query}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data



# # this will be temp
# if __name__ == '__main__':
#     YoutubeQuery('Tomorrow').run()
