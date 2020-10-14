var jQuery = {"ajaxSetup":()=>{}};
var _xsrf = "";
var cookieValue = "";
var shortlinks =  [];

function getHash(shortLink) {
    return shortLink.split("/").pop();
}

function getShortLink(hash) {
    var shortlink;
    for (var i = 0; i < shortlinks.length; i++) {
        if (getHash(shortlinks[i]) === hash) {
            shortlink = shortlinks[i];
        }
    }
    return shortlink;
}