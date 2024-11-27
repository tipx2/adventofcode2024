import requests
import os.path
from datetime import datetime

if not os.path.isfile("session.txt"):
  print("Please put session token in a file named 'session.txt' in the same folder as this script")
  exit(0)

def r(n):
  n = str(n)
  s = requests.session()
  s.cookies.set("session", open("session.txt", "r").read().strip())
  
  response = s.get("https://adventofcode.com/2024/day/" + n + "/input")
  data = response.text
  
  w_file = "day" + n + "/input" + n + ".txt"
  with open(w_file, "w") as f:
    f.write(data)
  
  print("Wrote to '\033[94m" + w_file + "\033[0m'")


if datetime.today().month == 12:
  r(datetime.today().day)
else:
  print("Not December")
  