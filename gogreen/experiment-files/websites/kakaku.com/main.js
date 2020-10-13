function EscapeSJIS(str) {
    return str.replace(/[^*+.-9A-Z_a-z-]/g, function(s) {
        var c = s.charCodeAt(0),
            m;
    })
};