$("#btn_show").click(function(){
    $("#myDIV").slideToggle(1500);
    $("#tab").slideToggle(1500);
});
$("#btn_close").click(function(){
    $("#myDIV").slideToggle(1500);
    $("#tab").slideToggle(1500);
});


 $(function () {
     $("#create_task").click(function () {
       // alert('hi')
         $.ajax({
             type: 'POST',
             url: '/Task/',
             data: $("form").serialize(),

             success: function (data, status) {
                    if (data['stat'] == "ok")
                    {
                      Materialize.toast('Task Created Successfully', 3000, 'rounded')
                    }
                    else {
                      Materialize.toast('Task Creation Failed.Please check all the field', 3000, 'rounded')
                    }
             }
         });
     });
   });
