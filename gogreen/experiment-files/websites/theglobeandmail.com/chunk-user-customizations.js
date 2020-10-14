(window.webpackJsonp = window.webpackJsonp || []).push([
    [41], {
        j80x: function(e, t, n) {
            "use strict";
            n.r(t), n.d(t, "parseAnonymousUserData", (function() {
            })), n.d(t, "parseRegisteredUserData", (function() {
            })), n.d(t, "parseCommonUserData", (function() {
            })), n.d(t, "determineAnonymousUserFeatures", (function() {
            })), n.d(t, "determineRegisteredUserFeatures", (function() {
            })), n.d(t, "default", (function() {
            }));
            var a, r, c, i = n("SgV1"),
                s = n("vr7q"),
                o = n("E42y"),
                u = n("QGZC"),
                l = n("dSFn"),
                f = "[USER-CUSTOMIZATIONS-HOME]";

            function d(e) {
                if (u.a.info("".concat(f, " Parse anonymous user data"), e), e.Features) {
                    var t = Object.values(e.Features),
                        n = t.length;
                    return {
                        sectionGroups: t.reduce((function(e, t) {
                            return t.TimestampFeatures && Object.keys(t.TimestampFeatures).forEach((function(n) {
                                var a = t.TimestampFeatures[n].ArticleSectionCount;
                                a && Object.keys(a).length && e.push(a)
                            })), e
                        }), []),
                        intervals: n
                    }
                }
            }

            function h(e) {
                u.a.info("".concat(f, " Parse registered user data"), e);
                var t = 0;
                return {
                    sectionGroups: e.reduce((function(e, n) {
                        return n.weeklyFeatures && Object.values(n.weeklyFeatures).forEach((function(n) {
                            var a = Object(l.i)(n, "deviceFeatures.Computer.articleSectionCount", {});
                            a && Object.keys(a).length && (e.push(a), t = ++t)
                        })), e
                    }), []),
                    intervals: t
                }
            }

            function m(e) {
                var t = e.sectionGroups,
                    n = e.intervals;
                u.a.info("".concat(f, " parseCommonUserData:"), t, n);
                var a, r = 0,
                    c = 0;
                if (!t.length) return {
                    articlesPerInterval: c,
                    robArticlesPercent: r
                };
                var i = {},
                    s = 0,
                    o = 0,
                    l = 0;
                return t.forEach((function(e) {
                    Object.keys(e).forEach((function(t) {
                        var n = e[t];
                        i[t] = (i[t] || 0) + n, s += n, "business" === t || "investor" === t || "investing" === t ? o += n : l += n
                    }))
                })), r = o / s * 100, a = l / s * 100, c = s / n, u.a.info("".concat(f, " Parsed data:"), {
                    sectionGroups: t,
                    intervals: n,
                    articlesRead: s,
                    articlesBySection: i,
                    articlesPerInterval: c,
                    robArticles: o,
                    robArticlesPercent: r,
                    otherArticles: l,
                    otherArticlesPercent: a
                }), {
                    articlesPerInterval: c,
                    robArticlesPercent: r
                }
            }

            function k(e) {
                var t = e.articlesPerInterval,
                    n = e.robArticlesPercent,
                    a = t,
                    r = [];
                return u.a.info("".concat(f, " determineAnonymousUserFeatures:"), {
                    articlesPerDay: a,
                    robArticlesPercent: n
                }), a > 1 ? n > 10 ? (u.a.info("".concat(f, " Heavy Financial Plus user")), r.push("marketTicker", "financialSearch", "latestNews")) : n < 2 ? (u.a.info("".concat(f, " Heavy non-business user")), r.push("latestNews")) : (u.a.info("".concat(f, " Heavy multi-faceted user")), r.push("marketTickerCollapsed", "latestNews")) : u.a.info("".concat(f, " Light user")), r
            }

            function v(e) {
                var t = e.articlesPerInterval,
                    n = e.robArticlesPercent,
                    a = t,
                    r = [];
                return u.a.info("".concat(f, " determineRegisteredUserFeatures:"), {
                    articlesPerWeek: a,
                    robArticlesPercent: n
                }), a > 4 ? n > 40 ? (u.a.info("".concat(f, " Heavy Financial Plus user")), r.push("marketTicker", "financialSearch", "latestNews")) : n < 5 ? (u.a.info("".concat(f, " Heavy non-business user")), r.push("latestNews")) : (u.a.info("".concat(f, " Heavy multi-faceted user")), r.push("marketTickerCollapsed", "latestNews")) : u.a.info("".concat(f, " Light user")), r
            }

            function p(e) {
                u.a.error("".concat(f, " API error"), e), b(["marketTicker", "financialSearch", "latestNews"])
            }

            function b() {
                var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : [];
                u.a.info("".concat(f, " Show:"), e), e.includes("marketTicker") || e.includes("marketTickerCollapsed") ? (u.a.info("".concat(f, " Show: marketTicker")), a && a.classList.remove("u-hidden")) : u.a.info("".concat(f, " Hide: marketTicker (remains hidden)")), e.includes("marketTickerCollapsed") && w(), e.includes("financialSearch") || (u.a.info("".concat(f, " Hide: financialSearch")), r && r.classList.add("u-hidden")), e.includes("latestNews") || (u.a.info("".concat(f, " Hide: latestNews")), c && c.classList.add("u-hidden"))
            }

            function w() {
                if (u.a.info("".concat(f, " Collapse market ticker")), a) {
                    var e = Object(l.z)(".c-market-ticker", a);
                    e && (e.classList.add("c-market-ticker--collapsed"), e.classList.add("c-market-ticker--collapsed-with-arrows"))
                }
            }

            function y(e) {
                u.a.info("".concat(f, " Init")), a = e, r = Object(l.z)("#secondary-promo-area-1 .pb-f-global-financial-search"), c = Object(l.z)("#tertiary-news-area .c-package--story-list--basic");
                var t = new Date,
                    n = t.getMonth() + 1,
                    w = t.getFullYear(),
                    y = n < 10 ? "0".concat(n.toString() + w.toString()) : n.toString() + w.toString(),
                    g = Object(l.i)(i.a, "datalayer.identity.guid", null),
                    P = Object(o.o)();
                if (Object(o.r)()) {
                    u.a.info("".concat(f, " Registered user"));
                    var S = "".concat(s.k, "/?hashId=").concat(g, "&monthYear=").concat(y, "&numberOfMonths=").concat(3);
                    fetch(S).then((function(e) {
                        return e.json()
                    })).then(h).then(m).then(v).then(b).catch((function(e) {
                        return p(e)
                    }))
                } else if (null !== P && "" !== P) {
                    u.a.info("".concat(f, " Anonymous user"));
                    var O = "".concat(s.d, "/?sophiId=").concat(P, "&monthYear=").concat(y, "&numberOfMonths=").concat(3);
                    fetch(O).then((function(e) {
                        return e.json()
                    })).then(d).then(m).then(k).then(b).catch((function(e) {
                        return p(e)
                    }))
                } else u.a.info("".concat(f, " Unknown user")), b(["marketTickerCollapsed", "financialSearch", "latestNews"])
            }
        }
    }
]);
//# sourceMappingURL=chunk-user-customizations.5a004c88f90f787f648f.min.js.map