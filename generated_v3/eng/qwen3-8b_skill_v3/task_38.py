from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk structure
atoms = Atoms('Cu', cell=(3.6, 3.6, 3.6), pbc=True)
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Set EMT calculator and optimize
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()

# Compute Helmholtz free energy at 300K
thermo = HarmonicThermo(frequencies, atoms, geometry='nonlinear', symmetry_number=1)
helmholtz_energy = thermo.get_helmholtz_energy(temperature=300)

print(f'Helmholtz free energy: {helmholtz_energy:.6f} eV')
