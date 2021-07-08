window.onload = function(){
    insert();
}

// function rewrite(){//重置合同内容
//     document.getElementById("blog_title").value="";
//     document.getElementById("blog_content").value="";
// }

function insert(){
        let data = {};
        data['username']="崔玉真";
        data['gender']="女";
        data['phone']="18301511616";
        data['id_card']="18301108";

        $.ajax({
    　　　　  url: 'http://127.0.0.1:5000/insert_OldPerson', 　
    　　　　  type: 'GET', 　　　　　　　　
    　　　　  data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(id)
            {　　　
                alert("信息插入成功！");
                },
            error: function(XMLHttpRequest, textStatus)
            {
                alert(XMLHttpRequest.status);
                // 如果有错误抛出异常
                alert(XMLHttpRequest.readyState);
                alert(textStatus);
                }
        });
    }

// function get_for_draft(){
//     $.ajax({
// 　　　　   url : 'http://127.0.0.1:5000/get_now_username', 　
// 　　　　   type : 'post',　　　　　　　　
// 　　　　   dataType : 'json',
// 　　　   　success:function(name_index){　　　<!--回调函数 -->
//            save_draft(name_index);
// 　　　　  }
// 　　　});
// }
//
// function opeartor_role(){
//     $.ajax({
// 　　　　   url : 'http://127.0.0.1:5000/opeartor_role', 　
// 　　　　   type : 'post',　　　　　　　　
// 　　　　   dataType : 'json',
// 　　　   　success:function(data_role){　　　<!--回调函数 -->
//                alert(data_role[0]['Draftcontract']);
// 　　　　  }
// 　　　});
// }

