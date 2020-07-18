import flask
import threading

app = flask.Flask('Github Follower Bot')

@app.route('/', methods=['GET','POST'])
def home():
  return 'pong'

def start():
  app.run(host="0.0.0.0", port=3000)

# thread = threading.Thread(target=start)
# thread.start()