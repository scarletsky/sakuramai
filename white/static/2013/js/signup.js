    $(document).ready(function(){
      $("#single_save").click(function(){
        var author0 = document.getElementById("id_author0").value;
        var contact0 = document.getElementById("id_contact0").value;
        var remark0 = document.getElementById("id_remark0").value;
        var pair_num = document.getElementById("id_pair_num").value;
        var post_data_single = {'author0':author0, 'contact0':contact0, 
                    'remark0':remark0, 'pair_num':pair_num, 'is_team':0}
        $.post("/signup/", post_data_single, 
          function(ret){
            if(ret==0){ alert("网络错误，请重试！"); }
            else if(ret==1){ alert("感谢参与！我们期待着你的作品哦！"); location=location; }
            else if(ret==2){ alert("你已经报过名了！赶快去填坑！"); }
            else if(ret==3){ alert("别提交空字段啊混蛋！"); }
            else if(ret==4){ alert("配对号填错了！地板女王要发怒了！") }
          });
      });


      $("#single_cancel").click(function(){
        $("#SingleForm").modal('hide');
      });


      $("#team_save").click(function(){
        var author1 = document.getElementById("id_author1").value;
        var contact1 = document.getElementById("id_contact1").value;
        var remark1 = document.getElementById("id_remark1").value;

        var author2 = document.getElementById("id_author2").value;
        var contact2 = document.getElementById("id_contact2").value;
        var remark2 = document.getElementById("id_remark2").value;
        var post_data_team = {'author1':author1, "contact1":contact1, "remark1":remark1, 
              "author2":author2, "contact2":contact2, "remark2":remark2, "is_team":1}
        $.post("/signup/", post_data_team, 
          function(ret){
            if(ret==0){ alert("网络错误，请重试！"); }
            else if(ret==1){ alert("感谢参与！我们期待着你们爱的结晶！"); location=location; }
            else if(ret==2){ alert("你被你机油坑了！他已经和其他人基上了！"); }
            else if(ret==3){ alert("别提交空字段啊混蛋！"); }
          });
      });
      $("#team_cancel").click(function(){
        $("#TeamForm").modal('hide');
      });
    });