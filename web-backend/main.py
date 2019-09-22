from flask import Flask
from textblob import TextBlob
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/depression/<username>")
def get_depression_index(username):
  page = requests.get("https://www.instagram.com/" + username + "/?hl=en")
  message = str(page.content)
  score = 0
  count = 0
  while '"text":"' in message and '"}}]}' in message:
    index1 = message.index('"text":"') + 8
    index2 = message.index('"}}]}')  
    s = message[index1:index2]
    text = TextBlob(s)
    print(s)
    print(text.sentiment.polarity)
    print()
    score += text.sentiment.polarity
    count += 1
    message = message[index2 + 5:]
  print (score/count)
  return "The Depression Index is: " + str(score/count)

app.run(host='0.0.0.0')

