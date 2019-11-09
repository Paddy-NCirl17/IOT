dweetio.get_latest_dweet_for("Fire_Room",function(err,dweet){
	var dweet =dweet[0];
	console.log(dweet.content);
	console.log(dweet.content.location);
	document.getElementById("Alarm").innerText=(dweet.content.Alarm);
	document.getElementById("Firedoor").innerText=(dweet.content.Firedoor);
	document.getElementById("Temperature").innerText=(dweet.content.Temperature);
	document.getElementById("Room").innerText=(dweet.content.location.Room);
	document.getElementById("Wing").innerText=(dweet.content.location.Wing);
	document.getElementById("Floor").innerText=(dweet.content.location.Floor);
	document.getElementById("created").innerText=(dweet.created);
	console.log(dweet.created);
	
});
