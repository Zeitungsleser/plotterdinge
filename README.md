# Plotterdinge

Diese Repo enthält alles mögliche rund um Plotter. Entwicklet im temporaerhaus.

test.py erzeugt eine .hpgl Datei, die verschiedene parametrisierte kurven zeichnet.

.hpgl Dateien plottet man mit folgendem Befehl `cat <document>.hpgl | pv --quite --rate-limit 100 > /dev/ttyUSB0`
