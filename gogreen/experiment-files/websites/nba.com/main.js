function gender(val) {
    var gender;

    if (val) {
        switch (val.toLowerCase()) {
            case "m":
            case "male":
                gender = "M";
                break;
            case "f":
            case "female":
                gender = "F";
                break;
            default:
                gender = "O";
        };
        return gender;
    } else {
        return undefined;
    }
}