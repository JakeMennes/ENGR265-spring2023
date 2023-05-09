import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('harrisonburg-map.png'))
imgplot = plt.imshow(img)

plt.scatter([1789, 1011, 1277, 1409, 953, 1060,220,729,986], [48, 1074, 1205, 1302, 774, 521,1695,841,1654],color='red')

plt.show()
