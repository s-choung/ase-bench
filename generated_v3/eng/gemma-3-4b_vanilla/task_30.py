from ase.md.verlet import VelocityVerlet
from ase.md.npt import NPTBerendsen
from ase.calculators import EMT
from ase.constraints import FixAtOrigin
from ase.units import angstrom, bar, eV, fs, K
import numpy as np

# Create Cu FCC 3x3x3 supercell
a = 3.615 * angstrom
cell = np.array([[a, 0, 0],
                  [0, a, 0],
                  [0, 0, a]])
atoms = ASE.Atom(positions=np.array([[0,0,0], [1,1,0], [2,1,0], [1,2,1], [2,2,1], [3,2,1], [1,3,2], [2,3,2], [3,3,2]]),
                  numbers=[29])
slab = ASE.Structure(cell, atoms)

# Set calculator to EMT
slab.calc = EMT(xc='LDA')

# Apply constraint to fix at origin
constraint = FixAtOrigin()
slab.set_constraint(constraint)

# MD parameters
timestep = 5 * fs
taut = 100 * units.fs
taup = 1000 * units.fs
nsteps = 200

# NPT simulation
md = VelocityVerlet(slab, dt=timestep)
npt = NPTBerendsen(slab, taup=taup, taut=taut, target_density=1.0)
md.attach(npt)

# Run simulation
npt.run(nsteps)

# Print initial and final cell volume and pressure
print("Initial cell volume:", slab.get_cell_volume())
print("Final cell volume:", slab.get_cell_volume())
print("Final pressure:", npt.pressure)
