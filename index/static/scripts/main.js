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
});




