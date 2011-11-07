function calcDiff(ref, comp)
{
	var nutCupping = nutCup(ref, comp);
	var legTightness = legFit(ref, comp);
	var buttCupping = buttCup(ref, comp);
	var diaperButt = diaper(comp, buttCupping);
	var muffinTop = muffin(ref, comp);
	var thighTightness = thigh(ref, comp); 
	var ankleTightness = ankle(ref, comp);

	return '<p onclick=explainThis(this) id="nutcupping" title="'+nutCupping+'">'+compThem(nutCupping, "nutcupping")+'</p>'+
		   '<p onclick=explainThis(this) id="leg" title="'+legTightness+'">'+compThem(legTightness, "leg")+'</p>'+
		   '<p onclick=explainThis(this) id="buttcupping" title="'+buttCupping+'">'+compThem(buttCupping, "buttcupping")+'</p>'+
		   '<p onclick=explainThis(this) id="muffintop" title="'+muffinTop+'">'+compThem(muffinTop, "muffintop")+'</p>'+
		   '<p onclick=explainThis(this) id="thigh" title="'+thighTightness+'">'+compThem(thighTightness, "thigh")+'</p>'+
		   '<p onclick=explainThis(this) id="ankle" title="'+ankleTightness+'">'+compThem(ankleTightness, "ankle")+'</p>';
}

function thigh(ref, comp)
{
	return ref["thigh"] - comp["thigh"];
}

function ankle(ref, comp)
{
	return ref["cuff"] - comp["cuff"];
}

function muffin(ref, comp)
{
	return ref["front_rise"] - comp["front_rise"];
}

function diaper(pant, buttCupping)
{
	var excessThreshold = 1;
	var seamThreshold = .25;
	if (buttCupping > excessThreshold)
	{
		if (seamRatio(pant) > seamThreshold)
		{
			return 1;
		}
	}
	return 0;
}

function seamRatio(pant)
{
	return pant["outseam"]/pant["inseam"];
}

function buttCup(ref, comp)
{
	var revCup = ref["back_rise"]/riseSum(ref);
	var compCup = comp["back_rise"]/riseSum(comp);
	var cuppingFactor = revCup-compCup;
	return cuppingFactor;
}

function nutCup(ref, comp)
{
	var riseFactor = riseSum(ref)-riseSum(comp);
	var waistFactor = ref["waist"]-comp["waist"];
	var totalFactor = riseFactor + waistFactor;
	return totalFactor;
}

function riseSum(pant)
{
	return pant["front_rise"] + pant["back_rise"]; 
}

function legFit(ref, comp)
{
	var refOpening = leg(ref)/body(ref);
	var compOpening = leg(comp)/body(comp);
	var openingFactor = refOpening-compOpening;
	return openingFactor
}

function leg(pant)
{
	return pant["cuff"]+pant["knee"]+pant["thigh"];
}

function body(pant)
{
	return pant["waist"] + riseSum(pant) + pant["outseam"];
}