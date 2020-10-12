function isSafeAscii(password) {
    for (var i = 0; i < password.length; i++) {
        if (password.charCodeAt(i) < 32 || password.charCodeAt(i) > 127)
            return false;
    }
    return true;
}