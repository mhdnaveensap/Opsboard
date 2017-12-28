$(document).ready(function(){
          pullcommand();
});

// This Script will pull the command from command table with the condition to task id
function pullcommand(){
  var task_id = ($('#taskid').attr("for"))
  var url = "/command/"+task_id;

  $.get(url, function(data)
    {
      $('#command_div').html(data);
    });
}

$(function () {

  $("#btn_add_cmd").click(function () {

      var task_id = ($('#taskid').attr("for"))
      var url = "/command/"+task_id;
      $.ajax({
          type: 'POST',
          url: url,
          data:$("#update_form").serialize(),

          success: function (data,status) {
                 if (data['stat'] == "ok")
                 {
                   Materialize.toast('Your Comment is saved.. ', 3000, 'rounded')
                   pullcommand();
                 }
                 else {
                   Materialize.toast('Your Comment is save field !!', 3000, 'rounded')
                 }
          }
      });
  });
  });

// This second function is for submitting the form inside the modal and handling validation


   $(function () {
       $("#update_task").click(function () {
           var url = window.location.pathname+"/update";
           console.log(url);
           $.ajax({
               type: 'POST',
               url: url,
               data:$("form").serialize(),

               success: function (data,status) {
                      if (data['stat'] == "ok")
                      {
                        Materialize.toast('Task updated Successfully', 3000, 'rounded')
                      }
                      else {
                        Materialize.toast('Task update Failed.Please check all the field', 3000, 'rounded')
                      }
               }
           });
       });
     });
