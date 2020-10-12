function cmp(v1, v2) {
    if (!v1 || !v2) {
        return +!!v1 - +!!v2;
    }
    var _v1 = ('' + v1).split('.'),
        _v2 = ('' + v2).split('.'),
        i;
    for (i = 0; i < _v1.length && i < _v2.length && +_v1[i] == +_v2[i]; i++);
    if (_v1.length == i || _v2.length == i)
        return _v1.length - _v2.length;
    return +_v1[i] - +_v2[i];
};