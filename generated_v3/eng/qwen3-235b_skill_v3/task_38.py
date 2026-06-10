from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Optimize structure
from ase.optimize import BFGS
BFGS(atoms, fmax=0.01).run()

# Compute vibrations
vib = Vibrations(atoms, name='vib')
vib.run()

# Extract vibrational energies in eV
vib_energies = vib.get_energies()  # in meV
vib_energies_eV = vib_energies / 1000.0  # convert to eV

# Compute Helmholtz free energy at 300 K
thermo = HarmonicThermo(vib_energies=vib_energies_eV, potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300)

print(f"{F:.6f}")
vib.clean()
