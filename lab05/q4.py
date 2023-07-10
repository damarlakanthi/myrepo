import requests
import json
url = "https://michaelgathara.com/api/python-challenge"
# Send a GET request to retrieve the challenge
response = requests.get(url)
# Extract the challenges from the response
challenges = response.json ()
print(challenges)

for i in challenges:
    print("the ans for  " +str(i['id'])+" :")
    prob = i['problem']
    prob=prob[0:len(prob)-1]
    print (eval(prob))
#print (challenges)