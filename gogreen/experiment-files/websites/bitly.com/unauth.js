var jQuery = {"ajaxSetup":()=>{}};
var _xsrf = "";
var cookieValue = "";
var shortlinks =  []
function getFriendlyError(code) {
    var errorCode = code || 'DEFAULT';

    var messages = {
        'RATE_LIMIT_EXCEEDED': 'Whoa - you\'ve exceeded your quota. Create a free account to keep shortening.',
        'INVALID_ARG_URL': 'Unable to shorten that link. It is not a valid url.',
        'ALREADY_A_BITLY_LINK': 'That is already a Bitly link',
        'MISSING_ARG_URL': 'Please, provide a valid url',
        'UNKNOWN_ERROR': 'Woops. Something went wrong. Please try again.',
        'DEFAULT': 'An error occurred'
    };

    return messages[errorCode];
}