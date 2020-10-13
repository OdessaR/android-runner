    function g(n) {
        var r, t = [];
        for (t[(n.length >> 2) - 1] = void 0, r = 0; r < t.length; r += 1) t[r] = 0;
        var u = 8 * n.length;
        for (r = 0; r < u; r += 8) t[r >> 5] |= (255 & n.charCodeAt(r / 8)) << r % 32;
        return t
    }