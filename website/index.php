<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>VSAS Software</title>
<link rel="shortcut icon" href="/images/favicon.ico" />
    <style type="text/css">
        html,body {
            margin: 0;    /* must */
            padding: 0;   /* must */
            height: 100%; /* must */
        }
        body {
            width: 1000px;
            margin: 0 auto;
            /*background-color: #A0A0A0;*/
           background-color: #000000;
        }
        #header {
            background-image: url('images/layout/header.png');
            width: 1000px;
            height: 200px;
        }
        #content {
            background-color: #FFFFFF;
            /*background-color: #4d4b4b;*/
            width: 840px;
            position: relative;
            margin-top: 5px;
            padding: 80px 80px 200px 80px; /* set bottom height to height of footer */
            height: auto !important;
            height: 100%;
            min-height: 100%;
            border-style: solid;
            border-width: medium;
            border-color: #00d800;
        }
        #container {
           position: relative; /* must have to make footer stay at bottom */
           margin: 0px auto;     /*centers in all browsers but IE5 */
           width: 1000px;      /* set to width of your site */
           height: auto !important; /* sets automatic height for browsers but IE */
           height: 100%;            /* only used by IE for automatic height */
           min-height: 100%;        /* sets automatic height for browsers but IE */
        }
        #footer {
            background-image: url('images/layout/footer.png');
            position: absolute;  /* must have for hugging to bottom */
            bottom: 0;           /* must have for hugging to bottom */
            width: 867px;
            height: 140px;       /*must have to appear */
            padding: 50px 33px 10px 100px;
        }
        /*-- -- -- -- -- -- -- -- -- -- ---- -- -- -- --*/
       .button {
            float: left;
            margin-top: 10px;
        }
        
        #home {
            display: block;
            padding: 30px;
        }
        #home-button {
            margin-left: 150px;
            opacity: 1.0;
            border-bottom: 1px solid #00d800;
        }
        #team {
            display: none;
            padding: 30px;
        }
        #team-button {
            opacity: 0.4;
            border-bottom: 1px solid #00d800;
        
        }
        #download {
            display: none;
            padding: 30px;
        }
        #download-button {
            opacity: 0.4;
            border-bottom: 1px solid #00d800;
        
        }
        #manual {
            display: none;
            padding: 30px;
        }
        #manual-button {
            opacity: 0.4;
            border-bottom: 1px solid #00d800;
        
        }
        #login {
            display: none;
            padding: 30px;
        }
        #login-button {
            opacity: 0.4;
            border-bottom: 1px solid #00d800;
        
        }
        .clear {
            clear: both;
        }
    </style>
        <!--[if lt IE 7]> 
            <style type="text/css">
                body, #container {
                height: 100%;
                }
            </style>
        <![endif]-->

    <script type="text/javascript" src="js/jquery.js"></script>

    <script type="text/javascript">
    
        $(function(){
            $("#home-button").css({
                opacity: 1,
                borderWidth: 5
            })
            
            $("#team-button").css({
                opacity: 0.4
            });
            $("#download-button").css({
                opacity: 0.4
            });
            $("#manual-button").css({
                opacity: 0.4
            });
        
            $("#container div.button").click(function(){
                
                $clicked = $(this);
                
                // if the button is not already "transformed" AND is not animated
                if ($clicked.css("opacity") != "1" && $clicked.is(":not(animated)")) {
                    
                    $clicked.animate({
                        opacity: 1,
                        borderWidth: 5
                    }, 300 );
                    
                    // each button div MUST have a "xx-button" and the target div must have an id "xx" 
                    var idToLoad = $clicked.attr("id").split('-');
                    
                    //we search trough the content for the visible div and we fade it out
                    $("#content").find("div:visible").fadeOut("fast", function(){
                        //once the fade out is completed, we start to fade in the right div
                        $(this).parent().find("#"+idToLoad[0]).fadeIn();
                    })
                }
                
                //we reset the other buttons to default style
                $clicked.siblings(".button").animate({
                    opacity: 0.4,
                    borderWidth: 1
                }, 300 );
                
            });
        });
        
    </script>

</head>
<body><!-- -- -- -- -- -- -- -- -- -- --- -- body -- -- -- -- -- -- -- -- -- -- --- -->
    <div id="header">
        
    </div>
    
    <div id="container">
        <div id="home-button" class="button">
            <img src="/images/layout/menu_home.jpg" alt="home" class="button" />
        </div>
        <div id="team-button" class="button">
            <img src="/images/layout/menu_team.jpg" alt="team" class="button" />
        </div>

        <div id="download-button" class="button">
            <img src="/images/layout/menu_download.jpg" alt="download" class="button" />
        </div>
        <div id="manual-button" class="button">
            <img src="/images/layout/menu_manual.jpg" alt="manual" class="button" />
        </div>
        
        <div class="clear"></div>
        
        
        <div id="content">
            <div id="home">
                home content here
    
            </div>
            <div id="team">
                Team content here
    
            </div>
            <div id="download">
                download content here
    
            </div>
            <div id="manual">
                manual content here
    
            </div>
        </div>
<!--        <div id="footer">
</div> -->
    </div>

</body>
</html>
