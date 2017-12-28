$('#basicinfo').click(function(){
    $('#basicinfo').addClass("tab_on");
    $('#basicinfo').removeClass("tab_off");
    $('#passchange').addClass("tab_off");
    $('#passchange').removeClass("tab_on");

});

$('#passchange').click(function(){
  $('#passchange').addClass("tab_on");
  $('#passchange').removeClass("tab_off");
  $('#basicinfo').addClass("tab_off");
  $('#basicinfo').removeClass("tab_on");
});

$('#btn_editinfo').click(function() {
  editinfo();
});

function editinfo()
{
  $('#btn_editinfo').fadeOut(800);
  $('#btn_saveinfo').delay(800).fadeIn(800);
  $('#id_first_name').prop('disabled', false);
  $('#id_last_name').prop('disabled', false);
  $('#id_email').prop('disabled', false);
};
