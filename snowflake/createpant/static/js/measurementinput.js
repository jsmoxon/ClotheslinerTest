function displayLabelWaist()
{
document.getElementById("starter").innerHTML='<div class="measurementguide">\
	<p>With the pants laid flat, measure from edge to edge widthwise across the ellipse that\'s created by the space between the rear and the front of the waistband. If the rear waistband is a perfectly straight line, use that.</p>\
	<p>Don\'t include belt loops in your measurement.  Enter it. Your final measurement should be about half of what the designers label said it would be.</p>\
	<p>(You double it to know the whole waist size but we didn\'t want to risk you messing up the math while you enter the data. You\'ll notice, though, that the actual waist measurement is likely to be different from what the label said by as much as 2 inches).</p>\
	<img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
	</div>'
	;
}

function displayLabelInseam()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>Pick one of the legs, measure from the crotch of the pant to the bottom of the cuff. If the line between those two points isn\'t perfectly straight, try to follow its curvature. Your final measurement should be within a couple of inches of what the designer\'s label said it would be. </p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayWaist()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>This is what the designer has labeled the inseam. For example, if the pant is a 32x30, the "Label inseam size" is 30." If there is no inseam, there might be information like "long" or "short".</p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayInseam()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>Pick one of the legs, measure from the crotch of the pant to the bottom of the cuff. If the line between those two points isn\'t perfectly straight, try to follow its curvature. Your final measurement should be within a couple of inches of what the designer\'s label said it would be. </p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayOutseam()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>Pick a side of the pant and measure from the top of the waistband town to the cuff. Again, try to follow any shapes the line creates but don\'t worry about being too precise.</p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayFront()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>Measure from the crotch over the fly to the top of the waistband  on the front of the pant, just above the fly\'s closure.</p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayBack()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>This one is a bit tricky because when the pant is laid on the ground part of it is visible from the front, which is confusing.</p>\
    <p>Our preferred method is to (1) measure from the crotch upward to the top of the rear waistband and remember that number. Then (2) measure from the crotch down to any fabric that\'s below it (this should be only an inch or so), (3) double that second number and (4) add the it to the first. You see what you just did there? </p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayHips()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>Measure from the bottom of the fly out to the outside edge of the pant, trying to remain parallel to the top of the pant. This can be a hard angle to get exactly right, because the top is often an ellipse shape rather than a straight line and the outseam isn\'t perpendicular to the top. Just give it your best effort.</p>\
    <p>Note that the bottom of the fly is quite a bit above the crotch, and that the outside point you end up on is usually a bit below the bottom of any pockets you have. You might also cross the seam running along the outside of the pant, depending on how it\'s constructed. </p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayThigh()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>Measure from the crotch out to the side of the pant, again trying to remain parallel to the top of the pant. This will be hard for all the same reasons the hip is hard to measure. Don\'t stress about it, but recognize that this is one of the limits of using the manual entry page (We take pains to be consistent in our own measurements and double-check each other when necessary).</p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayKnee()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>Measure 14 inches down from the crotch along the inseam. From that point measure out to the edge of outside of the leg, trying to remain perpendicular to the sides of the leg and going right over any seams you come across. </p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayCuff()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p>Measure the width of the cuff, edge to edge. </p>\
    <img src="{% get_static_prefix %}images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}