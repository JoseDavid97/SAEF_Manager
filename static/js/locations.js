var action = "add";
var loid = "0";

function getStates(co_iso_num) {
    $.ajax({
            type: 'GET',
            url: "/locations/get_states/?country="+co_iso_num,
            success: function (response) {
                var states = response["states"];
                $("option[class='state_option']").remove();
                $("option[class='city_option']").remove();
                states.forEach((state) => {
                    $('#id_state').append(`<option class="state_option" value="${state.value}">${state.name}</option>`);
                });
            }
        });
}

function getCities(st_code) {
    $.ajax({
            type: 'GET',
            url: "/locations/get_cities/?state="+st_code,
            success: function (response) {
                var cities = response["cities"];
                $("option[class='city_option']").remove();
                cities.forEach((city) => {
                    $('#id_city').append(`<option class="city_option" value="${city.value}">${city.name}</option>`);
                });
            }
        });
}

function addLocation(){
    const name = $("#id_name").val();
    const address1 = $("#id_address1").val();
    const address2 = $("#id_address2").val();
    const city = $("#id_city").val();

    if (name.length == 0){
        $('#name_alert').show();
    } else if (address1.length == 0) {
        $('#name_alert').hide();
        $('#address_alert').show();
    } else if (city == null) {
        $('#name_alert').hide();
        $('#address_alert').hide();
        $('#city_alert').show();
    } else {
        $('#aBtn1').attr("disabled", true);
        $('#uBtn_'+loid).attr('disabled', true);
        $('#dBtn_'+loid).attr('disabled', true);
        $('#newLocationForm').modal('toggle');
        $('#name_alert').hide();
        $('#address_alert').hide();
        $('#city_alert').hide();

        $.ajax({
            type: 'GET',
            url: "/locations/create/?name="+encodeURIComponent(name)+
                 "&address1="+encodeURIComponent(address1)+
                 "&address2="+encodeURIComponent(address2)+
                 "&city="+encodeURIComponent(city)+
                 "&action="+encodeURIComponent(action)+
                 "&location="+encodeURIComponent(loid),
                 success: function (response) {
                    if (action == "add"){
                        $('#lotable > tbody:last-child').append(`<tr id="loid_${response['id']}"></tr>`);
                        $('#loid_'+response['id']).append(`<td id="loname_${response['id']}">${response['name']}</td>
                                                        <td id="loaddr_${response['id']}">${response['address']}</td>
                                                        <td id="locity_${response['id']}">${response['city']}</td>
                                                        <td><button class="btn btn-primary" onclick="editLocation('${response['id']}')">Editar</button>
                                                            <button id="dBtn_${response['id']}" class="btn btn-danger" onclick="delLocation('${response['id']}')">Eliminar</button>
                                                        </td>`);
                            
                        $("#loid_0").remove();
                    } else if (action == "edit"){
                        $("#loname_"+loid).html(response['name']);
                        $("#loaddr_"+loid).html(response['address']);
                        $("#locity_"+loid).html(response['city']);
                    }
                    action = "add";
                    $('#aBtn1').attr("disabled", false);
                    $('#uBtn_'+loid).attr('disabled', false);
                    $('#dBtn_'+loid).attr('disabled', false);
                }
        });

        $("#id_name").val("");
        $("#id_address1").val("");
        $("#id_address2").val("");
        $("#id_country").val("0");
        $("#id_state").val("0");
        $("#id_city").val("0");
    }

}

function editLocation(lo_id){
    action = "edit";
    loid = lo_id;
    $('#aBtn2').attr("disabled", true);
    $.ajax({
        type: 'GET',
        url: "/locations/detail/?location="+lo_id,
             success: function (response) {
                $('#newLocationForm').modal('toggle');
                $("#id_name").val(response["name"]);
                $("#id_address1").val(response["address1"]);
                $("#id_address2").val(response["address2"]);
                $("#id_country").val(response["country"]);

                getStates(response["country"]);

                function checkStates(){
                    if ($('#id_state > option').length<2){
                        window.setTimeout(checkStates, 200);	
                    } else {
                        $("#id_state").val(response["state"]);
                        getCities(response["state"]);
                        checkCities();
                    }
                }

                function checkCities(){
                    if ($('#id_city > option').length<2){
                        window.setTimeout(checkCities, 200);	
                    } else {
                        $("#id_city").val(response["city"]);
                        $('#aBtn2').attr("disabled", false);
                    }
                }

                checkStates();
            }
    });
}

function delLocation(lo_id){
    const result = prompt("Si elimina la localización se eliminará toda información asociada, para continuar escriba \"ELIMINAR\"", "");
    
    if (result == "ELIMINAR"){
        $('#uBtn_'+lo_id).attr('disabled', true);
        $('#dBtn_'+lo_id).attr('disabled', true);
        $.ajax({
            type: 'GET',
            url: "/locations/delete/?location="+lo_id,
            success: function (response) {
                $("#loid_"+lo_id).remove();

                if ($('#lotable tbody tr').length == 0){
                    $('#lotable > tbody:last-child').append(`<tr id="loid_0"><td colspan="4">Sin localizaciones</td></tr>`);
                }
            }
        });
    }
}