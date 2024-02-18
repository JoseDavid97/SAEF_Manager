var action = "add";
var parid = "0";

function addParameter(){
    const name = $("#id_name").val();
    const isnumber = $("#id_isnumber").val();
    const value = $("#id_value").val();
    const desc = $("#id_desc").val();

    if (name.length == 0){
        $('#name_alert').show();
    } else if (value.length == 0) {
        $('#name_alert').hide();
        $('#value_alert').show();
    } else if (desc.length == 0) {
        $('#name_alert').hide();
        $('#value_alert').hide();
        $('#desc_alert').show();
    } else {
        $('#name_alert').hide();
        $('#value_alert').hide();
        $('#desc_alert').hide();
    }
}

function clearForm(){
    $("#id_name").val("");
    $("#id_value").val("");
    $("#id_desc").val("");
}