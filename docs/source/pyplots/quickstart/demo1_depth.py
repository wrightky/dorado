"""Plot for quickstart demo 1."""
import matplotlib.pyplot as plt
from particlerouting.example_data.define_params import make_rcm_params

params = make_rcm_params()
fig = plt.figure()
ax = plt.gca()
im = ax.imshow(params.depth)
plt.title('Water Depth')
cax = fig.add_axes([ax.get_position().x1+0.01,
                    ax.get_position().y0,
                    0.02,
                    ax.get_position().height])
cbar = plt.colorbar(im, cax=cax)
plt.show()