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
    <link rel="stylesheet" type="text/css" media="screen" href="style.css" />
</head>

<body>
    <div class = "container">

        <div class="jumbotron">
            <h1 class="display-3">Cha Cha ChatBot</h1>
            <p class="lead"></p>Oleh : IP 4 Menanti</p>
        </div>

        <div class="row">
            <form action="<?php $_PHP_SELF ?>" method="POST">

                <div class="col-md-4 col-sm-4">
                    <label for="algorithmsel">Algorithm</label>
                    <select class="select" id="select" form="main-form" name="algorithm">
						<option>Boyer-Moore</option>
						<option>KMP</option>
						<option>Regex</option>
					</select>
                    <br>
                </div>
                
                <div class="col-md-8 col-md-8">
                    <label for="output">CHATBOX</label>
                    <div class="outbox">
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
                    <br>
                </div>

                <div class="col-md-8 col-md-8">
                    <div class="inputchat">
                        <label for="inputchat">Text me : </label>
                        <textarea input="text" name="inputbox" cols="100" rows="5"></textarea>
                        <br>
                    </div>
                    <input type="submit" class="button_css">
                </div>

             </form>
        </div>

    </div>
</body>

</html>

