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

        $('#aBtn1').attr("disabled", true);
        $('#uBtn_'+parid).attr('disabled', true);
        $('#dBtn_'+parid).attr('disabled', true);

        $('#newParameterForm').modal('toggle');

        $.ajax({
            type: 'GET',
            url: "/parameters/create/?name="+encodeURIComponent(name)+
                 "&isnumber="+encodeURIComponent(isnumber)+
                 "&value="+encodeURIComponent(value)+
                 "&desc="+encodeURIComponent(desc)+
                 "&action="+encodeURIComponent(action)+
                 "&parameter="+encodeURIComponent(parid),
                 success: function (response) {
                    if (action == "add"){
                        $('#partable > tbody:last-child').append(`<tr id="parid_${response['id']}"></tr>`);
                        $('#parid_'+response['id']).append(`<td id="parname_${response['id']}">${response['name']}</td>
                                                           <td id="parvalue_${response['id']}">${response['value']}</td>
                                                           <td id="pardesc_${response['id']}">${response['desc']}</td>
                                                           <td><button id="uBtn_${response['id']}" class="btn btn-primary" onclick="editParameter('${response['id']}')">Editar</button>
                                                               <button id="dBtn_${response['id']}" class="btn btn-danger" onclick="delParameter('${response['id']}')">Eliminar</button>
                                                           </td>`);
                            
                        $("#parid_0").remove();
                    } else if (action == "edit"){
                        $("#parname_"+parid).html(response['location']);
                        $("#parvalue_"+parid).html(response['name']);
                        $("#pardesc_"+parid).html(response['desc']);
                        action = "add";
                    }

                    $('#aBtn1').attr("disabled", false);
                    $('#uBtn_'+parid).attr('disabled', false);
                    $('#dBtn_'+parid).attr('disabled', false);

                    clearForm();
                }
        });
    }
}

function clearForm(){
    $("#id_name").val("");
    $("#id_value").val("");
    $("#id_desc").val("");
}