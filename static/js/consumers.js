var action = "add";
var mtid = "0";

function addMeter(){
    const location = $("#id_location").val();
    const name = $("#id_name").val();
    const url = $("#id_url").val();

    if (location == null){
        $('#location_alert').show();
    } else if (name.length == 0) {
        $('#location_alert').hide();
        $('#name_alert').show();
    } else if (location == null){
        $('#location_alert').hide();
        $('#name_alert').hide();
        $('#url_alert').show();
    } else {
        $('#aBtn1').attr("disabled", true);
        $('#uBtn_'+mtid).attr('disabled', true);
        $('#dBtn_'+mtid).attr('disabled', true);

        $('#newMeterForm').modal('toggle');

        $('#location_alert').hide();
        $('#name_alert').hide();
        $('#url_alert').hide();

        $.ajax({
            type: 'GET',
            url: "/meters/create/?location="+encodeURIComponent(location)+
                 "&name="+encodeURIComponent(name)+
                 "&url="+encodeURIComponent(url)+
                 "&action="+encodeURIComponent(action)+
                 "&meter="+encodeURIComponent(mtid),
                 success: function (response) {
                    if (action == "add"){
                        console.log(response);
                        $('#metable > tbody:last-child').append(`<tr id="mtid_${response['id']}"></tr>`);
                        $('#mtid_'+response['id']).append(`<td id="mtloc_${response['id']}">${response['location']}</td>
                                                           <td id="mtname_${response['id']}">${response['name']}</td>
                                                           <td><button id="uBtn_${response['id']}" class="btn btn-primary" onclick="editLocation('${response['id']}')">Editar</button>
                                                               <button id="dBtn_${response['id']}" class="btn btn-danger" onclick="delLocation('${response['id']}')">Eliminar</button>
                                                           </td>`);
                            
                        $("#mtid_0").remove();
                    } else if (action == "edit"){
                        $("#mtloc_"+mtid).html(response['location']);
                        $("#mtname_"+mtid).html(response['name']);
                        action = "add";
                    }

                    $('#aBtn1').attr("disabled", false);
                    $('#uBtn_'+mtid).attr('disabled', false);
                    $('#dBtn_'+mtid).attr('disabled', false);

                    clearForm();
                }
        });
    }
}

function editMeter(mt_id){
    action = "edit";
    mtid = mt_id;
    $.ajax({
        type: 'GET',
        url: "/meters/detail/?meter="+mt_id,
             success: function (response) {
                $('#newMeterForm').modal('toggle');
                $("#id_location").val(response['location']);
                $("#id_name").val(response['name']);
                $("#id_url").val(response['url']);
            }
    });
}

function delMeter(mt_id){
    const result = prompt("Si elimina el medidor se eliminará toda información asociada, para continuar escriba \"ELIMINAR\"", "");
    
    if (result == "ELIMINAR"){
        $('#uBtn_'+mt_id).attr('disabled', true);
        $('#dBtn_'+mt_id).attr('disabled', true);
        $.ajax({
            type: 'GET',
            url: "/meters/delete/?meter="+mt_id,
            success: function (response) {
                $("#mtid_"+mt_id).remove();

                if ($('#mttable tbody tr').length == 0){
                    $('#mttable > tbody:last-child').append(`<tr id="mtid_0"><td colspan="3">Sin medidores</td></tr>`);
                }
            }
        });
    }
}

function clearForm(){
    $("#id_location").val(0);
    $("#id_name").val("");
    $("#id_url").val("");
}