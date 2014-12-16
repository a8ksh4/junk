$(function() {
	$('.error').hide();
	$('imput.text-imput').css({backgroundColor:"#FFFFFF"});
	$('input.text-input').focus(function(){
		$(this).css({backgroundColor:"#FFDDAA"});
	});
	$('input.text-input').blur(function(){
		$(this).css({backgroundColor:"#FFFFFF"});
	});

	$(".button").click(function() {
	//Validate and process form here
	
	$('.error').hide();
	
		var name = $("input#name").val();
	  		if (name == "") {
		$("label#name_error").show();
		$("input#name").focus();
	  	return false;
	}
		var name = $("input#email").val();
	  		if (email == "") {
	 	$("label#email_error").show();
	 	$("input#email").focus();
	  	return false;
	}
		var character = $("input#character").val();
	  		if (character == "") {
	 	$("label#character_error").show();
	 	$("input#character").focus();
	  	return false;
	} 
	
			var dataString = 'name='+ name + '&email=' + email + '&character=' + character;


			$.ajax({
			type: "POST",
			url: "/ui/user.py",
			data: dataString,
			success: function() {
				$('#contact_form').html("div id='message'></div>");
				$('#message').html("<h2>Account Created!</h2>")
				.append("<p>Welcome to Web Game Thingy</p>")
			.hide()
			.fadeIn(1500, function() {
				$('#message').append("<img id='checkmark' src='images/check.png' />");
			});
		}
	});
	return false;
	});
});
runOnLoad(function(){
	$("input#name").select().focus();
});

