from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Build and relax bulk Cu
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Calculate vibrational modes
vib = Vibrations(atoms, name='cu_bulk_vib')
vib.run()
vib.summary()

# Compute Helmholtz free energy at 300K
vib_energies = vib.get_energies()
thermo = HarmonicThermo(vib_energies=vib_energies, atoms=atoms)
helmholtz_A = thermo.get_helmholtz_energy(temperature=300)

# Output result
print(f"\nHelmholtz free energy at 300K: {helmholtz_A:.4f} eV")

# Clean up temporary vibration files
vib.clean()
