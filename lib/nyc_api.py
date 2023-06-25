
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  def program_school(self):
    program_list= []
    programs = json.load(self.get_programs)
    for program in programs:
      program_list.append(program["agency"])
    return program_list  

programs = GetPrograms().get_programs()
print(programs)
