from pygwidget.speedometer import Speedometer
from base import run_sprite

sm = Speedometer(0, 0, scales=range(0, 190, 10), start_degree=0, stop_degree=180, label_height=15)
run_sprite(sm)
