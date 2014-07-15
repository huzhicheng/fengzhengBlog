function validate_user(uname,upassword){
	$.ajax({
		type:"post",
		url:"/fengzhengusercheck",
		data:{"Username":uname,"Password":upassword},
		success:function(result){
			var obj = JSON.parse(result);
			if(obj.success=="ok"){
				window.location.href = "/fengzhengadmin";
			}
		},
		error:function(a,b,c){
			alert(a+b+c);
		}
	})
}

function logout(){
	window.location.href = "/fengzhenglogout";
}
