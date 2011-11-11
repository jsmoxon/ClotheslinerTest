FIT_DICT = { #all are ref pant MINUS returned pant
#These are mostly done, ready for James

"muffintop": #for now just a function of frontRise
{
	"zero":"Rise - Structured to sit on your waist at about the same height as the reference pant.",
	"positive":
		{
		1: "Rise - These sit a bit lower on your waist.",
		2: "Rise - These sit lower on your waist or hip, feeling more like a low rise pant, and youll notice that some T shirts wont tuck in anymore.",
		3: "Rise - These sit signifcantly lower on your hips. Realize this will have a much different look and feel."
		},
	"negative":
		{
		1: "Rise - These sit a bit higher on your hip, but should feel pretty similar to the reference pant.",
		2: "Rise - These sit higher on your waist, and should feel a bit more secure.",
		3: "Rise - These are significanltly higher on your waist, and feel like a very different pant. They can be worn either sitting very high on your waist or as a drop-crotch pant, where the crotch of the pant is noticably low on your thigh."
		}
},	
	
"buttcupping": # (rearlRise/totalRise)
{
	"zero":"Seat - You wont notice much of a change in how much room these pants provide.",
	"positive":
		{
		.02: "Seat - The butt for these pants will feel slightly more tight, but not significantly enough to worry about.",
		.04: "Seat - The buttocks will be noticably more tight, and should be enough for you unless you find the reference pant to be super loose.",
		.05: "Seat - These will be much more tight in the butt, which is risky if the reference pant fits comfortably." 
		},
	"negative":
		{
		1: "Seat - These pants feel slightly more loose in the butt, but not signficantly so.",
		2: "Seat - Theres significantly more room in the rear of these pants, but you shouldnt run the risk yet of a diaper butt unless you already had plenty of room in the reference pant.",
		}
},
	
"diaperbutt": # some boolian
	{
	0: "Rear Fabric - This pant will sit high on your waist at the back. This should make it easier to keep your shirts tucked in.",
	1: "Rear Fabric - Youre running into a risk of having enough extra fabric at this point that you could fit a diaper in there; its known in the industry as diaper butt.",
	},

	
"nutcupping": # a shorter totalRise without a larger waist will result in more nutcupping
{
	"zero":"Crotch - These pants will fit you in the crotch at about the same level of tightness.",
	"positive":
		{
		1: "Crotch - These pants will feel negligably tighter.",
		2: "Crotch - These pants will feel noticably tighter.",
		3: "Crotch - These pants will feel a lot tighter."
		},
	"negative":
		{
		1: "Crotch - These pants will feel negligably looser.",
		2: "Crotch - These pants will feel noticably looser.",
		3: "Crotch - These pants will feel a lot looser."
		}
	},

"leg": #a function of (Cuff + Knee + Thigh) divided by (waist + totalRise + outseam)
{
	"zero":"Legroom - The legs will feel as roomy as those of the reference pant.",
	"positive":
                {
                .005: 'Legroom - The legs will feel about the same as the reference pant, depending on how light and stretchy the fabric is.',
                .02: 'Legroom - The legs will feel a bit slimmer all the way down, though they will maintain the same taper.',
                .04: 'Legroom - The legs will feel quite a bit tighter, depending on the fabric.'
                },
	"negative":
                {
                1: 'Legroom - The legs will feel a bit looser, but keep the same general shape.',
                2: 'Legroom - The legs will feel a lot looser, but keep the same general shape.',
                3: 'Legroom - The legs will feel a lot looser, depending on differences in fabric weight and stretch.'
                }
	},	
	
"thigh": #a function of the thigh and the fabric 
{
	"zero":"Thigh - Nearly exactly the same, except that we dont currently account for fabric weight or stretch.",
	"positive":
		{
		1: "Thigh - Will fit a little tighter which should not make a big difference.",
		2: "Thigh - Expect that the thigh will fit noticably tighter. If you feel crampted in your reference pair you may want to stay away.",
		3: "Thigh - These may start to limit your range of motion. But hey, the kids are wearing them that way these days."
		},
	"negative":
		{
		1: "Thigh - Will fit a bit looser but not enough to matter.",
		2: "Thigh - Noticably looser which will make you comfortable if your reference pant is too tight but may also feel baggy if your reference pant is currently comfortable.",
		3: "Thigh - Will fit significantly looser which which will start to feel very roomy and comfortable. That or hammer pants. Just kidding."
		}
	},	

"ankle": #for now a function of only cuff
	{
	"zero":"Ankle - The leg opening is very similar.",
	"positive":
		{
		.25: "Ankle - Finishes off with a bit tighter leg opening.",
		.5: "Ankle - The leg opening will be noticably tighter.",
		1: "Ankle - Finishes off with a much tighter leg opening, creating a more tapered feel.",
		2: "Ankle - The leg opening will feel like a boot cut by comparison.",
		99: "Ankle - This leg opening is insanely tighter. Only try these if you are comfortable losing circulation to your feet."
		},
	"negative":
		{
		.25: "Ankle - Finishes off with a bit looser leg opening.",
		.5: "Ankle - The leg opening will be noticably looser.",
		1: "Ankle - It finishes off with a much looser leg opening, giving it a less tapered feel.",
		2: "Ankle - The leg opening will feel like a boot cut by comparison.",
		99: "Ankle - The pant finishes much looser at the leg opening. Welcome to 1978. "
		}
	}
	}
