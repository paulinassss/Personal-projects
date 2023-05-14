<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Lab7</title>
    <link rel="stylesheet" href="style7.css">
  </head>
  <body>
  <?php
    $servername = "sauranskayap.cba.pl"; 
    $username = "svrnska"; 
    $password = "Pass1234"; 
    $dbname = "svrnska"; 


    $connection = mysqli_connect($servername, $username, $password, $dbname);


    if (!$connection) {
        die("Connection failed: " . mysqli_connect_error());
    }
    else{

    mysqli_select_db($connection, "svrnska");
    }

 ?>

<div class="container">
    <div class="row">
        <div class="col">

            <form method="post">

            <div class="row">
            
                <div class="col">
                    <p>Imię: </p>
                </div>

                <div class="col">
                    <input type="text" name="imie" class="window" value="Palina">
                </div>

            </div>

            <div class="row">
            
                <div class="col">
                    <p>Nazwisko: </p>
                </div>

                <div class="col">
                    <input type="text" name="nazwisko" class="window" value="Sauranskaya">
                </div>

            </div>

            <div class="row">
            
                <div class="col">
                    <p>Wiek: </p>
                </div>

                <div class="col">
                    <input type="number" name="wiek" class="window" value="21">
                </div>

            </div>

            <div class="row">
            
                <div class="col">
                    <input type="submit" name="dodaj" class="window" value="Dodaj">
                    <input type="submit" name="wyswietl" class="window" value="Wyświetl bazę danych">
                </div>

            </div>

            <div class="row">
            
                <div class="col">
                    <br/>
                    Id: <input type="text" name="id" class="window1">
                    <input type="submit" name="edytuj" class="window" value="Edytuj">
                    <input type="submit" name="usun" class="window" value="Usuń">
                </div>

            </div>
            </form>
        </div>
        <div class="col">
            <?php 
            if (array_key_exists('wyswietl', $_POST)){
                $sql = "SELECT * FROM PD7";
                $result = mysqli_query($connection, $sql);

                if (mysqli_num_rows($result) > 0) {
                foreach ($result as $row) {
                    echo "<strong>id:</strong> " . $row["id"] . " <strong>Imie: </strong>" . $row["imie"] . " <strong>Nazwisko: </strong>" . $row["nazwisko"] . " <strong>Wiek: </strong>" . $row["wiek"] . "<br>";
                } 
                }   
                else {
                    echo "0 results";
                }   
            }

            else if(array_key_exists('dodaj', $_POST)) {
                $imie = $_POST['imie'];
                $nazwisko = $_POST['nazwisko'];
                $wiek = $_POST['wiek'];
                $sql = "INSERT INTO PD7 (imie, nazwisko, wiek) VALUES ('$imie', '$nazwisko', '$wiek')";
                if (mysqli_query($connection, $sql)) {
                    echo "Dodano nowy rekord do bazy danych.";
                }else{
                    echo "Błąd: " . $sql . "<br>" . mysqli_error($connection);
                }
            }
            else if(array_key_exists('usun', $_POST)){
                $id = $_POST['id'];
                if($id != ""){
                  $sql1 = "SELECT * FROM PD7 WHERE id = $id" ;
                  $result = mysqli_query($connection,$sql1);
                  if(mysqli_num_rows($result)>0){
                    $sql = "DELETE FROM PD7 WHERE id = $id";
                if (mysqli_query($connection, $sql)) {
                    echo "Usunięto rekord z bazy danych.";
                } else {
                    echo "Błąd: " . mysqli_error($connection);
                }
                  } 
                  else{
                    echo "Brak rejestrów o padanym ID!";
                  }
                }
                else{
                    echo "Nie podano ID!";
                }
                
            }

            else if(array_key_exists("edytuj", $_POST)){
                $imie = $_POST['imie'];
                $nazwisko = $_POST['nazwisko'];
                $wiek = $_POST['wiek'];
                $id = $_POST['id'];
                if($id != ""){
                  $test = "SELECT * FROM PD7 WHERE id = $id" ;
                  $result = mysqli_query($connection,$test);
                  if(mysqli_num_rows($result)==1){
                    $sql = "UPDATE PD7 SET imie = '$imie', nazwisko = '$nazwisko', wiek = '$wiek' WHERE id = $id";
                if (mysqli_query($connection, $sql)) {
                    echo "Edytowano rekord z bazy danych.";
                } else {
                    echo "Błąd: " . mysqli_error($connection);
                }
                  } 
                  else{
                    echo "Brak rejestrów o padanym ID!";
                  }
                }
                else{
                    echo "Nie podano ID!";
                }
  
            }
            ?>
        </div>
    </div>
</div>



</body>