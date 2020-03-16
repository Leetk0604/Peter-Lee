<?php
session_start();
?>
<?php
if(!isset($_SESSION["username"])) {
	session_unset(); 
	session_destroy(); 
	HEADER("Location:home.php");
	 exit();
}
if($_SESSION["admin"] == 1) {}
else{
	HEADER("Location:main.php");
	 exit();
}
if(count($_COOKIE["timer"]) > 0) {
	}
	else{
		session_unset(); 
	session_destroy(); 
	HEADER("Location:home.php");
	 exit();}
?>

<HTML>
<style>
body {margin:0;
background-image: url("thmss.JPG");
  background-size: cover;
background-repeat: no-repeat;
}

aside {
  float: right;
  width: 20%;
      height:auto;
   min-height: 100%;
  margin-top:60px;
  padding: 20px;
}
content {
	float: left;
   width: auto;
  min-width: 50%;
  margin-top:60px;
  padding: 20px;
  border-radius: 25px;
  margin-left:95px;
  background-color:e8e8e8;
  opacity:0.9;
    height:auto;
   min-height: 100%;

}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  position: fixed;
  top: 0;
  width: 100%;
  z-index:52;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}
.active {
  background-color: #4CAF50;
}
/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position:relative;
  margin: auto;

}

/* Hide the images by default */
.mySlides {
  display: none;
}
/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 2s;
  animation-name: fade;
  animation-duration: 2s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
#mySidenav h2 {
  position: absolute; /* Position them relative to the browser window */
  left: -250px; /* Position them outside of the screen */
  transition: 0.3s; /* Add transition on hover */
  padding: 15px; /* 15px padding */
  width: 20%; /* Set a specific width */
  text-decoration: none; /* Remove underline */
  font-size: 20px; /* Increase font size */
  color: white; /* White text color */
  border-radius: 0 5px 5px 0; /* Rounded corners on the top right and bottom right side */
}

#mySidenav h2:hover {
  left: 0; /* On mouse-over, make the elements appear as they should */
}

/* The about link: 20px from the top with a green background */
#sidebar {
	z-index:50;
  top: 50px;
  background-color:#333;
}

cl {
list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: white;
  width: 100%;
  height:100px;
  width:100px;
}
</style>
<HTML>

   <ul>
  <li><a href="main.php" >Home Page</a></li>
    <li><a href="homework.php">Homework List</a></li>
    <li><a href="classphoto.php">Class Photo</a></li>
    <li><a href="chatroom.php">Chat room</a></li>
    <li><a href="resource.php">Resource</a></li>
	<li><a href="seat.php">Seat</a></li>
	

 <?php
if(($_SESSION["admin"]) ==1) {
	echo'<li><a href="admin.php"class="active">admin</a></li>
	';	
}
?>
  </ul>
  


<div id="mySidenav" class="sidenav" >
  <h2 id="sidebar">
<?php
echo "welcome" .$_SESSION["name"] ;
echo $_SESSION["name"] . ".<br>";
?>
<br>
<br>
<br>
<img src="6c.png" style="width:100%"></img>
<br>
<br>
<br>
<br>
<br>
<?php
if(($_SESSION["admin"]) ==1) {
	echo'<a href="hwinput.php"style="text-decoration: none; color: white;">Input homework</a>
	';	
}
?>
<br>
<?php
if(($_SESSION["admin"]) ==1) {
	echo'<a href="photoupload.php"style="text-decoration: none; color: white;">Photo upload</a>
	';	
}
?>
<br>
<br>
<a href="www.google.com"style="text-decoration: none; color: white;">setting</a><br>
<a href="www.google.com"style="text-decoration: none; color: white;">report bug</a><br>
<a href="www.google.com"style="text-decoration: none; color: white;">changing password</a>

</h2>
</div>
<content>
<h1>ADMIN</h1>

</content>
<aside>
<div style="width:100% top:60px;" position="relative";>
<a class="weatherwidget-io" href="https://forecast7.com/zh-tw/22d28114d17/hong-kong/" data-label_1="HONG KONG" data-label_2="WEATHER" data-font="微軟正黑體 (Microsoft JhengHei)" data-theme="original" >HONG KONG WEATHER</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>
</div>
<div style="width:50% " position="relative" >
<br>
<br>
<br>
<iframe src="https://calendar.google.com/calendar/embed?showTitle=0&amp;height=300&amp;wkst=1&amp;bgcolor=%23ffffff&amp;src=zh.hong_kong%23holiday%40group.v.calendar.google.com&amp;color=%23125A12&amp;ctz=Asia%2FHong_Kong" style="border:none" width="300" height="300" frameborder="0" scrolling="no" position="relative" border-style="hidden" ></iframe>
</div> 
</aside>
  </html>
 