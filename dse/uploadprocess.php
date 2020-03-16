<?php
session_start();
?>
<?php
$target_dir = "classphotocontainer/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        $_SESSION["uploadOk"] = 1;
    } else {
        $_SESSION["uploadOk"] = 3;
		$_SESSION["uploadsignal"] = 4;
		}
}
// Check if file already exists
if (file_exists($target_file)) {
    $_SESSION["uploadOk"] = 3;
	$_SESSION["uploadsignal"] = 1;
	header("location:photoupload.php");
		exit();
}
// Check file size
if ($_FILES["fileToUpload"]["size"] > 5000000) {
  
    $_SESSION["uploadOk"] = 3;
	$_SESSION["uploadsignal"] = 2;
	header("location:photoupload.php");
		exit();
}
// Allow certain file formats
if($imageFileType != "jpg"  ) {
    $_SESSION["uploadOk"] = 3;
	$_SESSION["uploadsignal"] = 3;
	header("location:photoupload.php");
		exit();
}
// Check if $uploadOk is set to 0 by an error
if ($_SESSION["uploadOk"] == 3) {
    echo "Sorry, your file was not uploaded.";
	header("location:photoupload.php");
		exit();
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        header("location:photoupload.php");
		exit();
    } else {
        echo "Sorry, there was an error uploading your file.";
		$_SESSION["uploadok"] = 2;
		header("location:photoupload.php");
		exit();
    }
}
?>