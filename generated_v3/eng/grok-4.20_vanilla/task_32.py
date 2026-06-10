from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create H2O molecule
atoms = Atoms('H2O',
              positions=[[0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0],
                         [0.8, 0.6, 0.0]],
              calculator=EMT())

# Optimize geometry (simple relaxation)
from ase.optimize import BFGS
dyn = BFGS(atoms, logfile=None)
dyn.run(fmax=0.01)

# Compute vibrations
vib = Vibrations(atoms, name='h2o_vib', delta=0.01)
vib.run()

# Get and print frequencies
print("Vibrational modes of H2O:")
for i, freq in enumerate(vib.get_frequencies()):
    energy_ev = vib.get_energies()[i]
    print(f"Mode {i+1}: {freq:.2f} cm^-1, {energy_ev:.6f} eV")

vib.clean()
