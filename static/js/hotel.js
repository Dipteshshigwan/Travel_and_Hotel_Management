// function sort(x) {
//     if (typeof(Storage) !== "undefined") {
//         var y = "hotel_";
//         var z = y + x;

//         var a = document.getElementById(z).innerHTML;

//         sessionStorage.setItem("nme", a);
//     } else {
//         document.getElementById("myID").innerHTML =
//             "The browser does not support Web Storage.";
//     }
// }

// document.getElementById("tryID").innerHTML= sessionStorage.getItem("nme");

function plan(a){
    var b = "plan_";
    var c = b + a;

    var bb = "planname_";
    var d = bb + a;

    var y = document.getElementById(d).innerHTML;
    var x = document.getElementById(c).innerHTML;
    
    sessionStorage.setItem("p_name", y);
    sessionStorage.setItem("amount", x);
}
document.getElementById("plan_name").innerHTML= sessionStorage.getItem("p_name");
document.getElementById("plan_amount").innerHTML= sessionStorage.getItem("amount");

document.getElementById("plan_amount_2").innerHTML= sessionStorage.getItem("amount");

// document.getElementById("plan_amount_2").innerHTML= sessionStorage.getItem("amount");
// document.getElementById("plan_name_2").innerHTML= sessionStorage.getItem("p_name");




