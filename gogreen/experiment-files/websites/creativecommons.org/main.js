function arrayAverage(array) {
    var sum = 0;
    for (var i = 0; i < array.length; i++) {
        sum += array[i];
    }
    return array.length > 0 ? sum / array.length : 0;
}