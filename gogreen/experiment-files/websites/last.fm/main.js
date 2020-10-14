function comma(t) {
    if (void 0 !== t) {
        var e = t.toString().split(".");
        console.log(e);
        return e[0] = e[0].replace(/\B(?=(\d{3})+(?!\d))/g, ","), e.join(".")
    }
    return ""
}