from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase.build import bulk

# Create bulk Cu
atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

# Optimize structure
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='vib')
vib.run()
frequencies = vib.get_frequencies()  # in cm^-1
vib.clean()

# Get vibrational energies (in eV)
energies = vib.get_energies()

# Create harmonic thermodynamics object
thermo = HarmonicThermo(vib_energies=energies, temperature=300)

# Calculate Helmholtz free energy (excluding electronic energy)
F_vib = thermo.get_helmholtz_energy()
print(f"{F_vib:.6f}")
