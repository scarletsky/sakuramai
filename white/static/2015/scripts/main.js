(function ($) {

  var checkInput = function (fields) {
    var input;
    var len = fields.length;
    for (var i = 0; i < len; i++) {
      input = fields.eq(i).val();
      if (! input || ! $.trim(input)) {
        alert('热地板说不能有空字段');
        return false;
      }
    }
    return true;
  };

  var checkAuthor = function (fields, type) {
    var data = {};
    if (type === 'single') {
      data.author1 = $.trim(fields.val());
      data.type = 'single';
    } else if (type === 'team') {
      data.author1 = $.trim(fields.eq(0).val());
      data.author2 = $.trim(fields.eq(1).val());
      data.type = 'team';
    }

    $.post('/check-author-ajax/', data, function (isSigned) {
      if (isSigned == 'True') {
        alert('热地板说你(们)已经报过名了');
        return false;
      }
    });
    return true;
  };

  var checkNum = function (field) {
    var pairNum = Number(field.val());
    var re = /^[0-9]{1}$/;
    if (re.test(pairNum) === false) {
      alert('热地板规定要填0~9');
      return false;
    }
    return true;
  };

  var getData = function (fields, type) {
    var name, val;
    var data = {type: type};
    fields.each(function () {
      name = $(this).attr('name');
      val = $.trim($(this).val());
      data[name] = val;
    });

    return data;
  };
  

  $(document).ready(function () {
    // info 页面
    var pathname = location.pathname;
    $(window).scroll(function (e) {
      var scrollTop = $(document).scrollTop();
      if (scrollTop > 200) {
        $('.guide').addClass('fixed');
      } else {
        $('.guide').removeClass('fixed');
      }
    });

    $('.guide [data-target]').click(function (e) {
      e.preventDefault();

      var target = $(this).data('target');
      $('html, body').animate({
        scrollTop: $(target).offset().top - 20
      }, 500);
    });

    // 播放
    $('.js-show-video').click(function (e) {
      var field = $(this);
      field.next().addClass('show');
      $('#overlay').show();

      return e.preventDefault();
    });

    $('#overlay').click(function (e) {
      var field = $(this);
      $('div.video.show').removeClass('show');
      field.hide();

      return e.preventDefault();
    });

    // 投票
    $('.js-vote').click(function (e) {
      var data = {};
      var teamNum = $.trim($(this).data('team-num'));
      var limitDay = $.trim($(this).data('vote-limit-day'));

      data['year'] = new Date().getFullYear();
      data['team_num'] = teamNum;
      data['vote_limit_day'] = limitDay;


      $.post('/vote-ajax/', data, function (ret) {
        switch (ret) {
        case '1':
          alert('投票结束');
          break;
        case '2':
          alert('你已经投过票了');
          break;
        default:
          alert('感谢投票');
        }
      });

      return e.preventDefault();
    });

    $('.author').blur(function () {
      checkAuthor($(this), 'single');
    });

    $('.pair-num').blur(function () {
      checkNum($(this));
    });


    // $('button#single').click(function (e) {
    //   e.preventDefault();

    //   var data;
    //   var fields = $('form#single input');

    //   if (checkInput(fields) && checkNum($('.pair-num')) ) {
    //     data = getData(fields, 'single');

    //     $(this).attr('disabled', 'true');
    //     $.post('/signup-ajax/', data, function (res) {
    //       if (res == '1') {
    //         $('#singleForm').modal('hide');
    //         $('#formSuccess').modal('show');
    //       } else {
    //         $('#singleForm').modal('hide');
    //         $('#formFailure').modal('show');
    //       }

    //       $('input:not([type="hidden"])').val('');
    //     });
    //   }

    //   return false;
    // });

    // $('button#team').click(function (e) {
    //   e.preventDefault();

    //   var data;
    //   var fields = $('form#team input');

    //   if (checkInput(fields)) {

    //     data = getData(fields, 'team');

    //     if (data['author1'] === data['author2']) {
    //       alert('热地板说必须和机油一起才能报名！');
    //       return;
    //     }

    //     $(this).attr('disabled', 'true');
    //     $.post('/signup-ajax/', data, function (res) {
    //       if (res == '1') {
    //         $('#teamForm').modal('hide');
    //         $('#formSuccess').modal('show');
    //       } else {
    //         $('#teamForm').modal('hide');
    //         $('#formFailure').modal('show');
    //       }

    //       $('input:not([type="hidden"])').val('');
    //     });
    //   }

    //   return false;
    // });

    // $('#signup-single-btn').click(function () {
    //   $('#forHotfloor').modal('hide');
    //   $('#singleForm').modal('show');
    // });

    // $('#signup-team-btn').click(function () {
    //   $('#forHotfloor').modal('hide');
    //   $('#teamForm').modal('show');
    // });

 });
} (jQuery));
