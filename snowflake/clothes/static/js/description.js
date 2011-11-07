function compThem(val, key)
{
	usage = sauce[key];
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
	else {"you messed up somewhere";}
}