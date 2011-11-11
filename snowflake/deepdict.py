DEEP_DICT = {

"muffintop": 
{
	"zero":"Muffintop is zero.",
	"positive":"Muffintop is positive.",	
	"negative": "Muffintop is negative."
},	
	
"buttcupping":
{
	"zero":"Buttcupping is zero.",
	"positive":"Buttcupping is positive.",	
	"negative": "Buttcupping is negative."
},
	
"diaperbutt":
{
	0: "Congrats! no Diaperbutt.",
	1: "This has Diaperbutt."
},

	
"nutcupping": 
{
	"zero":"Nutcupping is zero.",
	"positive":"Nutcupping is positive.",	
	"negative": "Nutcupping is negative."
},

"leg": 
{
	"zero":"Leg is zero.",
	"positive":"Leg is positive.",	
	"negative": "Leg is negative."
},	
	
"thigh":
{
	"zero":"Thigh is zero.",
	"positive":"Thigh is positive.",	
	"negative": "Thigh is negative."
},	

"ankle":
{
	"zero":"Ankle is zero.",
	"positive":"Ankle is positive.",	
	"negative": "Ankle is negative."
}
}

SHALLOW_DICT = {
    "muffintop": "How low the pant sits on the front of your waist is a function of the front rise. In this case the relevant measurements are:",
    "buttcupping": "The way the pant fits around the butt is a function of front and back rise. In this case the relevant measurements are:",
    "diaperbutt": "Extra material in the seat is a function of front and back rise and the ratio of inseam to outseam. In this case the relevant measurements are:",
    "nutcupping": "The way the pant feels around the crotch is a function of the relationship between front rise and actual waist. In this case the relevant measurements are:",
    "leg": "The taper of the pant is related to the measurements at the thigh, knee and cuff. In this case the relevant measurements are:",
    "thigh": "The thigh variable gives you an important sense of how tight the pant will fit around the upperleg. At this point we dont account for fabric weight or stretch, which are very important. That said, the relevant measurements are:",
    "ankle": "The ankle is a function of the leg opening and is an important indicator of how the pant is style and how it will taper. In this case the relevant measurements are:"
}

RIGHT_DICT = {
"muffintop": "front_rise",	
"buttcupping": "front_rise back_rise",
"diaperbutt": "front_rise back_rise inseam outseam",	
"nutcupping": "waist front_rise back_rise",
"leg": "cuff thigh knee",
"thigh": "thigh",	
"ankle": "cuff"
}

OTHER_DICT = {
'waist':
	{
	'zero': 'Similar waist', 
	'positive': 'Smaller waist',
	'negative': 'Larger waist',
	},
'front_rise':
	{
	'zero': 'Similar front rise', 
	'positive': 'Smaller front rise',
	'negative': 'Larger front rise',
	},
'thigh':
	{
	'zero': 'Similar thigh', 
	'positive': 'Smaller thigh',
	'negative': 'Larger thigh',
	},
'outseam':
	{
	'zero': 'Similar outseam', 
	'positive': 'Smaller outseam',
	'negative': 'Larger outseam',
	},
'inseam':
	{
	'zero': 'Similar inseam', 
	'positive': 'Smaller inseam',
	'negative': 'Larger inseam',
	},
'cuff':
	{
	'zero': 'Similar cuff', 
	'positive': 'Smaller cuff',
	'negative': 'Larger cuff',
	},
'knee':
	{
	'zero': 'Similar knee', 
	'positive': 'Smaller knee',
	'negative': 'Larger knee',
	},
'hips':
	{
	'zero': 'Similar hips', 
	'positive': 'Smaller hips',
	'negative': 'Larger hips',
	},
'back_rise':
	{
	'zero': 'Similar back rise', 
	'positive': 'Smaller back rise',
	'negative': 'Larger back rise',
	}
}

EXPLANATION = "Here is how you use our site"
