import pyrebase, json

firebaseConfig = {
  "apiKey": "AIzaSyC6Kl26Y1kY35DRudHAsXA9EjHE0zu4Wvo",
  "authDomain": "disaster-data-extraction.firebaseapp.com",
  "databaseURL": "https://disaster-data-extraction-default-rtdb.firebaseio.com",
  "projectId": "disaster-data-extraction",
  "storageBucket": "disaster-data-extraction.appspot.com",
  "messagingSenderId": "403244136343",
  "appId": "1:403244136343:web:90b7b6190ee0e49533b6d2",
  "measurementId": "G-HMEZSZZ1DX"
}

firebase = pyrebase.initialize_app(firebaseConfig);
db = firebase.database()

def push_demo_data():
    victims = db.child("victims")
    victims.push({
            "name" : "abhiraj kale",
            "age" : 19,
            "location": "Vidyavihar",
            "x coord": "1.00.0.1.0",
            "y coord": "1.0.0.1.0",
            "people": 4
    })    

def push_twitter_data(disaster, created_at, text, username, source, source_url, location):
  twitter = db.child("twitter").child(disaster)
  twitter.push({
    "created_at" : created_at, 
    "text": text,
    "username" : username, 
    "source" : source, 
    "source_url" : source_url, 
    "location": location
  })

def push_keywords(list, user_id):
    db.child('victims').child(user_id).update({
      "keywords" : list
      })

def get_all_data():
    return (json.dumps(db.child("victims").get().val()))

def upload_audio(user_id): 
  storage = firebase.storage()
  
  path_on_cloud = f'audio/Mumbai/{user_id}/foo.wav'
  local = "street_20dB.wav"
  storage.child(path_on_cloud).put(local)
  
def download_file(path_on_cloud, local_path):
  storage = firebase.storage()
  storage.child(path_on_cloud).download(local_path)
 