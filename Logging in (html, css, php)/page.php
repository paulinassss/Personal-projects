<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style6.css">
    <title>Strona.php</title>
</head>
<body>
    <?php
        session_start();
        if(array_key_exists('logout', $_POST)) {
            session_destroy();
            header("Location: index6.php");
        }
        if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
            header("location: index6.php");
            exit;
        }
        else { ?>
            <div> Logged in successfully! </div> 
            <?php 
            if(isset($_SESSION["data"])){
                $dane = $_SESSION["data"]; ?>
                <div> Data: </div>
                <div>Name:  <?php echo $dane["Imie"]; ?> </div>
                <div> Surname: <?php echo $dane["Nazwisko"]; ?> </div>
                <?php if ($dane["Plec"] == "k"){ ?>
                    <div> Sex: Female </div> <?php }
                if ($dane["Plec"] == "m"){ ?>
                    <div> Sex: Male </div> <?php } ?>
                <div> Date of birth: <?php echo $dane["Data urodzenia"]; ?> </div>
                <div> Phone number: <?php echo $dane["Numer telefonu"]; ?> </div>
                <?php if(isset($dane['prawojazdy']) && $dane['Prawo jazdy'] == 'tak'){ ?>
                    <div> Driver's licence: Yes </div>
                <?php }
                else{ ?>
                    <div> Driver's licence: No </div>
                <?php } ?>
                <div> City: <?php echo $dane["Miasto"]; ?> </div>

            <?php } 
            else{
                echo "User is not logged in!";
            }
        }
    ?>

    <form method="post">
        <div class="cl_sub">
            <input type="submit" name="logout" class="window" value="Log out">
        </div>
    </form>
</body>
