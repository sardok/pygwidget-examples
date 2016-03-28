import os.path
from pygwidget.speedometer import Speedometer
from base import run_sprite

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
background = os.path.join(package_dir, 'assets', 'high-speed-speedometer-background.png')
indicator = os.path.join(package_dir, 'assets', 'high-speed-speedometer-indicator.png')
sm = Speedometer(0, 0, scales=range(0, 220, 20), start_degree=325, stop_degree=215,
                 scale_anchor_x=560, scale_anchor_y=474, background_image_path=background,
                 indicator_image_path=indicator, indicator_anchor_height=298)
run_sprite(sm, size=(1024, 1024))
