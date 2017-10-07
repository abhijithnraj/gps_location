<?php 
$gps=$_GET["gps"];
//echo $gps;
$word="sudo python2 find.py '".$gps."'";
//echo $word;
exec($word,$output);
//exec("sudo python2 find.py",$output);
echo $output[0];
//echo $word;

?>
