<?php

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $login = htmlspecialchars($_POST["login"]);
    $password = htmlspecialchars($_POST["password"]);
    if ($login == "palina" && $password == "1234"){
        session_start();
        $_SESSION["loggedin"] = true;
        $_SESSION['data'] = array(
            'Imie' => $_POST['imie'],
            'Nazwisko' => $_POST['nazwisko'],
            'Plec' => $_POST['plec'],
            'Data urodzenia' => $_POST['urodziny'],
            'Numer telefonu' => $_POST['telefon'],
            'Prawo jazdy' => $_POST['prawojazdy'],
            'Miasto' => $_POST['miasto'],
            'Uwagi' => $_POST['uwagi']
          );
        header("Location: page.php");
    }
    else {
        header("Location: index6.php");
    }
    }
else {
    header("Location: index6.php");
}
