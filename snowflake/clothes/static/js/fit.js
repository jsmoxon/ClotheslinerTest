function calcDiff(ref, comp)
{
	var nutCupping = nutCup(ref, comp);
	
	return nutCupping;
}

function nutCup(ref, comp)
{
	var riseFactor = riseSum(ref, comp);
	var waistFactor = waist(ref, comp);
	var totalFactor = riseFactor + waistFactor;
	return totalFactor;
}

function riseSum(ref, comp)
{
	return (ref["front_rise"] + ref["back_rise"])-(comp["front_rise"] + comp["back_rise"]);
}

function waist(ref, comp)
{
	return ref["waist"]-comp["waist"];
}