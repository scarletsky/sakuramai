(function ($) {

  /* 

  var checkInput = function (fields) {
    var input;
    var len = fields.length;
    for (var i = 0; i < len; i++) {
      input = fields.eq(i).val();
      if (! input || ! $.trim(input)) {
        alert('有空字段，自寻死路啊');
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
        alert('该用户已经报名刷热地板了！');
        return false;
      }
    });
    return true;
  };

  var checkNum = function (field) {
    var pairNum = Number(field.val());
    var re = /^[0-9]{1}$/;
    if (re.test(pairNum) === false) {
      alert('女王规定要填0~9');
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
  */

  $(document).ready(function () {
    $('.js-vote').click(function (e) {
      var data = {};
      var teamNum = $.trim($(this).data('team-num'));
      var limitDay = $.trim($(this).data('vote-limit-day'));

      data['year'] = 2014;
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
          alert('感谢投票')
        }

      });

      return e.preventDefault();
    });

    /*
    $('#index-cover').click(function () {
      $(this).hide();
      $('#queen').show();
      sessionStorage.hideCover = true;
    });

    $('#queen').hide();

    $('.author').blur(function () {
      checkAuthor($(this), 'single');
    });

    $('.pair-num').blur(function () {
      checkNum($(this));
    });


    $('button#single').click(function (e) {
      var data;
      var fields = $('form#single input');
      if (checkInput(fields) &&
          checkNum($('.pair-num'))) {
        $(this).attr('disabled', 'true');
        data = getData(fields, 'single');
        $.post('/signup-ajax/', data, function (res) {
          if (res == '1') {
            $('#singleForm').modal('hide');
            $('#formSuccess').modal('show');
          } else {
            $('#singleForm').modal('hide');
            $('#formFailure').modal('show');
          }
        });
      }
      return e.preventDefault();
    });

    $('button#team').click(function (e) {
      var data;
      var fields = $('form#team input');
      if (checkInput(fields)) {
        $(this).attr('disabled', 'true');
        data = getData(fields, 'team');
        $.post('/signup-ajax/', data, function (res) {
          if (res == '1') {
            $('#teamForm').modal('hide');
            $('#formSuccess').modal('show');
          } else {
            $('#teamForm').modal('hide');
            $('#formFailure').modal('show');
          }
        });
      }
      return e.preventDefault();
    });

    $('#signup-single-btn').click(function () {
      $('#forHotfloor').modal('hide');
      $('#singleForm').modal('show');
    });

    $('#signup-team-btn').click(function () {
      $('#forHotfloor').modal('hide');
      $('#teamForm').modal('show');
    });

    */

 });
} (jQuery));
