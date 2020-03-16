<?php
session_start();
$_SESSION["wrong"] = 0;
$_SESSION["username"] = 0;
?>
<?php
$myfile = fopen("account.txt", "r") or die("Sorry ! There are some problem of our web page .Class web page services is stopped. We will fixed as soon as possible.");
$a= $_POST["username"];
$b= $_POST["password"];
 
while(!feof($myfile)) 
  {
$username = trim(fgets($myfile)); 
$password = trim(fgets($myfile));
$admin = trim(fgets($myfile));
$name = trim(fgets($myfile));
if (($a == $username) && ($b == $password))
{
$_SESSION["username"] = $username;
$_SESSION["password"] = $password;
$_SESSION["admin"] = $admin;
$_SESSION["name"] = $name;
setcookie("timer","1",time()+3600,"/");
}
}	
fclose($myfile);

if(!empty($_SESSION["username"])) {
HEADER("Location:main.php");
	exit();
}
else{
	$_SESSION["wrong"] = 1;
	HEADER("Location:home.php");
exit();
}
?>
