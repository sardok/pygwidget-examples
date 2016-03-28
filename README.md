### pygwidget-examples

Various examples that use [PygWidget](https://github.com/sardok/PygWidget).

#### Install requirements

```
virtualenv env
source env/bin/active
pip install -r requirements.txt
```


#### Speedometer

Speedometer examples could be directly run via `python` command, e.g.:

`python examples/speedometer1.py`

Examples:

* speedometer1: Basic usage with no background or indicator image. Uses pygame drawing functions only, for indicator and labels.
* speedometer2: Basic usage as in speedometer1 where circle angle beyond 180 degree.
* speedometer3: Pygame drawing function for indicator and labels, background image is given.
* speedometer4: Pygame drawing function for labels, indicator and background image is given.
* speedometer5: Speedometer circle is beyond 180 degree and indicator image is given.
* speedometer6: Better quality  background and indicator image, labels are kept for debugging.
* speedometer7: Same as 6th example where labels are removed.

