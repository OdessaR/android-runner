function code(a) {
    try {
        return decodeURI(a);
    } catch (b) {
        return false;
    }
}