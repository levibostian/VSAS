<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>VSAS Software</title>
        <link rel="shortcut icon" href="/images/favicon.ico" />
        <style type="text/css">
            html, body {
                margin: 0; /* must */
                padding: 0; /* must */
                height: 100%; /* must */
            }
            body {
                width: 1000px;
                margin: 0 auto;
                /*background-color: #A0A0A0;*/
                background-color: #000000;
            }
            #header {
                background-image: url('/images/layout/header.png');
                width: 1000px;
                height: 200px;
            }
            #content {
                background-color: #FFFFFF;
                /*background-color: #4d4b4b;*/
                width: 840px;
                position: relative;
                margin-top: 5px;
                padding: 80px 80px 100px 80px; /* set bottom height to height of
                 * footer */
                height: auto !important;
                height: 100%;
                min-height: 100%;
                border-style: solid;
                border-width: medium;
                border-color: #00d800;
            }
            #container {
                position: relative; /* must have to make footer stay at bottom */
                margin: 0px auto; /*centers in all browsers but IE5 */
                width: 1000px; /* set to width of your site */
                height: auto !important; /* sets automatic height for browsers
                 * but IE */
                height: 100%; /* only used by IE for automatic height */
                min-height: 100%; /* sets automatic height for browsers but IE */
            }
            #footer {
                background-image: url('images/layout/footer.png');
                position: absolute; /* must have for hugging to bottom */
                bottom: 0; /* must have for hugging to bottom */
                width: 867px;
                height: 140px; /*must have to appear */
                padding: 50px 33px 10px 100px;
            }
            /*-- -- -- -- -- -- -- -- -- -- ---- -- -- -- --*/

        </style>
        <!--[if lt IE 7]>
        <style type="text/css">
        body, #container {
        height: 100%;
        }
        </style>
        <![endif]-->

        <script type="text/javascript" src="js/jquery.js"></script>

    </head>
    <body>
        <a href="/index.php" ><div id="header"></div>
        </a>
        <div id="container">

            <?php
            $id = $_GET["id"];
            $path = $_GET["path"];
            $url = "https://dl.dropboxusercontent.com/1/view/" . $id . "/Apps/fileUploader_linkCreator/fileUploader_linkCreator/" . $path;
            // $dropboxVidURL = "https://dl.dropboxusercontent.com/1/view/o806ukymfnn4fov/Apps/fileUploader_linkCreator/fileUploader_linkCreator/golf-testVid.mov";
            // http://vsas.com/video/index.php?id=d4vx3mhvrsc9htt&path=golf-testVid.mov
            ?>
            <div id="content">
                <center>
                    <video width="700" height="400" controls>
                        <source src="<?php echo $url; ?>" type="video/webm">
                        <object data="<?php echo $url; ?>" width="700" height="400">
                        <embed src="<?php echo $url; ?>" width="700" height="400">
                        </object>
                    </video>
                    <a href="<?php echo $url; ?>" target="_blank" ><img src="/images/layout/download.png" /></a>
                </center>
            </div>
        </div>

    </body>
</html>
