var cart = new Array();

function popupForm(sel, token) 
{
var urlpk;
	var newForm = document.createElement("form");
	if (typeof sel === 'undefined') {
		urlpk ="/p4tt/super_compare/";
		newForm.action="/p4tt/super_compare/";
		}
		
	else {
		urlpk="/p4tt/super_compare/"+sel+"/"; 
		newForm.action="/p4tt/super_compare/"+sel+"/";
		}
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
	popupThis(newForm, urlpk);

}


function popupThis(form, url)
{
	//alert("foo"); //for debugging; tells us that the JS doesn't fail prior to this
	console.log("cart: "+cart); //for debugging; this records (to Console) how many pants get added
	window.open(url, "Compare Pants", "status=0, height=1500, width=1100");
	//window.open('', "", "");
	form.target = "Compare Pants";
	form.submit();
}