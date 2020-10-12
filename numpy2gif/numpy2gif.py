import numpy as np
from array2gif import write_gif

__all__ = ["gif_gray"]

def gif_gray(arr, fname, fps=10):
    assert arr.ndim == 3, "Array must be 3D"

    arr_rgb = np.copy(arr).astype(np.float32)
    arr_rgb -= arr_rgb.min()
    arr_rgb /= arr_rgb.ptp()
    arr_rgb *= 255

    arr_rgb = np.repeat(arr_rgb[:, None], 3, 1)

    write_gif(arr_rgb.astype(np.uint8), fname, fps)
