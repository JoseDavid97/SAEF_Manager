
function editEvents(provider, action){

    $.ajax({
        type: 'GET',
        url: "/locations/get_events/?provider="+provider+
                                    "&action="+action,
             success: function (response) {
                $('#actionModalForm').modal('toggle');
                console.log(response);
            }
    });
}

function clearForm(){

}

function addAction(){
    
}