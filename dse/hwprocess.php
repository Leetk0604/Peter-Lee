
<?php

$end=("end of today's hw");
$start=(date("Y-m-d"));
$a= $_POST["hwcontent"];
$myfile = fopen("hw.txt", "a") or die("Unable to open file!");
fwrite($myfile,"$start\r\n");
fwrite($myfile,"$a\r\n");
fwrite($myfile,"$end\r\n");
fclose($myfile);
header("location:hwinput.php");
?>
