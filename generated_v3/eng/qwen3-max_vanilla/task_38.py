from ase import Atoms
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo
import numpy as np

# Create Cu bulk (FCC, conventional cell)
a = 3.6  # Approximate lattice constant for Cu
cu = Atoms('Cu4', positions=[[0,0,0], [0.5,0.5,0], [0.5,0,0.5], [0,0.5,0.5]], 
           cell=[a, a, a], pbc=True)
cu.calc = EMT()

# Calculate phonons with 2x2x2 supercell and 1 displacement step
N = 2
ph = Phonons(cu, EMT(), supercell=(N, N, N), delta=0.01)
ph.run()
ph.clean()

# Get dynamical matrix and vibrational frequencies
dyn = ph.dynmat()
omega = ph.get_omega().real
omega = omega[omega > 0]  # Remove zero modes

# Compute Helmholtz free energy at 300 K
thermo = HarmonicThermo(energies=omega)
F = thermo.get_helmholtz_energy(temperature=300.0)

print(f"{F:.6f}")
