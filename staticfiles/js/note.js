$(document).ready(function(){
          pullcommand();
});



// This Script will pull the command from command table with the condition to task id
function pullcommand(){

  var url = "/note_show";

  $.get(url, function(data)
    {
      $('#mydiv').html(data);
    });
}

$(function () {

  $("#add_task").click(function () {

      var url = "/note_update";
      $.ajax({
          type: 'POST',
          url: url,
          data:$("#note_update").serialize(),

          success: function (data,status) {
                 if (data['stat'] == "ok")
                 {
                   Materialize.toast('Your Note is updated.. ', 3000, 'rounded')
                   pullcommand();
                   $('#modal1').modal('close');
                 }
                 else {
                   Materialize.toast('Your Comment is save field !!', 3000, 'rounded')
                 }
          }
      });
  });
  });
