$(function () {
  $("#upd_cmd").click(function () {

    var taskid = $(this).attr("value");
    var cmdtext = $('#mycmdbox').val();
    $.get('/mytaskcmd/', {tskid: taskid,cmd_text:cmdtext}, function(data){
          $('#modal1').modal('close');
          Materialize.toast(data['status'], 3000, 'rounded');
          Materialize.toast("Once you refresh this page you can see your comment", 3000, 'rounded');

     });

  });
});
