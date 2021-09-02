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
<a href='?action=blink'>knipperen</a><br />
<a href='?action=greentored'>Groen naar Rood</a><br />
<a href='?action=redtogreen'>Rood naar Groen</a>

