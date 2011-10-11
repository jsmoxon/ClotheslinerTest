var d = new Object();
{% for des, sty in styles.items %}
d[{{des.id}}] = new Array();
{% for st in sty %}
d[{{des.id}}].push(new Array("{{st.id}}","{{st.name}}"));
{% endfor %}
{% endfor %}

function genStyles(sel)
{
    var optionlist = d[sel[sel.selectedIndex].value];
    var z = document.getElementById("styles");
    while(z.length > 0)
        {
	    z.remove(0);
        }
    for (i=0;i<optionlist.length;i++)
        {
	    var newOption = document.createElement("OPTION");
	    newOption.text = optionlist[i][1];
	    newOption.value = optionlist[i][0];
	    z.add(newOption, null);
        }
}
