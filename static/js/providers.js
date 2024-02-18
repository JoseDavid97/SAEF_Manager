var action = "add";
var prid = "0";
var clid = "0";

function addProvider(){
    const name = $("#id_name").val();
    const client = $("#id_client").val();
    const webacc = $("#id_webacc").val();

    if (name.length == 0){
        $('#name_alert').show();
    } else if (webacc.length == 0){
        $('#name_alert').hide();
        $('#webacc_alert').show();
    } else {
        $('#aBtn1').attr("disabled", true);
        $('#uBtn_'+prid).attr('disabled', true);
        $('#dBtn_'+prid).attr('disabled', true);
        $('#newProviderForm').modal('toggle');
        $('#name_alert').hide();
        $('#webacc_alert').hide();

        $.ajax({
            type: 'GET',
            url: "/providers/create/?name="+encodeURIComponent(name)+
                 "&client="+encodeURIComponent(client)+
                 "&webaccess="+encodeURIComponent(webacc)+
                 "&action="+encodeURIComponent(action)+
                 "&provider="+encodeURIComponent(prid),
                 success: function (response) {
                    if (action == "add"){
                        $('#prtable > tbody:last-child').append(`<tr id="prid_${response['id']}"></tr>`);
                        $('#prid_'+response['id']).append(`<td id="prname_${response['id']}">${response['name']}</td>
                                                           <td id="prclient_${response['id']}">${response['clt_name']}</td>
                                                           <td id="prwebacc_${response['id']}">${response['webacc']}</td>
                                                           <td><button id="uBtn_${response['id']}" class="btn btn-primary" onclick="editProvider('${response['id']}')">Editar</button>
                                                               <button id="dBtn_${response['id']}" class="btn btn-danger" onclick="delProvider('${response['id']}')">Eliminar</button>
                                                           </td>`);
                            
                        $("#prid_0").remove();
                    } else if (action == "edit"){
                        $("#prname_"+prid).html(response['name']);
                        $("#prclient_"+prid).html(response['clt_name']);
                        $("#prwebacc_"+prid).html(response['webacc']);
                        action = "add";
                    }
                    clid = response["clt_id"];
                    
                    $('#aBtn1').attr("disabled", false);
                    $('#uBtn_'+prid).attr('disabled', false);
                    $('#dBtn_'+prid).attr('disabled', false);
                    $('#aBtn2').attr("disabled", true);
                    
                    clearForm()
                }
        });
    }
}

function editProvider(pr_id){
    action = "edit";
    prid = pr_id;
    $('#aBtn2').attr("disabled", false);
    $.ajax({
        type: 'GET',
        url: "/providers/detail/?provider="+pr_id,
             success: function (response) {
                if ($('#id_client option[value='+response["clt_id"]+']').length == 0){
                    $('#id_client').append(`<option id="clop_${response["clt_id"]}" value="${response["clt_id"]}">${response["clt_name"]}</option>`);
                    clid = response["clt_id"];
                }

                $('#newProviderForm').modal('toggle');
                $("#id_name").val(response["name"]);
                $("#id_client").val(response["clt_id"]);
                $("#id_webacc").val(response["webacc"]);
            }
    });
}

function delProvider(pr_id){
    const result = prompt("Si elimina el proveedor se eliminará toda información asociada, para continuar escriba \"ELIMINAR\"", "");
    
    if (result == "ELIMINAR"){
        $('#uBtn_'+pr_id).attr('disabled', true);
        $('#dBtn_'+pr_id).attr('disabled', true);
        $.ajax({
            type: 'GET',
            url: "/providers/delete/?provider="+pr_id,
            success: function (response) {
                $("#prid_"+pr_id).remove();
                $('#id_client').append(`<option id="clop_${response["clt_id"]}" value="${response["clt_id"]}">${response["clt_name"]}</option>`);

                if ($('#prtable tbody tr').length == 0){
                    $('#prtable > tbody:last-child').append(`<tr id="prid_0"><td colspan="3">Sin Proveedores</td></tr>`);
                }
            }
        });
    }
}

function clearForm(){
    $('#aBtn2').attr("disabled", true);
    $("#clop_"+clid).remove();
    $("#id_name").val("");
    $("#id_client").val("0");
    $("#id_webacc").val("");
}