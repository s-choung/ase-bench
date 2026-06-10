from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Generate and relax Cu bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.05)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()

# Compute Helmholtz free energy
thermo = HarmonicThermo(vib_energies, geometry='nonlinear', symmetrynumber=1, spin=0)
F = thermo.get_helmholtz_energy(300)
print(f'Helmholtz free energy at 300K: {F:.6f} eV')
