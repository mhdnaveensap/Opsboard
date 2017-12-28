// This second function is for submitting the form inside the modal and handling validation

 $(function () {

     $("#create_task").click(function () {
        // alert("hi")
         $.ajax({
             type: 'POST',
             url: '/taskmaster/',
             data: $("form").serialize(),

             success: function (data, status) {
                    if (data['stat'] == "ok")
                    {
                      Materialize.toast('Task Created Successfully', 3000, 'rounded')
                      // $("#task_create").trigger("reset");
                      // $("#myDIV").delay( 2000 ).slideToggle(1500);
                      // $("#tab").slideToggle(1500);

                    }
                    else {
                      Materialize.toast('Task Creation Failed.Please check all the field', 3000, 'rounded')
                    }
             }
         });
     });
   });


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
                        Materialize.toast('Task Created Successfully', 3000, 'rounded')
                        // $("#task_create").trigger("reset");
                        // $("#myDIV").delay( 2000 ).slideToggle(1500);
                        // $("#tab").slideToggle(1500);

                      }
                      else {
                        Materialize.toast('Task Creation Failed.Please check all the field', 3000, 'rounded')
                      }
               }
           });
       });
     });
