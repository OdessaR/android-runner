c = {
    primary: "newHomeButton--primary",
    secondary: "newHomeButton--secondary",
    terciery: "newHomeButton--terciery"
}

function validator(t) {
    return -1 !== Object.keys(c).indexOf(t)
}