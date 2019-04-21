<?php 
    session_start();
                            
    if (!isset($_SESSION['qna']))
        {
            $_SESSION['qna'] = array();
            array_push($_SESSION['qna'], "Hello, may I help you ? :)");
        }

    if (!isset($_SESSION['user']))
        {
            $_SESSION['user'] = array();
        }
    
    $url = 'http://127.0.0.1:5000/';

    if (isset($_POST['inputbox']) )
        {
            if ($_POST['inputbox'] === "reset")
                {
                    $_SESSION['qna'] = array();
                    array_push($_SESSION['qna'], "Hello, may I help you ? :)");
                    $_SESSION['user'] = array();
                }
            else
                {
                    $res = findAnswer($url,$_POST);
                    array_push($_SESSION['qna'],$res); 
                    array_push($_SESSION['user'],$_POST['inputbox']);
                }
        }

    function findAnswer($url,$data) 
        {
            $ch = curl_init($url);

            curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

            $getres = curl_exec($ch);

            curl_close($ch);
            
            $finalx = json_decode($getres);

            return $finalx;
        }

        unset($_POST);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Flat ChatBox</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body>
    
    <div class="name">
        <p>
            ChaChaChatBox
        </p>    
    </div>

    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">

        <select class="select" name="algorithm" required>
            <option value="" hidden>Select Algorithm</option>
            <option value="BM">Boyer-Moore</option>
            <option value="KMP">KMP</option>
            <option value="Regex">Regex</option>
        </select>

        <div id = "container">

            <div class="gif">
                <img src="bot.gif" width = 200 height = 240 />
            </div>

            <div class="chatbox">

                <div class="chatlogs">

                            <div class="chat bot">
                                    <div class="user-pic">
                                        <!img src="1.jpg">
                                    </div>
                                    <p class="chat-message">
                                        <?php echo($_SESSION['qna'][0]); ?>
                                    </p>
                            </div>

                            <?php
                                if (!empty($_SESSION['user']) && !empty($_SESSION['qna']))
                                    {
                                        for ($x = 0 ; $x < count($_SESSION['user']) ; $x++)
                                            { ?>
                                                <div class="chat self">
                                                    <div class="user-pic">
                                                        <!img src="2.jpg">
                                                    </div>
                                                    <p class="chat-message">
                                                        <?php echo($_SESSION['user'][$x]); ?>
                                                    </p>
                                                </div>

                                                <div class="chat bot">
                                                    <div class="user-pic">
                                                        <!img src="1.jpg">
                                                    </div>
                                                    <p class="chat-message">
                                                        <?php echo($_SESSION['qna'][$x+1]->data); ?>
                                                    </p>
                                                </div>

                                        <?php  }
                                    }
                            ?>
                </div>

                <div class="chat-form">
                    <textarea name="inputbox"></textarea>
                    <button>Send</button>
                </div>

            </div>
        </div>

    </form>
    
</body>
</html>