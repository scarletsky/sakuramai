(function ($) {

$(document).ready(function() {

  $('[data-dna]').mouseover(function(e) {
    var $elem = $(this);
    var dna = $elem.data('dna');
    $('#dna').attr('class', 'p' + dna);
  });

  $('#form-success.modal')
    .modal('attach events', '#team-form.modal #team-submit.button');

  $('#form-fail.modal')
    .modal('attach events', '#single-form.modal #single-submit.button');

  $('#click-me-to-signup').click(function(e) {
    e.preventDefault();
    $('#team-form.modal').modal('show');
  });

  $('#single-link').click(function(e) {
    e.preventDefault();
    $('#single-form.modal').modal('show');
  });

  $('#team-link').click(function(e) {
    e.preventDefault();
    $('#team-form.modal').modal('show');
  });

});
} (jQuery));
