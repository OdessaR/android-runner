function getHostName(r) {
    if (r) {
        var e = r.match(/^(?:https?:|ftps?:)?(?:\/\/)?([^\/\?]+[.]+[\w]+[:\w]*)/i);
        return null != e && e.length > 1 && "string" == typeof e[1] && e[1].length > 0 ? {
            origin: e[0],
            host: e[1]
        } : null
    }
}