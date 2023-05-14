<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Formularz</title>
    <link rel="stylesheet" href="style6.css">
  </head>
  <body>
    <script>
      var passwordInput = document.getElementById("password");
      passwordInput.value = passwordInput.value.replace(/./g, "*");
      function hideCharacters(input) {
        var value = input.value;
        var length = value.length;
        var hiddenValue = "";
        for (var i = 0; i < length; i++) {
          hiddenValue += "*";
        }
      input.value = hiddenValue;
      }
    </script>

    <h1 class="formul"> Form </h1>
    <div class="maindiv">
    <form action="check.php" method="post">

    <div class="container">
      
      <div class="col">
        <p>Login: </p>
        <p>Hint: palina </p>
      </div>

      <div class="col">
        <input type="text" name="login" class="window" value="palina">
      </div>

    </div>

    <div class="container">
      
      <div class="col">
        <p>Password: </p>
        <p>Hint: 1234 </p>
      </div>

      <div class="col">
        <input type="text" name="password" id="password" class="window" oninput="hideCharacters(this)" value="1234">
      </div>

    </div>

    <div class="container">

      <div class="col">
        <p>Name: </p>
      </div>

      <div class="col">
        <input type="text" name="imie" pattern="[A-Za-z]{2,20}([\- ])?([A-Za-z]{2,20})?([\- ])?([A-Za-z]{2,20})?" title="Letters only!" class="window" value="Palina">
      </div>

    </div>

    <div class="container">

      <div class="col">
        <p>Surname: </p>
      </div>

      <div class="col">
        <input type="text" name="nazwisko" pattern="[A-Za-z]{2,20}([\- ])?([A-Za-z]{2,20})?([\- ])?([A-Za-z]{2,20})?" title="Letters only!" class="window" value="Sauranskaya">
      </div>

    </div>

    <div class="container">

      <div class="col">
        <p>Sex: </p>
      </div>

      <div class="col">
        Female&nbsp<input type="radio" name="plec" value="k" checked>&nbspMale&nbsp<input type="radio" name="plec" value="m">
      </div>

    </div>

    <div class="container">

      <div class="col">
        <p>Date of birth: </p>
      </div>

      <div class="col">
        <input type="date" name="urodziny" class="window" value="2001-12-10">
      </div>

    </div> 

 
    <div class="container">

      <div class="col">
        <p>Phone number: </p>
      </div>

      <div class="col">
        +48 <input type="text" name="telefon" pattern="([0-9]{3})([ \-]{1,3})?([0-9]{3})([ \-]{1,3})?([0-9]{3})" title="9 cyfr" class="window" value="111111111">
      </div>

    </div>

    <div class="container">

      <div class="col">
        <p>Driver's licence: </p>
      </div>

      <div class="col">
        <input type="checkbox" name="prawojazdy" value="tak" checked>
      </div>

    </div>

    <div class="container">

      <div class="col">
        <p>City: </p>
      </div>

      <div class="col">
        <select name="miasto" class="window">
							<option name="Warsaw" selected>Warszawa</option>
							<option name="Kraków">Kraków</option>
							<option name="Wrocław">Wrocław</option>
							<option name="Łódź">Łódź</option>
							<option name="Poznań">Poznań</option>
							<option name="Gdańsk">Gdańsk</option>
							<option name="Szczecin">Szczecin</option>
							<option name="Bydgoszcz">Bydgoszcz</option>
							<option name="Lublin">Lublin</option>
							<option name="Białystok">Białystok</option>
							<option name="Katowice">Katowice</option>
        </select>
      </div>

    </div>


    <div class="container">

      <div class="col">
        <p>Remarks: </p>
      </div>

      <div class="col">
        <textarea name="uwagi" rows="1" cols="30" class="window"></textarea>
      </div>

    </div>
  <div class="cl_sub">
    <input type="reset" name="p1" value="Clear" class="window col"> <input type="submit" name="p2" value="Log in" class="window col">
  </div>
  </form>
    </div>

  <a href="index.html">Back</a>
  
  </body>
</html>