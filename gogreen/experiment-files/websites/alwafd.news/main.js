function calculateCutOff(len, delta, items) {
    var cutoff = [];
    var cutsum = 0;
    for (var i in items) {
        var item = items[i];
        var fractOfLen = item.twidth / len;
        cutoff[i] = Math.floor(fractOfLen * delta);
        cutsum += cutoff[i];
    }
    var stillToCutOff = delta - cutsum;
    while (stillToCutOff > 0) {
        for (i in cutoff) {
            cutoff[i]++;
            stillToCutOff--;
            if (stillToCutOff == 0) break;
        }
    }
    return cutoff;
};