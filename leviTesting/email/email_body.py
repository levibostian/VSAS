"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN"
+"http://www.w3.org/TR/html4/strict.dtd\">
+"<html>
   +"<head>
        +"<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">
        +"<style type=\"text/css\">
            +"body {
                +"margin: 0 auto;
                +"padding: 0;
                +"width: 600px;
                +"height: 100%;
                +"background-color: #FFFFFF;
                +"text-align: center;
            +"}
            +"#container {
				+"height: 100%;
				+"width: 600px;
			+"}
		+"</style>
    +"</head>
    +"<body>
		+"<h1 style=\"color:"+'"'+self.alertLevel.toLower()+'"'+"; font-size: 50px;\">"+'"'+self.alertLevel+'"'+" ALERT</h1>
		+"<h3>VSAS Motion Detected</h3>
		
		+"<!-- Img link below, make source to dropbox photo link -->
		+"<img src="+'"'+self.dbPhotoLink+'"'+" width=\"500px;\" height=\"400px;\" />
		
		+"<table border=0 style=\"margin: 0 auto;\">
			+"<tr>
				+"<th colspan=3>-Motion Details-</th>
			+"</tr>
			+"<tr>
				+"<th>Duration:</th>
				+"<td colspan=2>"+'"'+self.duration+'"'+"</td>
			+"</tr>
			+"<tr><td colspan=3></td></tr>
			+"<tr>
				+"<th colspan=3>Video Footage Link</th>
			+"</tr>
			+"<tr>
				+"<td colspan=3><a href="+'"'+self.dbVidLink+'"'+">"+'"'+self.dbVidLink+'"'+"</a></td>
			+"</tr>
		+"</table>
		+"<h1> </h1>
    +"</body>
+"</html>"
