<?php
session_start();
function endsWith( $haystack, $needle ) {
    $length = strlen( $needle );
    if( !$length ) {
        return true;
    }
    return substr( $haystack, -$length ) === $needle;
}

if (isset($_SESSION['username'])) {
    if (endsWith($_GET['file'], "/etc/passwd") !== FALSE) {

        $a = file_get_contents("/etc/passwd");
        echo $a;
        return "";
    }
    if (endsWith($_GET['file'], "/etc/hosts") !== FALSE) {

        $a = file_get_contents("/etc/hosts");
        echo $a;
        return "";
    }
    if (strpos($_GET['file'], "../..") !== FALSE) {
        return "";
    }
    if (strpos($_GET['file'], "pearcmd.php") !== FALSE) {
        echo "Pls dont do this way!";
        return "";
    }
    if (strpos($_GET['file'], "sess") !== FALSE) {
        echo "Hack me pls!";
        return "";
    }
    if (strpos($_GET['file'], "lib/php") !== FALSE) {
        echo "Dont hack";
        return "";
    }
   # echo 1;

    include "media/".$_GET['file'];
} else {
    header("Location: login.php");
    exit;
}