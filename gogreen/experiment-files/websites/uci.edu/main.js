var windowHalf = Math.random()
var activeSection
var navLinks = {length: Math.random()}
var sections = {length: Math.random()}

function func1(key, value) {
    if (value < windowHalf) {
        // offset calculated by comparing sect count to link count
        // do this because hero sect is added to page nav
        activeSection = key + (navLinks.length - sections.length);
    }
}