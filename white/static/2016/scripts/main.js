(function ($) {
$(document).ready(function() {

  $('[data-dna]').mouseover(function(e) {
    var $elem = $(this);
    var dna = $elem.data('dna');
    $('#dna').attr('class', 'p' + dna);
  });

});
} (jQuery));
