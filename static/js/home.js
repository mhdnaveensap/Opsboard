$(document).ready(function(){

  // Initialize collapse button
   $('.button-collapse').sideNav();
  //Initialize collapsible (uncomment the line below if you use the dropdown variation)
  $('.collapsible').collapsible();

        // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
        $('.modal').modal();
        $('select').material_select();
        $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        format: 'mm/dd/yyyy',
        closeOnSelect: false // Close upon selecting a date,
      });
  });
