/* Lazy Load XT 1.1.0 | MIT License */ ! function(t, r, e, s) {
    var n, a, c = t.lazyLoadXT,
        o = /^\s*(\S*)/,
        d = /\S\s+(\d+)w/,
        u = /\S\s+(\d+)h/,
        l = /\S\s+([\d\.]+)x/,
        x = [0, 1 / 0],
        w = [0, 1],
        h = {
            srcsetAttr: "data-srcset",
            srcsetExtended: !0,
            srcsetBaseAttr: "data-srcset-base",
            srcsetExtAttr: "data-srcset-ext"
        },
        f = {
            w: 0,
            h: 0,
            x: 0
        };
    for (n in h) void 0 === c[n] && (c[n] = h[n]);

    function p(r, e) {
        return Math[e].apply(null, t.map(r, function(t) {
            return t[n]
        }))
    }

    function A(t) {
        return t[n] >= f[n] || t[n] === a
    }

    function m(t) {
        return t[n] === a
    }

    function g(s) {
        var i = s.attr(c.srcsetAttr);
        if (!i) return !1;
        var h = t.map(i.replace(/(\s[\d.]+[whx]),/g, "$1 @,@ ").split(" @,@ "), function(t) {
            return {
                url: o.exec(t)[1],
                w: parseFloat((d.exec(t) || x)[1]),
                h: parseFloat((u.exec(t) || x)[1]),
                x: parseFloat((l.exec(t) || w)[1])
            }
        });
        if (!h.length) return !1;
        var g, v, y = e.documentElement;
        for (g in f = {
                w: r.innerWidth || y.clientWidth,
                h: r.innerHeight || y.clientHeight,
                x: r.devicePixelRatio || 1
            }) n = g, a = p(h, "max"), h = t.grep(h, A);
        for (g in f) n = g, a = p(h, "min"), h = t.grep(h, m);
        return v = h[0].url, c.srcsetExtended && (v = (s.attr(c.srcsetBaseAttr) || "") + v + (s.attr(c.srcsetExtAttr) || "")), v
    }
    c.selector += ",img[" + c.srcsetAttr + "],source[" + c.srcsetAttr + "]", t(e).on("lazyshow", "img", function(t, r) {
        var e = r.attr(c.srcsetAttr);
    }), t(e).on("lazyshow", "source", function(r, e) {
        t(this).removeClass("lazy-hidden");
        var s = e.attr(c.srcsetAttr);
    })
}(window.jQuery || window.Zepto || window.$, window, document);