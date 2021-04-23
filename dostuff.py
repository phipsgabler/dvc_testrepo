import json

with open("params.json") as fd:
    params = json.load(fd)
print(f"Param is: {params['testparam']}")

