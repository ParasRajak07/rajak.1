import json
import os


#
def load_data(filename):
  if os.path.exists(filename) == False:
    file = open(filename, "w")
    json.dump([], file)
    file.close()
    return []

  file = open(filename, "r")
  data = json.load(file)
  file.close()
  return data

def save_data(filename, data):
  file = open(filename, "w")
  json.dump(data, file, indent=4)
  file.close()