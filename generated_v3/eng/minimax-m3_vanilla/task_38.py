from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.thermo.harmonic import HarmonicThermo
from ase.vibrations import Vibrations
import numpy as np

# Setup Cu bulk (FCC)
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=1e-3)

# Build supercell for vibrational analysis
sc = atoms.repeat((2, 2, 2))
sc.calc = EMT()
BFGS(sc).run(fmax=1e-3)

# Compute vibrational modes (Hessian by finite differences)
vib = Vibrations(sc, delta=0.01)
vib.run()

# Vibrational energies in eV (filter out non-physical / acoustic modes)
ve = vib.get_energies()
ve = ve[ve > 0]

# Helmholtz free energy at 300 K
thermo = HarmonicThermo(ve, energy=0.0)
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Vibrational modes used: {len(ve)}")
print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
