from ase.md.npt import NPTBerendsen
from ase.calculators import EMT, LJ
from ase.build import fcc111
import numpy as np

# Create an Al FCC 2x2x2 supercell
cell = fcc111('Al', size=(2, 2, 2), a=4.050)

# Set up the calculator
calc = EMT()
cell.set_calculator(calc)
calc.xc='LDA'
calc.kpts=(2,2,2)

# Add LJ potential
lj = LJ(r_c=4.050)
cell.set_calculator(lj)


# MD simulation parameters
temp = 500.0
pressure = 10.0
nsteps = 100

# Set up NPTBerendsen
md = NPTBerendsen(box=cell, temp=temp, pressure=pressure, nsteps=nsteps)

# Run the simulation
md.run()

# Print initial and final cell volume
print(f"Initial cell volume: {cell.get_volume()}")
print(f"Final cell volume: {cell.get_volume()}")
