$(function(){

	var error_name = true;
	var error_pwd = true;
	var error_cpwd = true;
	var error_email = true;
	var error_allow = true;

	$('#user_name').blur(function(){
		check_username();
	})

	$('#user_name').focus(function(){
		$(this).next().hide();
	})

	$('#pwd').blur(function(){
		check_pwd();
	})

	$('#pwd').focus(function(){
		$(this).next().hide();
	})

	$('#cpwd').blur(function(){
		check_cpwd();
	})

	$('#cpwd').focus(function(){
		$(this).next().hide();
	})

	$('#email').blur(function(){
		check_email();
	})

	$('#email').focus(function(){
		$(this).next().hide();
	})

	$('#allow').click(function(){
		
		if ($(this).prop('checked')==true) {
			error_allow = false;
			$('.error_tip2').hide();
		}
		else{
			error_allow = true;
			$('.error_tip2').html('请勾选同意协议！').show();
		}
	})

	function check_username(){

		var val = $('#user_name').val();
		var re =/^[\w]{5,15}$/;
		if (val =='') {
			$('#user_name').next().html('用户名不能为空!');
			$('#user_name').next().show();
			error_name = true;
			return;
		}
		if(re.test(val)){
			error_name = false;
		}
		else{
			error_name = true;
			$('#user_name').next().html('用户名是包含数字、字母、下划线的5到15位!');
			$('#user_name').next().show();
		}
	}

	function check_pwd(){

		var val = $('#pwd').val();
		var re =/^[\w\.\$\#\*\+\-\!\&]{6,16}$/;
		if (val =='') {
			$('#pwd').next().html('密码不能为空!');
			$('#pwd').next().show();
			error_pwd = true;
			return;
		}
		if(re.test(val)){
			error_pwd = false;
		}
		else{
			error_pwd = true;
			$('#pwd').next().html('用户名是包含数字、字母、下划线和.+-！#$*&的6到16位!');
			$('#pwd').next().show();
		}
	}

	function check_cpwd(){

		var val = $('#cpwd').val();
		var cval = $('#pwd').val();
		if (val == cval) {
			error_cpwd = false;
		}
		else{
			error_cpwd = true;
			$('#cpwd').next().html('两次输入密码不一致!');
			$('#cpwd').next().show();
		}

	}

	function check_email(){

		var val = $('#email').val();
		var re =/^[\w]{6,12}(@qq\.com$)|(@163\.com$)/i;
		if (val =='') {
			$('#email').next().html('邮箱不能为空!');
			$('#email').next().show();
			error_email = true;
			return;
		}
		if(re.test(val)){
			error_email = false;
		}
		else{
			error_pwd = true;
			$('#email').next().html('邮箱是包含数字、字母、下划线格式为xxx@163/qq.com的6到12位!');
			$('#email').next().show();
		}
	}

	$('.reg_sub').submit(function(){

		if (!(error_name==false&&error_pwd==false&&error_cpwd==false&&error_email==false&&error_allow==false)) {
			return false;
		}
	})

})