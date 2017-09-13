/**
 * Created by python on 17-9-13.
 */
$('#user_name').blur(function() {
    check_user_name();
});

function check_user_name(){
    // duname是数据库里的用户名,如果和用户输入的相同,提示已被注册.

    // 定义一个字典,键为juname,juname是js里面的user_name的意思
    // 从字典里取出值拼接到/jason/后面传递到后台再用get方法获取出来.
    // 定义一个变量接收用户输入的账户名
    var juname = $('#user_name').val();

    $.get('/jason/',{'jason':juname},function (data) {
        if (data)
        {
            $('#user_name').next().html('用户名已存在,请重新输入或登录')
            $('#user_name').next().show();
        }
        else
            $('#user_name').next().hide();
    });

    // error_name = false;

	}