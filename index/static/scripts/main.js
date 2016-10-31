$(document).ready(function () {
  $(".img-class").click(function(){ 
	$("#player").get(0).pause();	
	var filename = this.id;
	filename = filename.replace('static/images/thumbnails/','');
	filename = filename.replace('.jpeg','_dash.mpd');
	player = dashjs.MediaPlayer().create();
	player.initialize($("#player").get(0), "http://10.1.20.113/dash_vod/"+filename, true);
	$("#player").get(0).load();
	$("#player").get(0).play();
 });
 
 //$("#popup").dialog({ autoOpen: false, show: 'slide', resizable: false, position: 'center', stack: true, height: 'auto', width: 'auto', modal: true });
 //$("#popup").dialog('open'); 

  // Get the modal 
var modal = document.getElementById('popup'); 
var btn = document.getElementById("myBtn"); 
var span = document.getElementsByClassName("close")[0];  
btn.onclick = function() { modal.style.display = "block"; } 
span.onclick = function() { modal.style.display = "none"; } 
window.onclick = function(event) { if (event.target == modal) { modal.style.display = "none"; } }

    $("#uploadvideo").click(function(){$(".modal-body").html("<img style='width:20%;' src='https://s-media-cache-ak0.pinimg.com/originals/93/a4/39/93a439f02fed8676fb281e461bbde801.gif'></img>");
$(".modal-content").height("50%")});
});






