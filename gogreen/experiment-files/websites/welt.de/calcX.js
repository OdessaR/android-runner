var ASCDP = window.ASCDP || {};
ASCDP.adS = ASCDP.adS || {}, ASCDP.adS.calcX = function(e, t) {
    try {
        var a = t ? parseInt(t) : 0,
            d = e.offsetParent && "BODY" !== e.parentNode.tagName ? e.offsetParent : e.parentNode;
    } catch (e) {}
};