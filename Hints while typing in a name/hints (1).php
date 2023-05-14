<?php
$servername = "sauranskayap.cba.pl"; 
$username = "svrnska"; 
$password = "Pass1234"; 
$dbname = "svrnska";  
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("Nie udało połączyć!");
}
$sql = "SELECT imie FROM PD9";
$result = mysqli_query($conn, $sql);
if ($result) {
    $names = array();
    while ($row = mysqli_fetch_assoc($result)) {
        $names[] = $row['imie'];
    }
} else {
    echo "Błąd!";
}
mysqli_close($conn);

function compare($name, $hint){
    $hintLen = strlen($hint);
    if(strncmp($name, $hint, $hintLen) == 0){
        return true;
    }
    else{
        return false;
    }
}

if (isset($_POST['hint'])) {
    $hint = $_POST['hint'];
    if (!empty($hint)) {
        foreach ($names as $name) {
            if (compare($name, $hint) !== false) {
                echo $name . "<br>";
            }
        }
    }
}


?>