function show_alert() {alert("I am an alert box!");}
function feedbackPopup() {
window.open("/feedback/", "feedbackWindow", "status=1, height = 600, width = 600, resizable = 0")
}


var p = jQuery.parseJSON('{{measurements|escapejs|safe}}');
p.sort();

function sortOptions(sel)
{
	var my_options = $("#"+sel+" option");
	my_options.sort(function(a,b) {
	    if (a.text > b.text) return 1;
	    else if (a.text < b.text) return -1;
	    else return 0
	})
	$("#"+sel).empty().append( my_options );
}

function genDesigners()
{
	var z = document.getElementById("designers");
	for (var key in p)
	{
		var newOption = document.createElement("OPTION");
		newOption.text = key;
		newOption.value = key;
		z.add(newOption, null);
	}
	
	sortOptions("designers");
	genStyles(z);
}

function genStyles(sel)
{
	var z = document.getElementById("styles");
	while(z.length > 0)
	{
	   z.remove(0);
	}
	for (var key in p[sel[sel.selectedIndex].value])
	{
		var newOption = document.createElement("OPTION");
		newOption.text = key;
		newOption.value = key;
		z.add(newOption, null);
	}
	sortOptions("styles");
	genMeasurements(sel, z);
}

function genMeasurements(des, sel)
{
	var z = document.getElementById("measurements");
	while(z.length > 0)
	{
		z.remove(0);
	}
	for (var key in p[des[des.selectedIndex].value][sel[sel.selectedIndex].value])
	{
		var a = p[des[des.selectedIndex].value][sel[sel.selectedIndex].value][key];
		var newOption = document.createElement("OPTION");
		if (a[1] == "0") {a[1] = "Unhemmed"}
		newOption.text = a[0]+' x '+a[1];
		newOption.value = a[0]+' '+a[1]+' '+a[2]+' '+a[3];
		z.add(newOption, null);
	}
}
