<?php

declare(strict_types=1);

$response = file_get_contents('http://flask-api');

?>

<h1>Welcome on the test page of this Docker project template</h1>

<p>This file is rendered through php-fpm. All requests to this server reach this file. The current requested endpoint is <?php echo $_SERVER['REQUEST_URI'] ?></p>

<p>The response of the flask application is <?php echo $response ?></p>


