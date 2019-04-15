<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Chaca Chat-Bot</title>
</head>
<body>
    <form action="frontend.php" method="post">
    question: <input type="text" name="quest" value=><br>
    <input type="submit">
    </form>

    <?php
        $question = $_POST["quest"];
        if (isset($question))
            {
                echo $question;
            };
    ?>
</body>
</html>