import matplotlib
print(matplotlib.__version__)

# Pyplot:
from matplotlib import pyplot as plt
import numpy as np

# Draw a diagram from (0,0) to (6,250)
xpoints = np.array([0,6])
ypoints = np.array([0,250])

# plot your points:
plt.plot(xpoints, ypoints)
# display graph with your points:
plt.show()
