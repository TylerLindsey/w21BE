from flask import Flask, request, jsonify
from helpers.db_helpers import run_query

app = Flask(__name__)

@app.post('/api/poster')
def poster_post():
  # TODO DB select
  poster_list =run_query()
  # will replace the above at some point
  return jsonify(poster_list), 200
# poster is what i am calling the data, liike animals in the class example
@app.post('/api/poster')
def poster_post():
  data = request.json
  # above isva the object that allows me to access the data from the request
  poster_name = data.get('posterName')
  # above is the name of variable in the API request
  # document what exactly the name is (capitalization and whatnot)
  
  # check if the above is set, if the get has no value in the dictionary the data will return none because none is = to false, so use conditional to add an error if the value is none 
  if not poster_name:
    return jsonify('Could not process but understood the request'), 422
