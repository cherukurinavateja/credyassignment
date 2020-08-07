from requests.auth import HTTPBasicAuth
import requests
import json

# Get movie page sent by client
def movieList(mv_url):
    while True:
        a=requests.get(mv_url, auth=HTTPBasicAuth('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0', 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
        if a.status_code == 200:
            mv_list= json.loads(a.content)
            break
    return mv_list

#Get total page count of pagination
def movie_page_count():
    while True:
        a=requests.get('https://demo.credy.in/api/v1/maya/movies/', auth=HTTPBasicAuth('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0', 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
        if a.status_code == 200:
            mv_list= json.loads(a.content)
            pg_count= mv_list['count']
            break
    return pg_count


