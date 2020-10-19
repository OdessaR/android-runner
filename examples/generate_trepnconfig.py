from glob import glob
import json


config_web_gogreen_memoized = {}
config_web_gogreen_normal = {}
with open("trepn/config_web_gogreen_memoized.json", "r") as f: config_web_gogreen_memoized = json.load(f)

with open("trepn/config_web_gogreen_normal.json", "r") as f: config_web_gogreen_normal = json.load(f)


config_web_gogreen_normal["paths"] = []
config_web_gogreen_memoized["paths"] = []

config_web_gogreen_memoized_auto = []
config_web_gogreen_normal_auto = []

population_auto = []

for path in sorted(glob("../gogreen/experiment-files/normalExec/*")):
    if path[3:].startswith("gogreen/experiment-files/normalExec/auto."):
        config_web_gogreen_normal_auto.append("file:///storage/emulated/0/" + path[3:])
        population_auto.append(path.split("/")[-1])
    else:
        config_web_gogreen_normal["paths"].append("file:///storage/emulated/0/" + path[3:])


for path in sorted(glob("../gogreen/experiment-files/memoizedExec/*")):
    if path[3:].startswith("gogreen/experiment-files/memoizedExec/memoizedAuto."):
        config_web_gogreen_memoized_auto.append("file:///storage/emulated/0/" + path[3:])
    else:
        config_web_gogreen_memoized["paths"].append("file:///storage/emulated/0/" + path[3:])


population_auto = set(population_auto)
for i in range(0, 50):
    t = population_auto.pop()
    config_web_gogreen_normal["paths"].append("file:///storage/emulated/0/gogreen/experiment-files/normalExec/%s" % t)
    config_web_gogreen_memoized["paths"].append("file:///storage/emulated/0/gogreen/experiment-files/memoizedExec/memoized%s" % t[0].upper() + t[1:])


# print("\n".join(config_web_gogreen_memoized["paths"]))

with open("trepn/config_web_gogreen_memoized.json", "w") as f: json.dump(config_web_gogreen_memoized, f, indent=2)

with open("trepn/config_web_gogreen_normal.json", "w") as f: json.dump(config_web_gogreen_normal, f, indent=2)
