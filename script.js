function toggle() {
    var sums = document.getElementsByClassName("sum");
    var control = document.getElementById("control");
    if (sums[0].style.display === "none") {
        var i;
        for (i = 0; i < sums.length; i++) {
            sums[i].style.display = "table-cell";
        }
        control.innerHTML = "Verstecke Kontrolle";
    } else {
        var i;
        for (i = 0; i < sums.length; i++) {
            sums[i].style.display = "none";
        }
        control.innerHTML = "Zeige Kontrolle";
    }
}