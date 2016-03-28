import os.path
from pygwidget.speedometer import Speedometer
from base import run_sprite

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
background = os.path.join(package_dir, 'assets', 'scale_background1.png')
sm = Speedometer(0, 0, scales=range(0, 190, 10), start_degree=0, stop_degree=180, label_height=15,
                 background_image_path=background, scale_anchor_x=200, scale_anchor_y=250,
                 scale_radius=200)
run_sprite(sm)
