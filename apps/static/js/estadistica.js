var data = [45,20,35,15,60];
		var r = 250;
		var color = d3.scale.ordinal().range(["red","white","gray","purple","blue"]);
		var canvas = d3.select("#mainright").append("svg").attr("width", 1000).attr("height", 1000);
		var group = canvas.append("g").attr("transform","translate(300,300)");
		var arc = d3.svg.arc().innerRadius(0).outerRadius(r);
		var pie = d3.layout.pie().value(function(d){return d;});
		var arcs = group.selectAll(".arc").data(pie(data)).enter().append("g").attr("class", "arc");
		arcs.append("path").attr("d",arc).attr("fill", function(d){return color(d.data);});
		arcs.append("text").attr("transform",function(d){return "translate("+arc.centroid(d)+")";}).attr("text-anchor","middle").attr("font-size","1.5em").text(function(d){return d.data;});
		