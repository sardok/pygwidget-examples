from pygwidget.speedometer import Speedometer
from base import run_sprite


sm = Speedometer(0, 0, scales=range(0, 7), start_degree=315, stop_degree=225, label_height=15)
run_sprite(sm)
