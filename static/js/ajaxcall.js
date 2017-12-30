$(document).ready(function(){
    var $myForm = $('#task_create')
    $myForm.submit(function(){
        event.preventDefault()
        var $formData = $(this).serialize()
        var $thisURL = $myForm.attr('data-url') || window.location.href // or set your own url
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })
    })
    
    function handleFormSuccess(data, textStatus, jqXHR){
        Materialize.toast(data['message'], 3000, 'rounded')
    }

    function handleFormError(jqXHR, textStatus, errorThrown){
      var result = jQuery.parseJSON(jqXHR.responseText);
          for (var key in result)
          {
              key = key.replace('_',' ')
              var $toastContent = $('<span>Please enter the required field</span>').add($('<p class="btn-flat toast-action">'+ key +'</p>'));
              Materialize.toast($toastContent,8000, 'rounded' );
          }
    }
})
