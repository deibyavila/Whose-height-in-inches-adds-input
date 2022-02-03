from urllib.request import urlopen
import pandas as pd
import json
from itertools import combinations

URL = 'https://mach-eight.uc.r.appspot.com/'

response = urlopen(URL)
data_json = json.loads(response.read())
h_in =   pd.DataFrame(data_json["values"]).values.tolist()
  
def findPairs(lst, K):
 
    res = []
    for var in combinations(lst, 2):
        if int(var[0][1]) + int(var[1][1]) == K:
            res.append((var[0], var[1]))   
    return res

def printResult(res):
    if len(res)==0:
      print("No matches found")
    else:
      for r in res:
        print(r)

if __name__ == '__main__':
  print("Please input height to searches through NBA player pairs heights:")
  input_a = int(input())
  printResult(findPairs(h_in, input_a))
