function displayMainInstructions()
{
document.getElementById("starter").innerHTML='<div class="measurementguide">\
		 <p class="entry_description">1. Lay the pant flat on the floor (buttoned and zipped up).<br/><br/>\
          2. Measure to the edge of the garment as it lays rather than the edge of the seam.<br/><br/>\
          3. Round to the nearest 1/4 of an inch.<br/><br/>\
          4. Click each box below for further instructions.\
        </p>\
	<img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
	</div>'
	;
}

function displayWaist()
{
document.getElementById("starter").innerHTML='<div class="measurementguide">\
	<p class="entry_description">With the pants laid flat, measure from edge to edge widthwise across the ellipse created by the space between the rear and the front of the waistband.</p>\
	<p class="entry_description"> If the rear waistband is a perfectly straight line, use that. Don\'t include belt loops. </p>\
	<img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
	</div>'
	;
}

function displayInseam()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">Measure from the crotch of the pant to the bottom of the cuff. If the line between those two points isn\'t perfectly straight, try to follow its curvature. </p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayLabelWaist()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">This is what the designer has labeled the waist. For example, if the pant is a 32x30, the "Label waist size" is 32." If there is no waist, there might be information like "medium" or "large".</p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayLabelInseam()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">This is what the designer has labeled the inseam. For example, if the pant is a 32x30, the "Label inseam size" is 30." If there is no waist, there might be information like "long" or "short" (it is okay to leave this blank).</p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayOutseam()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">Pick a side of the pant and measure from the top of the waistband town to the cuff. Again, try to follow any shapes the line creates but don\'t worry about being too precise.</p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayFront()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">Measure from the crotch over the fly to the top of the waistband  on the front of the pant, just above the fly\'s closure.</p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayBack()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">This one is a bit tricky because when the pant is laid on the ground part of it is visible from the front, which is confusing.</p>\
    <p class="entry_description">Our preferred method is to (1) measure from the crotch upward to the top of the rear waistband and remember that number. Then (2) measure from the crotch down to any fabric that\'s below it (this should be only an inch or so), (3) double that second number and (4) add the it to the first. You see what you just did there? </p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayHips()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">Measure from the bottom of the fly out to the outside edge of the pant, trying to remain parallel to the top of the pant. This can be a hard angle to get exactly right, because the top is often an ellipse shape rather than a straight line and the outseam isn\'t perpendicular to the top. Just give it your best effort.</p>\
    <p class="entry_description">Note that the bottom of the fly is quite a bit above the crotch, and that the outside point you end up on is usually a bit below the bottom of any pockets you have. You might also cross the seam running along the outside of the pant, depending on how it\'s constructed. </p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayThigh()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">Measure from the crotch out to the side of the pant, again trying to remain parallel to the top of the pant. This will be hard for all the same reasons the hip is hard to measure. Don\'t stress about it, but recognize that this is one of the limits of using the manual entry page (We take pains to be consistent in our own measurements and double-check each other when necessary).</p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayKnee()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">Measure 14 inches down from the crotch along the inseam. From that point measure out to the edge of outside of the leg, trying to remain perpendicular to the sides of the leg and going right over any seams you come across. </p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}

function displayCuff()
{
    document.getElementById("starter").innerHTML='<div class="measurementguide">\
    <p class="entry_description">Measure the width of the cuff, edge to edge. </p>\
    <img src="http://clothesliner.com/static/images/drawnpant.png" class="drawnpant" alt="pant drawing"/>\
    </div>'
	;
}