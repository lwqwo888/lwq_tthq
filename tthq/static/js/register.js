$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;

	// 用户名
	$('#user_name').blur(function() {
		check_user_name();
	});
	// 密码
	$('#pwd').blur(function() {
		check_pwd();
	});
	// 再次输入密码
	$('#cpwd').blur(function() {
		check_cpwd();
	});
	// 邮箱
	$('#email').blur(function() {
		check_email();
	});
	// 同意使用协议
	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名');
			$('#user_name').next().show();
			error_name = true;
        }
		else
		{
            // 定义一个变量接收用户输入的账户名
            // var juname = $('#user_name').val();

            // 定义一个字典,键为juname,juname是js里面的user_name的意思
            // 从字典里取出值拼接到/jason/后面传递到后台再用get方法获取出来.

            // ajax方法一.
			// $.get('/jason/',{'jason':juname},function (data) {

			// console.log('222222222');
            // ajax方法二.拼接url
            $.get("/jason/?jason="+$('#user_name').val(),function (data) {
				// 传到ajax的返回值是object对象
            	console.log(typeof(data));
				// 从data中使用count取值是int
				console.log(data.count);
				// 因为模型类查询结果是字典,所以data.count,提取键'count'所对应的值
				if (data.count==1) // 如果后台查询结果传回的字典值不是0就说明被注册过
				{
					console.log('6666666');
                	$('#user_name').next().html('用户名已存在,请重新输入或登录');
                	$('#user_name').next().show();
                	error_name = true;
            	}
            	else
				{
                    $('#user_name').next().hide();
                    error_name = false;
                }
            });

		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;

		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});



})