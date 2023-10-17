This module only has one function: `gif_gray`. Use it to create a grayscale GIF
from a 3D numpy array. 

```python
import numpy as np
from numpy2gif import gif_gray

# generate 3D data
# gif will play over 0th axis
data = np.random.normal(loc=0, scale=100, size=(30, 100, 200))

# generate gif file
# input will be scaled to [0, 1] automatically
# `fname` can be relative or absolute
gif_gray(data, fname="hello_world.gif", fps=10)
```

generates file `hello_world.gif`:

![example](https://github.com/clemisch/numpy2gif/assets/5190547/e53bf41e-0357-4bfa-bf82-224dfebba6fd)




Keep in mind that the input array is scaled **linearly** to [0, 1], so you 
won't see much if your data is not linearly scaled in the first place.
