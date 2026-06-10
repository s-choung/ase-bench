import numpy as np
from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Setup H2O molecule and EMT calculator
atoms = molecule('H2O')
atoms.set_calculator(EMT())

# Relax the structure to find the equilibrium geometry
from ase.optimize import BFGS
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational modes
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies() # in eV

# Conversion factor: 1 eV = 8065.54 cm^-1
ev_to_cm = 8065.54

print(f"{'Mode':<10} {'Energy (eV)':<15} {'Frequency (cm^-1)':<20}")
for i, freq in enumerate(frequencies):
    print(f"{i:<10} {freq:<15.4f} {freq * ev_to_cm:<20.2f}")
