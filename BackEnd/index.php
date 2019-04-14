<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>ChaCha Chat-Bot</title>
    <!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<!-- Latest compiled JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="//cdn.jsdelivr.net/bootstrap.tagsinput/0.4.2/bootstrap-tagsinput.css" />
	<script src="//cdn.jsdelivr.net/bootstrap.tagsinput/0.4.2/bootstrap-tagsinput.min.js"></script>
</head>
<body>
    <div class = "container">
        <h1 class = "text-center"> 
            Cha-Cha ChatBot 1.0 
        </h1>

        <div class="row">
            <form action="<?php $_PHP_SELF ?>" method="POST">
                    <label for="inputchat">Input chat:</label>
					<input type="text" class="form-control" placeholder="input here.." id="input" name="inputbox">
					<br>
            </form>
        </div>

        <?php

            $url = 'http://127.0.0.1:5000/';
            if (isset($_POST['inputbox']))
                {
                    tembak($url,$_POST);
                    exit();
                }

            function tembak($url,$data) {
                $ch = curl_init($url);

                curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
                curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

                $getres = curl_exec($ch); // Masih dalam bentuk json

                curl_close($ch);
                
                echo ($getres);
            } 
        ?>
    </div>
</body>
</html>