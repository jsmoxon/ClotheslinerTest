FIT_DICT = { #all are ref pant MINUS returned pant
#These are mostly done, ready for James
'nutcupping': # a shorter totalRise without a larger waist will result in more nutcupping
{
	'zero':'These pants will fit you in the crotch with about the same level of tightness',
	'positive':
		{
		1: 'These pants will feel negligably more tight in the crotch.',
		2: 'These pants will feel noticably more tight in the crotch.',
		3: 'These pants will feel a lot more tight in the crotch.'
		},
	'negative':
		{
		1: 'These pants will feel negligably less tight in the crotch.',
		2: 'These pants will feel noticably less tight in the crotch.',
		3: 'These pants will feel a lot less tight in the crotch.'
		}
	},
	
'leg': #a function of (Cuff + Knee + Thigh) divided by (waist + totalRise + outseam)
{
	'zero':'The leg will feel generally the same degree of tightness',
	'positive':
		{
		1: 'The leg will feel slightly more tight all the way down',
		2: 'The leg will feel quite a bit more tight all the way down',
		3: 'The leg will feel a lot more tight all the way down'
		},
	'negative':
		{
		1: 'The leg will feel slightly more loose all the way down',
		2: 'The leg will feel quite a bit more loose all the way down',
		3: 'The leg will feel a lot more loose all the way down'
		}
	},		

'buttCupping': # +ratio(backrise/totalrise) if  +ratio(outseam/inseam) < threshold (if >threshold then it's higher back)
#if -ratio(backrise/totalrise) then more buttcup (OR, we're not sure: either just changed crotch (no impact on fit) or wedgie and high front rise, depending on something we don't understand)

{
	'zero':"These pants won't change how much they gap at the small of your back",
	'positive':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		},
	'negative':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		}
	},	

'muffintop': #for now just a function of frontRise
{
	'zero':"The pants will sit on your waist at about the same level.",
	'positive':
		{
		1: 'a bit lower',
		2: 'lower',
		3: 'signifcantly lower'
		},
	'negative':
		{
		1: 'a bit higher',
		2: 'higher',
		3: 'significantly higher'
		}
	},	
	
'thigh': #a function of the thigh and the fabric 
{
	'zero':'nada',
	'positive':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		},
	'negative':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		}
	},	

'ankle': #for now a function of only cuff, but maybe later thigh divided by knee divided by cuff
	{
	'zero':'Same cuff',
	'positive':
		{
		.25: 'Similar cuff',
		.5: 'Tighter cuff',
		1: 'Much tighter cuff',
		2: 'Extremely tighter cuff',
		99: 'Insanely tighter cuff'
		},
	'negative':
		{
		.25: 'Similar cuff',
		.5: 'Looser cuff',
		1: 'Much looser cuff',
		2: 'Extremely looser cuff',
		99: 'Insanely looser cuff'
		}
	},


'plumberButt': # increases if backRise goes down and frontRise doesn't increase to compensate
# if frontRise does increase, the crotch just moves further back (we don't know the impact of that)
{
	'zero':"These pants won't change your risk of plumber butt.",
	'positive':
		{
		1: 'These pants will increase your risk of plumber butt by a lot.',
		2: 'These pants will increase your risk of plumber butt by a little bit.'

		},
	'negative':
		{
		1: 'These pants will decrease the chance you get a plumber butt, but not by much.',
		2: 'These pants should signficanly decrease your risk of getting a plumber butt.'
		}
	},


#Not going to use these yet
'backgap': # a larger (Outseam - Inseam), assuming equal totalRise, will equal less backgap
# a larger (O-I) with shorter totalRise will equal more wedgie and nutcupping (should add a variable for wedgie)
# a larger (O-I) with longer totalRise will equal larger pants
#should have waist too
{
	'zero':"These pants won't change how much they gap at the small of your back",
	'positive':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		},
	'negative':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		}
	},	

'wedgie': # +rearRise/totalRise
{
	'zero':"These pants won't change how much they gap at the small of your back",
	'positive':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		},
	'negative':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		}
	},		

	
	
'waistLooseness': #increases if waist goes up and frontRise stays the same; decreases if waist decrease and frontRise remains same; ambiguous if waist increases but frontRise decreases; loosens if waist increases and front rise increases
# need to rewrite these descriptors to account for waist/rise interaction
{
	'zero': 'Similar waist', 
	'positive': 
		{
		.25: 'Similar waist',
		.5: 'Slightly tighter waist',
		1: 'Tighter waist',
		2: 'Much tighter waist',
		99: 'Insanely tighter waist'
		},
	'negative': 
		{
		.25: 'Similar waist',
		.5: 'A bit looser waist',
		1: 'Looser waist',
		2: 'Much looser waist',
		99: 'Insanely looser waist'
		}
	},
	


'seat': #as +(outseam divided by inseam) or +rearrise, seat increases
{
	'zero':'The seat has generally more room',
	'positive':
		{
		1: 'The leg will feel slightly more tight all the way down',
		2: 'nada',
		3: 'nada'
		},
	'negative':
		{
		1: 'nada',
		2: 'nada',
		3: 'nada'
		}
	},	