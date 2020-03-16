<?php
session_start();
?>
<?php
$reply=$_POST["reply"];
$date=(date("Y-m-d"));
$time=(date("h:i:sa"));
$myfile = fopen("chatroom.txt", "a") or die("Unable to open file!");
fwrite($myfile,$_SESSION["name"]."\r\n");
fwrite($myfile,"$reply\r\n");
fwrite($myfile,"$date\r\n");
fwrite($myfile,"$time\r\n");
fclose($myfile);
HEADER("Location:chatroom.php");
?>