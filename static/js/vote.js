    function Vote(obj){
      document.getElementById('layer').style.display = "inline";
      var r = confirm("你认为这组同步吗？");
      if (r==true){
        var team_num = $(obj).attr("team_num");
        var day = $(obj).attr("day");
        var post_data = {"team_num":team_num, "day":day};
        $.post("/2013/", post_data, function(ret){
          if (ret==0){
            alert("感谢你的投票！");
          }
          else{
            alert("你已经投过票了!");
          };
        });
        document.getElementById('layer').style.display = "none";
      }
      else{
        document.getElementById('layer').style.display = "none";
      }
      return 0;
    };


    function EndVote(){
      alert('投票结束～');
      return 0;
    }

