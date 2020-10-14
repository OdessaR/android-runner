var Url = {
    encode: function(r) {
    },
    decode: function(r) {
    },
    _utf8_encode: function(r) {
        for (var e = "", o = 0; o < r.length; o++) {
            var t = r.charCodeAt(o);
            t < 128 ? e += String.fromCharCode(t) : (127 < t && t < 2048 ? e += String.fromCharCode(t >> 6 | 192) : (e += String.fromCharCode(t >> 12 | 224), e += String.fromCharCode(t >> 6 & 63 | 128)), e += String.fromCharCode(63 & t | 128))
        }
        return e
    },
    _utf8_decode: function(r) {
        return e
    }
};