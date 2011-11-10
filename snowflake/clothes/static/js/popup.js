var cart = new Array();

function popupForm(sel, token) 
{
	var newForm = document.createElement("FORM");
	if (typeof sel === 'undefined') {newForm.action="/p4tt/super_compare/";}
	else {newForm.action="/p4tt/super_compare/"+sel+"/";}
	newForm.method="post";
	newForm.onsubmit="popupThis(this)";
	
	var csrfToken = document.createElement("INPUT");
	csrfToken.name = "csrfmiddlewaretoken";
	csrfToken.type = "hidden";
	csrfToken.value = token;
	
	var fRoom = document.createElement("INPUT");
	fRoom.name = "fitRoom";
	fRoom.type = "hidden";
	fRoom.value = cart;
	
	newForm.appendChild(fRoom);
	newForm.appendChild(csrfToken);
	popupThis(newForm);
}

function popupThis(form)
{
	window.open('', "Compare Pants", "status=0, height=1500, width=1100");
	form.target = "Compare Pants";
	form.submit();
}