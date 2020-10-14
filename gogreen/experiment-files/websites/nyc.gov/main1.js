function getCurrentDate(range) {


    var m_names = new Array("January", "February", "March",
        "April", "May", "June", "July", "August", "September",
        "October", "November", "December");

    var now = new Date(),
        day = now.getDate() + range,
        today = '';

    /*if (self.iOS) {
      month = (now.getMonth() + 1);
      
      if (month < 10)
        month = "0" + month;

      if (day < 10)
        day = "0" + day;

      month = (m_names[now.getMonth()]).slice(0, 3);
      //today = now.getFullYear() + '-' + month + '-' + day;
      today = month +' '+ day + ', '+ now.getFullYear();
      console.log("ios date: " + today);
    } else {*/
    //}

    return today;
}