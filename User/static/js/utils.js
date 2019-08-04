let is_null = (list) => {
    let bandera = true;
    list.forEach(function(element) {
        element.removeClass("is-invalid");
        element.addClass(element.val() == "" ? "is-invalid" : "");
        bandera = element.val() == "" ? false : true;
    });
    return bandera;
}

let is_null_string = (list) => {
    let bandera = true;
    list.forEach(function(element) {
        bandera = element == "" ? false : true;
    });
    return bandera
}