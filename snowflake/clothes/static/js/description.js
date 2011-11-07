function compThem(val, key)
{
	var usage = sauce[key];
	if (val == 0) {return usage["zero"];}
	else if (val > 0)
	{
		for (var bound in usage["positive"])
			{if (val <= bound) {return usage['positive'][bound];}}
	}
	else if (val < 0)
	{
		for (var bound in usage['negative'])
			{if (Math.abs(val) <= bound) {return usage['negative'][bound];}}
	}
	else {return "you messed up somewhere";}
}

function explainThis(val)
{
	var generalDescription = lessSpecialSauce[val.id];
	var specify = specialSauce[val.id];
	var specificDescription;
	if (val.title == 0) {specificDescription = specify["zero"];}
	else if (val.title > 0) {specificDescription = specify["positive"];}
	else if (val.title < 0) {specificDescription = specify["negative"];}
	else {specificDescription = "you messed up somewhere";}
	$('div#explain').html("<p>"+generalDescription+"</p><p>"+specificDescription+"</p>");
}