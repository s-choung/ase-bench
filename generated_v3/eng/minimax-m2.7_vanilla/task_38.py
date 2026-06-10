from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Build Cu bulk (primitive fcc cell) and create a 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.615)
atoms *= (2, 2, 2)

# Set EMT calculator
atoms.calc = EMT()

# Compute vibrational modes (finite differences)
vib = Vibrations(atoms)
vib.run()

# Vibrational energies (eV); discard essentially zero frequencies
vib_energies = vib.get_energies()
vib_energies = vib_energies[vib_energies > 1e-6]

# Electronic (potential) energy of the static structure
potential_energy = atoms.get_potential_energy()

# Helmholtz free energy including vibrational contribution at 300 K
thermo = HarmonicThermo(vib_energies)
F = potential_energy + thermo.get_helmholtz_energy(300)

print(F)  # value in eV
