function validateRange(toDate, fromDate) {
    var t = new Date(toDate),
        f = new Date(fromDate),
        range = (t <= f) ? true : false;
    return range;
}