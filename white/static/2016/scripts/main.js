(function($) {

  var checkInput = function(fields) {
    var input;
    var len = fields.length;
    for (var i = 0; i < len; i++) {
      input = fields.eq(i).val();
      if (!input || !$.trim(input)) {
        return false;
      }
    }
    return true;
  };

  var checkAuthor = function(fields, type) {
    var data = {};
    if (type === 'single') {
      data.author1 = $.trim(fields.val());
      data.type = 'single';
    } else if (type === 'team') {
      data.author1 = $.trim(fields.eq(0).val());
      data.author2 = $.trim(fields.eq(1).val());
      data.type = 'team';
    }

    $.post('/check-author-ajax/', data, function(isSigned) {
      if (isSigned == 'True') {
        var formSelector = '#' + type + '-form';
        $(formSelector + ' .ui.dimmer')
          .dimmer({
            onShow: function() {
              $(formSelector + ' #dimmer-title').text('热地板说你（们）已经报过名了！');
            }
          })
          .dimmer('show');
      }
    });
  };

  var checkNum = function(field) {
    var pairNum = Number(field.val());
    var re = /^[0-9]{1}$/;
    if (re.test(pairNum) === false) {
      return false;
    }
    return true;
  };

  var getData = function(fields, type) {
    var name, val;
    var data = {
      type: type
    };
    fields.each(function() {
      name = $(this).attr('name');
      val = $.trim($(this).val());
      data[name] = val;
    });

    return data;
  };

  $(document).ready(function() {

    $('.cover-outer').click(function(e) {
      var video = $(this).children('.video');
      video.addClass('show');
      $('#overlay').show();

      return e.preventDefault();
    });

    $('#overlay').click(function(e) {
      $('.video.show').removeClass('show');
      $(this).hide();

      return e.preventDefault();
    });

    $('.vote').click(function(e) {
      var data = {};
      var teamNum = $.trim($(this).data('team-num'));
      var limitDay = $.trim($(this).data('vote-limit-day'));

      data['year'] = new Date().getFullYear();
      data['team_num'] = teamNum;
      data['vote_limit_day'] = limitDay;

      $('#modal-vote').modal('show');

      $.post('/vote-ajax/', data, function(ret) {

        $('#modal-text').removeClass();
        $('#modal-text').addClass('circle icon');
        switch (ret) {
          case '1':
            $('#modal-text').addClass('warning');
            $('#modal-text').text('投票结束');
            break;
          case '2':
            $('#modal-text').addClass('warning');
            $('#modal-text').text('你已经投过票了');
            break;
          default:
            $('#modal-text').addClass('check');
            $('#modal-text').text('感谢投票');
        }

        $('#modal-vote').modal('show');
      });

      return e.preventDefault();
    });

    var initSingleForm = function() {
      $('#single-form.modal')
        .modal({
          onApprove: function($elem) {
            var fields = $('#single-form input');

            if (!checkInput(fields)) {
              $('#single-form .ui.dimmer')
                .dimmer({
                  onShow: function() {
                    $('#single-form #dimmer-title').text('热地板说不能有空字段');
                  }
                })
                .dimmer('show');
              return false;
            }

            if (!checkNum($('#pair-num'))) {
              $('#single-form .ui.dimmer')
                .dimmer({
                  onShow: function() {
                    $('#single-form #dimmer-title').text('热地板规定配对号要填0~9');
                  }
                })
                .dimmer('show');
              return false;
            }

            $('#single-form .form').addClass('loading');
            $elem.addClass('loading');

            var data = getData(fields, 'single');

            $.post('/signup-ajax/', data)
              .then(function(res) {
                if (res == '1') {
                  $('#form-success.modal').modal('show');
                } else {
                  $('#form-fail.modal').modal('show');
                }

                $('#single-form .form').removeClass('loading');
                $elem.removeClass('loading');
                $('input:not([type="hidden"])').val('');
              }, function(err) {
                $('#single-form .form').removeClass('loading');
                $elem.removeClass('loading');
                $('#error').modal('show');
              });
          }
        })
        .modal('show');
    }

    var initTeamForm = function() {
      $('#team-form.modal')
        .modal({
          onApprove: function($elem) {
            var fields = $('#team-form input');

            if (!checkInput(fields)) {
              $('#team-form .ui.dimmer')
                .dimmer({
                  onShow: function() {
                    $('#team-form #dimmer-title').text('热地板说不能有空字段');
                  }
                })
                .dimmer('show');
              return false;
            }

            $('#team-form .form').addClass('loading');
            $elem.addClass('loading');

            var data = getData(fields, 'team');

            $.post('/signup-ajax/', data)
              .then(function(res) {
                if (res == '1') {
                  $('#form-success.modal').modal('show');
                } else {
                  $('#form-fail.modal').modal('show');
                }

                $('#team-form .form').removeClass('loading');
                $elem.removeClass('loading');
                $('input:not([type="hidden"])').val('');
              }, function(err) {
                $('#team-form .form').removeClass('loading');
                $elem.removeClass('loading');
                $('#error').modal('show');
              });
          }
        })
        .modal('show');
    }

    var initSignupEndModal = function() {
      $('#signup-end').modal('show');
    };

    $('[data-dna]').mouseover(function(e) {
      var $elem = $(this);
      var dna = $elem.data('dna');
      $('#dna').attr('class', 'p' + dna);
    });

    $('#single-form #author1').blur(function(e) {
      e.preventDefault();
      checkAuthor($('#single-form #author1'), 'single');
    });

    $('#team-form #author1, #team-form #author2').blur(function(e) {
      e.preventDefault();
      checkAuthor($('#team-form #author1, #team-form #author2'), 'team');
    });

    $('#click-me-to-signup, #signup-link').click(function(e) {
      e.preventDefault();
      initSignupEndModal();
      // $('#signup-entry.ui.modal')
      //     .modal({
      //         onApprove: function() {initSingleForm();},
      //         onDeny: function() {initTeamForm();}
      //     })
      //     .modal('show');
    });

    $('#single-link').click(function(e) {
      e.preventDefault();
      initSignupEndModal();
      // initSingleForm();
    });

    $('#team-link').click(function(e) {
      e.preventDefault();
      initSignupEndModal();
      // initTeamForm();
    });

  });
}(jQuery));
