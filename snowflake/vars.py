BIG_DICT = { #ref pant minus returned pant
'retailer1_price':
        {
        'zero': 'Similar price',
        'positive':
                {
                .25: '1/4 in. tighter price',
                .5: '1/2 in. tighter price',
                1: '1 in. tighter price',
                2: '2 in. tighter price',
                99: 'Insanely tighter price'
                },
        'negative':
                {
                .25: '1/4 in. looser price',
                .5: '1/2 in. looser price',
                1: '1 in. looser price',
                2: '2 in. looser price',
                99: 'Insanely looser price'
                }
        },

'waist':
	{
	'zero': 'Similar waist', 
	'positive': 
		{
		.25: '1/4 in. tighter waist',
		.5: '1/2 in. tighter waist',
		1: '1 in. tighter waist',
		2: '2 in. tighter waist',
		99: 'Insanely tighter waist'
		},
	'negative': 
		{
		.25: '1/4 in. looser waist',
		.5: '1/2 in. looser waist',
		1: '1 in. looser waist',
		2: '2 in. looser waist',
		99: 'Insanely looser waist'
		}
	},
'front_rise':
	{
	'zero':'Same rise',
	'positive': 
		{
		.25:'1/4 in. lower rise',
		.5: '1/2 in. lower rise',
		1: '1 in. lower rise',
		2: '2 in. lower rise',
		99: 'Insanely lower rise'
		},
	'negative': 
		{
		.25:'1/4 in. higher rise',
		.5: '1/2 in. higher rise',
		1: '1 in. higher rise',
		2: '2 in. higher rise',
		99: 'Insanely higher rise'
		}
	},
'thigh':
	{
	'zero':'Same thigh',
	'positive': 
		{
		.5: 'Similar thigh',
		1: 'Tighter thigh',
		1.5: 'Much tighter thigh',
		99: 'Insanely tighter thigh'
		},
	'negative':
		{
		.5: 'Similar thigh',
		1: 'Looser thigh',
		1.5: 'Much looser thigh',
		99: 'Insanely looser thigh'
		}
	},
'outseam':
	{
	'zero':'Same outseam',
	'positive':
		{
		.5: 'Similar outsesam',
		1: 'Shorter outseam',
		1.5: 'Much shorter outseam',
		99: 'Insanely shorter outseam'
		},
	'negative':
		{
		.5: 'Similar outseam',
		1: 'Longer outseam',
		1.5: 'Much longer outseam',
		99: 'Insanely longer outseam'
		}
	},
	
'inseam':
	{
	'zero':'Similar inseam',
	'positive':
		{
		.5: 'Similar inseam',
		1: 'Slightly shorter inseam',
		1.5: 'Shorter inseam',
		3: 'Much shorter inseam',
		99: 'Insanely shorter inseam'
		},
	'negative':
		{
		.5: 'Similar inseam',
		1: 'Slightly longer inseam',
		1.5: 'Longer inseam',
		3: 'Much longer inseam',
		99: 'Insanely longer inseam'
		}
	},
'cuff':
	{
	'zero':'Same cuff',
	'positive':
		{
		.25: '1/4 in. tighter cuff',
		.5: '1/2 in. tighter cuff',
		1: '1 in. tighter cuff',
		2: '2 in. tighter cuff',
		99: 'Insanely tighter cuff'
		},
	'negative':
		{
		.25: '1/4 in. looser cuff',
		.5: '1/2 in. looser cuff',
		1: '1 in. looser cuff',
		2: '2 in. looser cuff',
		99: 'Insanely looser cuff'
		}
	},
'knee':
	{
	'zero':'Same knee',
	'positive':
		{
		.5: 'Similar knee',
		1: 'Tighter knee',
		1.5: 'Much tighter knee',
		99: 'Insanely tighter knee'
		},
	'negative':
		{
		.5: 'Similar knee',
		1: 'Looser knee',
		1.5: 'Much looser knee',
		99: 'Insanley looser knee'
		}
	},
'hips':
	{
	'zero':'Same thigh',
	'positive':
		{
		.25: 'Similar hips',
		5: 'Tighter hips',
		1: 'Much tighter hips',
		99: 'Insanely tighter hips'
		},
	'negative':
		{
		.25: 'Similar hips',
		5: 'Looser hips',
		1: 'Much looser hips',
		99: 'Insanely looser hips'
		}
	},
'back_rise':
	{
	'zero':'same back rise',
	'positive':
		{
		.25: 'Similar back rise',
		.5: 'Shorter back rise',
		1: 'Much shorter back rise',
		99: 'Insanely shorter back rise'
		},
	'negative':
		{
		.25: 'Similar back rise',
		.5: 'Longer back rise',
		1: 'Much longer back rise',
		99: 'Insanely longer back rise'
		}
	}
}

MOE = {'waist':1, 'front_rise':1, 'thigh':1, 'outseam':1, 'inseam':1, 'cuff':1, 'knee':2, 'hips':2, 'back_rise':3, 'retailer1_price':10000}
