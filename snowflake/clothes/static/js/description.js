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
	ref = p[$('div#reference_pant').attr('title')]
	comp = p[$('div#comp_pant_1').attr('title')]
	var specify = specialSauce[val.id];
	var explanation = "<li>"+lessSpecialSauce[val.id]+"</li>";
	var parts = moreSpecialSauce[val.id].split(" ");
	for(var i=0;i<parts.length;i++)
	{
		if ((ref[parts[i]]-comp[parts[i]]) == 0) {explanation += "<li>"+otherSpecialSauce[parts[i]]["zero"]+"</li>";}
		else if ((ref[parts[i]]-comp[parts[i]]) > 0) {explanation += "<li>"+otherSpecialSauce[parts[i]]["positive"]+"</li>";}
		else if ((ref[parts[i]]-comp[parts[i]]) < 0) {explanation += "<li>"+otherSpecialSauce[parts[i]]["negative"]+"</li>";}
		else {specificDescription += "<li>you messed up somewhere</li>";}
	}
	
	if (val.title == 0) {explanation += "<li>"+specify["zero"]+"</li>";}
	else if (val.title > 0) {explanation += "<li>"+specify["positive"]+"</li>";}
	else if (val.title < 0) {explanation += "<li>"+specify["negative"]+"</li>";}
	else {specificDescription += "<li>you messed up somewhere</li>";}
	$('div#explain').html(explanation);
}