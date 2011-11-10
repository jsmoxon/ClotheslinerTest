FIT_DICT = { #all are ref pant MINUS returned pant
#These are mostly done, ready for James

"muffintop": #for now just a function of frontRise
{
	"zero":"The rise is structured so that this pair sits on your waist at about the same height as the reference pant does. That said, if theyre much looser around the waist theyll be inclined to slouch lower. ",
	"positive":
		{
		1: "These will sit a bit lower on your waist. This should feel pretty similar to your reference pant, but youll  notice that it fits lower if you think about it.",
		2: "They will sit lower on your waist or hip. This will feel like more of a low rise pant, and youll notice that some T shirts wont tuck in anymore.",
		3: "The pants will sit signifcantly lower on your hips. This will feel significantly more of a low rise pant, so youre going for a much different look and feel than your reference pant."
		},
	"negative":
		{
		1: "These sit a bit higher on your hip, which should feel pretty similar to the reference pant.",
		2: "You will definitely notice that this sits higher and unless your reference pant feels too low you should realize that this might sit too high on your waist (or, if you choose to wear it at the same height on your waist, youll feel like theres more excess space between your junk and the crotch of the pants).",
		3: "This is getting significantly higher in the rise, and will feel like a very different pant, either sitting very high on your waist or becomming a drop-crotch pant, where the crotch  of the pant is noticably low on your thigh."
		}
},	
	
"buttcupping": # (rearlRise/totalRise)
{
	"zero":"You wont notice much of a change in how much room these pants provide in the seat.",
	"positive":
		{
		.02: "The butt for these pants will feel slightly more tight, but not significantly enough to worry about.",
		.04: "The buttocks will be noticably more tight, and should be enough for you unless you find the reference pant to be super loose in the butt.",
		.05: "These will be much more tight in the butt, which is risky if the reference pant feels like its comfortably form-fitting because it might be enough of a difference that you end up feeling uncomfortably tight all around the pelvis as your butt pulls the fabric back and the crotch up toward your junk. That said, it might be what youre going for so dont let us be the judge of whats appropriate." 
		},
	"negative":
		{
		1: "These pants will feel slightly more loose in the butt, but not signficantly so.",
		2: "Theres significantly more room in the rear of these pants, but you shouldnt run the risk yet of a diaper butt unless you already had plenty of room in the reference pant.",
		}
},
	
"diaperbutt": # some boolian
	{
	0: "It will sit high on your waist at the back, coming up toward your lower back. This should make it easier to keep your shirts tucked in.",
	1: "Youre running into a risk of having enough extra fabric at this point that you could fit a diaper in there; its known in the industry as diaper butt",
	},

	
"nutcupping": # a shorter totalRise without a larger waist will result in more nutcupping
{
	"zero":"These pants will fit you in the crotch with about the same level of tightness",
	"positive":
		{
		1: "These pants will feel negligably tighter in the crotch.",
		2: "These pants will feel noticably tighter in the crotch.",
		3: "These pants will feel a lot tighter in the crotch."
		},
	"negative":
		{
		1: "These pants will feel negligably looser in the crotch.",
		2: "These pants will feel noticably looser in the crotch.",
		3: "These pants will feel a lot looser in the crotch."
		}
	},

"leg": #a function of (Cuff + Knee + Thigh) divided by (waist + totalRise + outseam)
{
	"zero":"The taper of the leg should basically mirror the reference pant.",
	"positive":
                {
                .005: 'It will taper slightly more all the way down which is traditionally called a tapered fit.',
                .02: 'It will taper noticably more all the way down the leg so it will be feel slimmer.',
                .04: 'It will taper a lot more down the leg which is how the kids are wearing it these days.'
                },
	"negative":
                {
                1: 'It will taper slightly less all the way down which is more of a straight cut.',
                2: 'It will taper noticably less all the way down the leg so it will feel looser and more relaxed.',
                3: 'It will taper a lot less down the leg which will start to feel like a much looser pant all around.'
                }
	},	
	
"thigh": #a function of the thigh and the fabric 
{
	"zero":" The thigh should be nearly the exact same.",
	"positive":
		{
		1: "Now for the legs. The thigh will fit a little tighter which should not make a big difference, depending on your taste.",
		2: "Expect that the thigh will fit noticably tighter which may start to feel rather tight if you are already feeling cramped at the thigh.",
		3: "Now for the legs. The thigh will fit significantly tighter which may start to change your range of motion. But hey, the kids are wearing them that way these days."
		},
	"negative":
		{
		1: "Now for the legs. The thigh will fit a bit looser which should not make a big differnce, depending on your taste.",
		2: "Expect that the thigh will fit noticably looser which might start to give you a bit more breathing room if that is what you are looking for.",
		3: "Now for the legs. The thigh will fit significantly looser which which will start to feel very roomy and comfortable. That or hammer pants. "
		}
	},	

"ankle": #for now a function of only cuff, but maybe later thigh divided by knee divided by cuff
	{
	"zero":"It finishes off with a very similar leg opening.",
	"positive":
		{
		.25: "It finishes off with a bit tighter leg opening.",
		.5: "The leg opening will be noticably tighter.",
		1: "It finishes off with a much tighter leg opening, creating a more tapered feel.",
		2: "The leg opening will feel like a boot cut by comparison.",
		99: "This leg opening is insanely tighter. Only try these if you are comfortable losing circulation to your feet."
		},
	"negative":
		{
		.25: "It finishes off with a bit looser leg opening.",
		.5: "The leg opening will be noticably looser.",
		1: "It finishes off with a much looser leg opening, giving it a less tapered feel.",
		2: "The leg opening will feel like a boot cut by comparison.",
		99: "Welcome to 1978. The pant finishes much looser at the leg opening."
		}
	}
	}
