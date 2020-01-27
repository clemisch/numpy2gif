This module only has one function: `gif_gray`. Use it to create a grayscale GIF
from a 3D numpy array. 

```python
import numpy as np
from numpy2gif import gif_gray

# generate 3D data
# gif will play over 0th axis
data = np.random.normal(loc=0, scale=100, size=(30, 40, 50))

# generate gif file
# input will be scaled to [0, 1] automatically
# `fname` can be relative or absolute
gif_gray(data, "hello_world.gif", fps=10)
```

The dtype and value range of the array don't matter. 

Keep in mind that the array values are scaled **linearly** to [0, 1], so you 
won't see much if your data is not linearly scaled in the first place.
