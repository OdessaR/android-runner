from glob import glob
import json


config_web_gogreen_memoized = {}
config_web_gogreen_normal = {}
with open("trepn/config_web_gogreen_memoized.json", "r") as f: config_web_gogreen_memoized = json.load(f)

with open("trepn/config_web_gogreen_normal.json", "r") as f: config_web_gogreen_normal = json.load(f)


config_web_gogreen_normal["paths"] = []
config_web_gogreen_memoized["paths"] = []


for path in sorted(glob("../gogreen/experiment-files/normalExec/*")):
    config_web_gogreen_normal["paths"].append("file:///storage/emulated/0/" + path[3:])

for path in sorted(glob("../gogreen/experiment-files/memoizedExec/*")):
    config_web_gogreen_memoized["paths"].append("file:///storage/emulated/0/" + path[3:])


with open("trepn/config_web_gogreen_memoized.json", "w") as f: json.dump(config_web_gogreen_memoized, f, indent=2)

with open("trepn/config_web_gogreen_normal.json", "w") as f: json.dump(config_web_gogreen_normal, f, indent=2)
