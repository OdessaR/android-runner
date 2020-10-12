from glob import glob
import os


for path in glob(os.path.sep.join(["experiment-files", "normalExec", "*"])):
    with open(path, "r") as f:
        print(path + " -> ", end="", flush=True)
        lines = []
        fn_line = False
        fn_name = ""
        experiment_element_start = False
        memo_lib_start = False
        for line in f.readlines():
            if line.strip() == "<body>":
                lines.append(line)
                memo_lib_start = True
                continue

            if line.strip() == "<script type=\"text/javascript\">":
                experiment_element_start = True
                lines.append(line)
                continue

            if line.strip().startswith("// memo"):
                fn_line = True
                lines.append(line)
                continue

            if memo_lib_start:
                lines.append("    <!-- memoization lib -->\n")
                lines.append("    <script src=\"../lib/memoization.js\"></script>\n")
            if fn_line:
                fn_name = line.split("(")[0].strip()
                line = line[:line.index(fn_name)] + "memoFunc" + line[line.index(fn_name) + len(fn_name):]
            
            if experiment_element_start:
                lines.append(None)

            lines.append(line)
            fn_line = False
            experiment_element_start = False
            memo_lib_start = False

        i = 0
        for line in lines:
            if line is None: lines[i] = "\n".join(["        /* ==> CONF: MEMOIZE FUNCTION */", "        const memoFunc = memoizer(%s);\n" % fn_name])
            i += 1
        
        path_parts = os.path.splitext(os.path.basename(path))
        new_name = "memoized%s%s%s" %  (path_parts[0][0].upper(), path_parts[0][1:], path_parts[1])
        if path_parts[0].lower().startswith("normal"):
            new_name = "memoized%s%s%s" % (path_parts[0][6].upper(), path_parts[0][7:], path_parts[1])

        with open(os.path.sep.join(["experiment-files", "memoizedExec", new_name]), "w") as f: f.writelines(lines)
        print(os.path.sep.join(["experiment-files", "memoizedExec", new_name]), flush=True)
