import requests
import os.path
from datetime import datetime

headers = {
  "User-Agent" : "https://github.com/tipx2/adventofcode2024 by tipx2gaming [AT] gmail [DOT] com" 
}

if not os.path.isfile("session.txt"):
  print("Please put session token in a file named 'session.txt' in the same folder as this script")
  exit(0)

def getInput(n):
  n = str(n)
  s = requests.session()
  s.cookies.set("session", open("session.txt", "r").read().strip())
  
  response = s.get("https://adventofcode.com/2024/day/" + n + "/input", headers=headers)
  data = response.text
  
  w_file = "day" + n.zfill(2) + "/input" + n + ".txt"
  with open(w_file, "w") as f:
    f.write(data)
  
  print("Wrote to " + w_file)

def createSource(n):
  n = str(n)
  w_file = "day" + n.zfill(2) + "/day" + n
  
  if os.path.isfile(w_file + "pt1.py"): # do not overwrite if source files already exist
    return
  
  default = f"with open(\"day{n.zfill(2)}/input{n}.txt\") as f:\n  lines = [x.strip() for x in f.readlines()]\n\n"
  f = open(w_file + "pt1.py", "w")
  f.write(default)
  f = open(w_file + "pt2.py", "w")
  f.close()
  
  


if datetime.today().month == 12:
  t = datetime.today().day
  getInput(t)
  createSource(t)
else:
  print("Not December")
