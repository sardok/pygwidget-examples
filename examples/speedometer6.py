import os.path
from pygwidget.speedometer import Speedometer
from base import run_sprite

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
background = os.path.join(package_dir, 'assets', 'scale_background1.png')
indicator = os.path.join(package_dir, 'assets', 'indicator_5x200.png')
sm = Speedometer(0, 0, scales=range(0, 250, 10), start_degree=330, stop_degree=210, label_height=15,
                 indicator_image_path=indicator)
run_sprite(sm)
