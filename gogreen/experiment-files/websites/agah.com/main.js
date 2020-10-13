function c(d, b, c) {
    for (var a = 0; a < d.length; a += 2) {
        var e = d[a + 1],
            g = c;
        if (25 > Math.abs(d[a] - b) && 25 > Math.abs(e - g)) return d.splice(a, a + 2), !0
    }
    return !1
}