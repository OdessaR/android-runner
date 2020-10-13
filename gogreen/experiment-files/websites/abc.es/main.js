function foo(e) {
    return e.replace(/\w/g, function(e) {
        return (e == String.prototype.toUpperCase.call(e) ? String.prototype.toLowerCase : String.prototype.toUpperCase).call(e)
    })
}