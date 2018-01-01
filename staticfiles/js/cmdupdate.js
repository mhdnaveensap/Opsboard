$(function () {
  $(".upd_cmd").click(function () {

    var taskid = $(this).attr("value");
    var row = $(this).closest('tr');
    var cmdtext = row.find('.mycmdbox').val();
    var status = row.find('input:radio[name="status"]:checked').attr("value");
    var taskque = row.find('input:radio[name="taskqueue"]:checked').attr("value");
    $(this).closest('tr').children('td.cmd_old').text(cmdtext);
    if (taskque == "Yes")
    {
      row.hide();
    }


    $.get('/mytaskcmd/', {tskid: taskid,cmd_text:cmdtext,statusnm:status,task_que:taskque}, function(data){
          $('#modal1').modal('close');
          Materialize.toast(data['status'], 8000, 'rounded');
     });

  });
});
