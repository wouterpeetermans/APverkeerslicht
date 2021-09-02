<?php
  switch ($_GET["action"]) {
    case "blink":
        system("killall python3");
        system("python3 oranje-knipperen.py > /dev/null 2>&1 &");
        break;
    case "greentored":
        system("killall python3");
        system("python3 groennaarrood.py > /dev/null 2>&1 &");
        break;
    case "redtogreen":
        system("killall python3");
        system("python3 roodnaargroen.py > /dev/null 2>&1 &");
        break;
}
?>
<!doctype html>
<html lang="en">
 <head>
  <title>AP verkeerslicht</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
 </head>
 <body>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
  <a class="btn btn-warning" href='?action=blink'>knipperen</a><br />
  <a class="btn btn-danger" href='?action=greentored'>Groen naar Rood</a><br />
  <a class="btn btn-success" href='?action=redtogreen'>Rood naar Groen</a>
 </body>
</html>
