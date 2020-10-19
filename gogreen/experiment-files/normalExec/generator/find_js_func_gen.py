from glob import glob
import csv

col_name = 0
col_cyclomatic = 1
col_line = 2
col_length = 3
col_params = 4
col_path = 5

res = []
with open("/home/pjotr/Downloads/function_stats.csv", "r") as f:
    for line in csv.reader(f.readlines()[6:]):
        if line[col_name]=="<anonymous>" or line[col_params] != "0": continue
        res.append({
            "path": line[col_path],
            "fn_name": line[col_name]
        })

import json
with open("res.json", "w") as f:
    f.writelines([json.dumps(res)])

template = """
<html>
<head>
<script src="../../websites/%s"></script>
</head>
<body>
<div id="res">Failed</div>
<script>
let failed = true;
try {
    %s();
    failed = false;
} catch (e) {
    failed = true;
}

document.getElementById("res").innerHTML = failed ? "Failed" : "Ok";
</script>
</body>
</html>
"""

# res

frames = []
i = 0
for item in res:
    path = item["path"][16:]
    fn_name = item["fn_name"]
    html = template % (path, fn_name)
    with open("tests/%d.html" % i, "w") as f: f.writelines([html])
    frames.append("tests/%d.html" % i)
    i += 1


html = """
<html>
<head>
</head>
<body>
<iframe id="iframe"></iframe>
<script>
var items = %s;
var total = items.length;
var data = {};
function loadNextItem() {
    var url = items.pop();
    console.log(url);
    if (url == "tests/645.html") url = items.pop();
    if (url == "tests/638.html") url = items.pop();
    iframe.setAttribute("src", url);
    console.log(1 - (items.length / total));
    if (items.length > 0) {
        iframe.onload = function() {
            var iframe = document.getElementById("iframe");
            var innerDoc = iframe.contentDocument || iframe.contentWindow.document;
            data[items.length] = innerDoc.getElementById("res").innerHTML;
            if (items.length > 0) {
                loadNextItem();
            } else {
                console.log(data);
            }
        };
    }
}
//loadNextItem();


</script>
</body>
</html>
"""
print(html % (json.dumps(frames)))
# with open("test_all.html", "w") as f:
#     f.writelines([html])