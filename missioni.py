#!/usr/bin/python2

import subprocess
import os.path
import sys

print "Content-Type: text/html"
print
try:
	pwd = os.path.dirname(os.path.abspath(__file__))
	proc = subprocess.Popen(["%s/missioni-data/polygen" % pwd, "%s/missioni-data/grammar" % pwd], stdout=subprocess.PIPE)
	(out, err) = proc.communicate()
	titolo, descrizione, _ = out.splitlines()
except Exception, e:
	print e
	sys.exit(0)

print """
<!DOCTYPE html>
<html lang="it">
    <head>
        <link href='http://fonts.googleapis.com/css?family=Coda' rel='stylesheet' type='text/css'>
        <meta charset="utf-8">
        <title>Generatore di missioni di @NoTAVernello</title>
        <style TYPE="text/css">
        * {font-family: 'Coda', cursive; background-color: #000000;}
        .titolo {color: #00ffff;font-size: 200%%;}
        .autore {color: #00ff00;font-size: 200%%;}
        .descrizione {color: #007777;font-size: 200%%;}
	.bottom { position: absolute; bottom: 0;}
        </style>
    </head>
    <body>
        <div class="titolo"><h1>%s</h1></div>
        <div class="autore"><p>NoTAVernello<p></div>
        <div class="descrizione"><p>%s</p></div>
	<div class="bottom"><a href="javascript:location.reload()">Un altro!</a></div>
    </body>
</html>
""" % (titolo,descrizione)
