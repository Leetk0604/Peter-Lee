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
  min-width: 100%;
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

</style>

<HTML>

   <ul>
  <li><a href="main.php" >Home Page</a></li>
    <li><a href="homework.php">Homework List</a></li>
    <li><a href="classphoto.php">Class Photo</a></li>
    <li><a href="chatroom.php">Chat room</a></li>
    <li><a href="resource.php">Resource</a></li>
	<li><a href="seat.php"class="active">Seat</a></li>
	

 <?php
if(($_SESSION["admin"]) ==1) {
	echo'<li><a href="admin.php">admin</a></li>
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
<h1>seat</h1>
<img src="seat.jpg" usemap="#image-map" >
<map name="image-map">
    <area target="" alt="6c01" title="6c01" href="" coords="208,261,96,196" shape="rect">
    <area target="" alt="6c02" title="6c02" href="" coords="99,273,207,333" shape="rect">
    <area target="" alt="6c03" title="6c03" href="" coords="97,347,203,408" shape="rect">
    <area target="" alt="6c04" title="6c04" href="" coords="96,421,204,483" shape="rect">
    <area target="" alt="6c05" title="6c05" href="" coords="96,496,204,558" shape="rect">
    <area target="" alt="6c06" title="6c06" href="" coords="226,198,334,261" shape="rect">
    <area target="" alt="6c07" title="6c07" href="" coords="225,272,331,335" shape="rect">
    <area target="" alt="6c09" title="6c09" href="" coords="226,420,331,482" shape="0">
    <area target="" alt="6c10" title="6c10" href="" coords="225,494,333,557" shape="0">
    <area target="" alt="6c11" title="6c11" href="" coords="395,198,501,262" shape="0">
    <area target="" alt="6c08" title="6c08" href="" coords="225,345,331,409" shape="0">
    <area target="" alt="6c12" title="6c12" href="" coords="393,274,501,334" shape="0">
    <area target="" alt="6c13" title="6c13" href="" coords="396,348,498,409" shape="0">
    <area target="" alt="6c14" title="6c14" href="" coords="393,422,501,487" shape="0">
    <area target="" alt="6c15" title="6c15" href="" coords="393,496,500,557" shape="0">
    <area target="" alt="6c16" title="6c16" href="" coords="520,198,627,262" shape="0">
    <area target="" alt="6c17" title="6c17" href="" coords="520,272,630,334" shape="0">
    <area target="" alt="6c18" title="6c18" href="" coords="521,348,629,413" shape="0">
    <area target="" alt="6c19" title="6c19" href="" coords="518,422,630,487" shape="0">
    <area target="" alt="6c20" title="6c20" href="" coords="522,496,630,559" shape="0">
    <area target="" alt="6c21" title="6c21" href="" coords="692,200,796,263" shape="0">
    <area target="" alt="6c22" title="6c22" href="" coords="689,273,796,338" shape="0">
    <area target="" alt="6c23" title="6c23" href="" coords="817,200,925,265" shape="0">
    <area target="" alt="6c24" title="6c24" href="" coords="816,273,924,338" shape="0">
    <area target="" alt="6c25" title="6c25" href="" coords="985,198,1094,263" shape="0">
    <area target="" alt="6c26" title="6c26" href="" coords="985,273,1094,337" shape="0">
    <area target="" alt="6c27" title="6c27" href="" coords="1114,201,1221,264" shape="0">
    <area target="" alt="6c28" title="6c28" href="" coords="1111,272,1219,338" shape="0">
    <area target="" alt="null" title="null" href="" coords="690,349,1218,561" shape="0">
</map>
</content>
  </html>
 
