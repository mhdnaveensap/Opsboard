// This function is for showing the modal
 $(function () {

     $(".add_category_show_button").click(function () {
         $.ajax({
             type: 'GET',
             url: '/taskmaster/new/',
             data: $("form").serialize(),
             cache: false,
             success: function (data, status) {
                 $('#add_category_modal_id').html(data);
                 $('#add_category_modal_id').modal()
             }
         });
     }); });

// This second function is for submitting the form inside the modal and handling validation

 $(function () {

     $(".add_category_submit_button").click(function () {
         $.ajax({
             type: 'POST',
             url: '/taskmaster/new/',
             data: $("form").serialize(),
             cache: false,
             success: function (data, status) {
                 if (data['stat'] == "ok") {
                     $('#add_category_modal_id').modal('hide');
                     $('#add_category_modal_id').children().remove();
                     $('#id_category')
                         .append($("<option></option>")
                             .attr("value", data['new_itemcategory_key'])
                             .text(data['new_itemcategory_value']))
                         .val(data['new_itemcategory_key']);
                 }
                 else {
                     $('#add_category_modal_id').html(data);
                     $('#add_category_modal_id').modal('show');
                 }
             }
         });
     }); });
