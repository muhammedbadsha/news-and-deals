<?php
ob_start();
?>
<html>
	<head>
	</head>
	<body>
		<div><b>Name</b>: <?php echo $values["name"]; ?></div>
		<div><b>E-mail</b>: <?php echo $values["email"]; ?></div>
		<div><b>Message</b>: <?php echo nl2br($values["message"]); ?></div>
	</body>
</html>
<?php
$content = ob_get_contents();
ob_end_clean();
return($content);
?>	