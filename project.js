dweetio.get_latest_dweet_for("IOTNCIPJM",function(err,dweet){
	var dweet =dweet[0];
	console.log(dweet.content);
	document.getElementById("thing").innerText=(dweet.thing);
	document.getElementById("message").innerText=(dweet.content.message);
	document.getElementById("latitude").innerText=(dweet.content.latitude);
	document.getElementById("longitude").innerText=(dweet.content.longitude);
	document.getElementById("temp").innerText=(dweet.content.temp);
	document.getElementById("Humidity").innerText=(dweet.content.Humidity);
	document.getElementById("created").innerText=(dweet.created);
	console.log(dweet.created);
	
});
