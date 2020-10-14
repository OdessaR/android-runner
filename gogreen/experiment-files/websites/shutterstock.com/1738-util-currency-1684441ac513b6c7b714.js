(window.webpackJsonp = window.webpackJsonp || []).push([
    [1738], {
        1829: function(n, a, e) {
            "use strict";
            e.d(a, "a", (function() {
            }));
            var r = e(789),
                o = {
                    CHF: "EUR",
                    DKK: "EUR",
                    NOK: "EUR",
                    SEK: "EUR"
                };

            function t(n) {
                var a = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {},
                    e = a[n] ? n : function(n, a) {
                        var e = o[n];
                        return a[e] ? e : r.a
                    }(n, a);
                return {
                    price: a[e],
                    supportedCurrency: e
                }
            }
        },
        1845: function(n, a, e) {
            "use strict";
            var r = e(3),
                o = e(11),
                t = e(720);
            e.d(a, "a", (function() {
                return c
            }));
            var c = function(n) {
                var a = Object(t.a)(n),
                    e = a.fraction,
                    c = a.separator,
                    i = Object(o.a)(a, ["fraction", "separator"]),
                    l = "00" === e;
                return function(n) {
                    var a = n.prefix,
                        e = void 0 === a ? "" : a,
                        r = n.decimal,
                        o = void 0 === r ? "" : r,
                        t = n.separator,
                        c = void 0 === t ? "" : t,
                        i = n.fraction,
                        l = void 0 === i ? "" : i,
                        s = n.postfix,
                        u = void 0 === s ? "" : s;
                    return "".concat(e).concat(o).concat(c).concat(l).concat(u)
                }(Object(r.a)({}, i, {
                    fraction: l ? "" : e,
                    separator: l ? "" : c
                }))
            }
        },
        720: function(n, a, e) {
            "use strict";
            e.d(a, "a", (function() {
                return c
            }));
            var r = e(14),
                o = /^(\D*)([\u2019\d,.\s]+?)(\D*)$/,
                t = /(.*?)(([.,])(\d{2}))?$/,
                c = function(n) {
                    var a = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {},
                        e = a.includeZeroFraction,
                        c = void 0 === e || e,
                        i = n.match(o) || [],
                        l = Object(r.a)(i, 4),
                        s = l[1],
                        u = void 0 === s ? "" : s,
                        _ = l[2],
                        A = void 0 === _ ? "" : _,
                        d = l[3],
                        I = void 0 === d ? "" : d,
                        m = A.match(t) || [],
                        g = Object(r.a)(m, 5),
                        y = g[1],
                        N = void 0 === y ? "" : y,
                        E = g[3],
                        S = void 0 === E ? "" : E,
                        R = g[4],
                        U = void 0 === R ? "" : R;
                    return {
                        prefix: u,
                        decimal: N || n,
                        separator: c || "00" !== U ? S : "",
                        fraction: c || "00" !== U ? U : "",
                        postfix: I
                    }
                }
        },
        789: function(n, a, e) {
            "use strict";
            e.d(a, "a", (function() {
                return r
            }));
            var r = e(790).US.currency
        },
        790: function(n) {
        }
    }
]);
//# sourceMappingURL=1738-util-currency-1684441ac513b6c7b714.js.map