$(function () {
  $(".upd_cmd").click(function () {

    var taskid = $(this).attr("value");
    var row = $(this).closest('tr');
    var cmdtext = row.find('.mycmdbox').val();
    $(this).closest('tr').children('td.cmd_old').text(cmdtext);
    $.get('/mytaskcmd/', {tskid: taskid,cmd_text:cmdtext}, function(data){
          $('#modal1').modal('close');
          Materialize.toast(data['status'], 3000, 'rounded');
     });

  });
});
