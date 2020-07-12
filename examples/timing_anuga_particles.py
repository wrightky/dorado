"""Example of the workflow with gridded anuga output data"""

import numpy as np
from particlerouting.routines import time_plots
from particlerouting.particle_track import params

# load some variables from a deltarcm output so stage is varied
data = np.load('ex_anuga_data.npz')

# pull depth and stage from that data
depth = data['depth']
qx = data['qx']
qy = data['qy']

# create params and then assign the parameters
params = params()

# define the params variables
params.depth = depth
params.stage = depth  # using depth as stand-in for stage in this example
params.qx = qx
params.qy = qy

params.seed_xloc = list(range(20,30))
params.seed_yloc = list(range(48,53))
params.Np_tracer = 50
params.dx = 50.
params.theta = 1.0
params.model = 'Anuga'

np.random.seed(0)
# Apply the parameters to run the particle routing model
# using steady (time-invariant) plotting routine
time_plots(params, 50, 'timing_anuga_example')
