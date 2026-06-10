from ase import Atoms
from ase.calculators.emt import EMT
from ase.units import kB
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create FCC copper bulk
atoms = Atoms('Cu', cell=[[0, 1, 1], [1, 0, 1], [1, 1, 0]], pbc=True)
atoms *= (2, 2, 2)
atoms.calc = EMT()

# Relax structure
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms, name='cu-vib')
vib.run()
vib.summary(log=None)

# Get vibrational energies
energies = vib.get_energies()

# Compute Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies=energies)
F = thermo.get_helmholtz_energy(temperature=300, verbose=False)

print(f"Helmholtz free energy at 300K: {F:.6f} eV")

# Clean up
vib.clean()
