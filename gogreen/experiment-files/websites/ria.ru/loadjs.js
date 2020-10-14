(function(d) {
    var c = function(c, a, e) {
        var f, g = d.document.getElementsByTagName("script")[0],
            b = d.document.createElement("script");
        b.src = c;
        b.async = !e;
        g.parentNode.insertBefore(b, g);
        a && "function" === typeof a && (b.onload = a);
        return b
    };
})("undefined" !== typeof global ? global : this);