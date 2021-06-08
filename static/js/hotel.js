function sort(x) {
    if (typeof(Storage) !== "undefined") {
        var y = "hotel_";
        var z = y + x;

        var a = document.getElementById(z).innerHTML;

        sessionStorage.setItem("nme", a);
    } else {
        document.getElementById("myID").innerHTML =
            "The browser does not support Web Storage.";
    }
}

document.getElementById("tryID").innerHTML= sessionStorage.getItem("nme");
