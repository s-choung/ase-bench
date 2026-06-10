import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Bulk Cu (fcc) and geometry optimization (cell + positions)
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01, steps=200)

# Supercell for phonon calculation
supercell = atoms * (2, 2, 2)
supercell.calc = EMT()

# Vibrational frequencies
vib = Vibrations(supercell, name='cu_vib')
vib.run()
freqs = vib.get_frequencies()
vib.clean()

# Helmholtz free energy at 300 K (eV)
thermo = HarmonicThermo(vib_frequencies=freqs)
F = thermo.get_helmholtz_energy(temperature=300)
print(f'Helmholtz free energy (300 K): {F:.6f} eV')
