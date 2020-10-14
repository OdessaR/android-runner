from glob import glob
import csv
import json

col_name = 0
col_cyclomatic = 1
col_line = 2
col_length = 3
col_params = 4
col_path = 5

res = []
with open("/home/pjotr/Downloads/function_stats.csv", "r") as f:
    for line in csv.reader(f.readlines()[6:]):
        if len(res) > 0 and res[len(res)-1]["path"] == line[col_path]:
            res[len(res)-1]["end"] = line[col_line]
        if line[col_name]!="<anonymous>" or line[col_params] != "0": continue
        res.append({
            "path": line[col_path],
            "fn_name": line[col_name],
            "line": line[col_line], 
            "length": line[col_length], 
        })

# print(len(res))

items = []
for item in res:
    path = "../websites/" + item["path"][16:]

    try:
        with open(path, "r") as f:
            lines = []
            i = 0
            a = 1
            indents = None
            for line in f.readlines():
                if i >= int(item["line"])-1:
                    if indents is None: indents = 0
                    if indents >= 0:
                        indents += sum([int(c == "{") for c in line])
                        indents -= sum([int(c == "}") for c in line])
                        if indents >= 0:
                            lines.append(line)
                    else:
                        break
                    a += 1
                i += 1
            
            end = 1+lines[len(lines)-1].index("}")
            if end > 0:
                lines[len(lines)-1] = lines[len(lines)-1][:end]
            temp = "".join(lines)
            item["content"] = "var testFunc = " + temp[temp.index("function"):]
            items.append(item)
            # item["content"] = "".join()
        # print(item["content"])
    except:
        pass

template = """
<html>
<head>
<script>
%s
</script>
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
i = 0
frames=[]
for item in items:
    # print(json.dumps(item, indent=2))
    html = template % (item["content"], "testFunc")
    with open("tests_anon/%d.html" % i, "w") as f: f.writelines([html])
    frames.append("tests_anon/%d.html" % i)
    i+=1
    # break

# import json
# with open("res2.json", "w") as f:
#     f.writelines([json.dumps(res)])

# template = """
# <html>
# <head>
# <script src="../../websites/%s"></script>
# </head>
# <body>
# <div id="res">Failed</div>
# <script>
# let failed = true;
# try {
#     %s();
#     failed = false;
# } catch (e) {
#     failed = true;
# }

# document.getElementById("res").innerHTML = failed ? "Failed" : "Ok";
# </script>
# </body>
# </html>
# """

# # res

# frames = []
# i = 0
# for item in res:
#     path = item["path"][16:]
#     fn_name = item["fn_name"]
#     html = template % (path, fn_name)
#     with open("tests/%d.html" % i, "w") as f: f.writelines([html])
#     frames.append("tests/%d.html" % i)
#     i += 1


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
    //console.log(url);
    //if (url == "tests/638.html") url = items.pop();
    iframe.setAttribute("src", url);
    console.log(1 - (items.length / total), url);
    if (items.length > 0) {
        iframe.onload = function() {
            var iframe = document.getElementById("iframe");
            var innerDoc = iframe.contentDocument || iframe.contentWindow.document;
            data[items.length] = innerDoc.getElementById("res").innerHTML;
            if (items.length > 0) {
                loadNextItem();
            } else {
                console.log(JSON.stringify(data));
                let ok = 0;
                let failed = 0
                for (let k in data) {
                    if (data[k] == "Ok") {
                        ok++;
                    }else{
                        failed++;
                    }
                }
                console.log({"ok":ok,"failed":failed});
            }
        };
    }
}
loadNextItem();


</script>
</body>
</html>
"""
print(html % (json.dumps(frames)))
# with open("test_all_anon.html", "w") as f:
#     f.writelines([html])