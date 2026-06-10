from ase.calculators.emt import EMT
from ase.calculators import LJ
from ase.build import molecule
from ase.constraints import FixAtoms
from ase.geometry import Point
from ase.io import write
import numpy as np

# Build a water molecule
molecule_water = molecule('H2O')

# Add a small oxygen atom to simulate an isolated molecule
oxygen = Point(0, 0, 0)
molecule_water.add_atom(oxygen)
molecule_water.wrap = False

# Set up EMT calculator
emt = EMT(lxc=1, kpts=10)

# Set up LJ calculator
lj = LJ(r_c=4.0)

# Combine calculators
emt.set_calculator(lj)

# Apply a constraint to fix the oxygen atom
constraint = FixAtoms(indices=[1])
molecule_water.set_constraint(constraint)

# Calculate the frequencies
molecule_water.calc(emt)

# Print vibrational modes
for mode in molecule_water.vibrations:
    freq = mode.frequency
    energy = mode.energy
    print(f"Frequency: {freq:.2f} cm^-1, Energy: {energy:.6f} eV")

# Write the structure to a file
write('h2o.vasp', molecule_water)
