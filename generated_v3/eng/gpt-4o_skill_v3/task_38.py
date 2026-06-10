from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Build Cu bulk and assign the calculator
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()

# Compute Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300)
print(f"Helmholtz free energy at 300K: {F:.5f} eV")

# Clean up files
vib.clean()
