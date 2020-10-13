function removeFromArray(e, r) {
    var o = e.indexOf(r);
    o >= 0 && e.splice(o, 1);
    return e
}