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
	else {return "Sorry, data not available";}
}

function explainThis(val)
{
	ref = p[$('div#reference_pant').attr('title')]
	comp = p[$('div#comp_pant_1').attr('title')]
	var specify = specialSauce[val.id];
	var explanation = "<p>"+lessSpecialSauce[val.id]+"</p>";
	var parts = moreSpecialSauce[val.id].split(" ");
	for(var i=0;i<parts.length;i++)
	{
		if ((ref[parts[i]]-comp[parts[i]]) == 0) {explanation += "<p>"+otherSpecialSauce[parts[i]]["zero"]+"</p>";}
		else if ((ref[parts[i]]-comp[parts[i]]) > 0) {explanation += "<p>"+otherSpecialSauce[parts[i]]["positive"]+"</p>";}
		else if ((ref[parts[i]]-comp[parts[i]]) < 0) {explanation += "<p>"+otherSpecialSauce[parts[i]]["negative"]+"</p>";}
		else {specificDescription += "<p>An error happened.</p>";}
	}
	
//	if (val.title == 0) {explanation += "<li>"+specify["zero"]+"</li>";}
//	else if (val.title > 0) {explanation += "<li>"+specify["positive"]+"</li>";}
//	else if (val.title < 0) {explanation += "<li>"+specify["negative"]+"</li>";}
//	else {specificDescription += "<li>you messed up somewhere</li>";}
	$('div#explain').html(explanation);
}