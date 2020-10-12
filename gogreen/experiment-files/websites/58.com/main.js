function foo(b) {
    var a = ".58.com.cn portal.58.com faw-vw-dasweltauto.58.com 5858.com lieche.58.com dict.58.com/xiaoqu about.58.com m.58.com/city.html lieche.m.58.com".split(" "),
        d;
    for (d in a)
        if (-1 !== b.indexOf(a[d])) return "YES";
    return "NO"
}