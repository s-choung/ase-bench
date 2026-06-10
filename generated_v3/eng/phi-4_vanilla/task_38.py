from ase.build import bulk
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import kB
from ase.phonons import Phonons
from ase.utils import paropen

# Create a Cu bulk structure
cu = bulk('Cu', 'fcc', a=3.6)

# Set up the calculator
calc = EMT()
cu.set_calculator(calc)

# Set up the phonon calculation
phonon = Phonons(cu, supercell=(2, 2, 2), proto=[1, 2, 3, 4])
phonon.run()

# Compute vibrational frequencies
frequencies = phonon.get_frequencies()

# Filter out imaginary frequencies (negative values)
real_frequencies = frequencies[frequencies > 0]

# Compute thermodynamic quantities
thermo = phonon.get_thermo()

# Calculate Helmholtz free energy at 300K
T = 300.0
F = thermo.get_f('F')(T)  # in Hartree

# Convert to eV
F_ev = F * 27.2114

# Print the result
print(f"Helmholtz free energy at 300K: {F_ev:.4f} eV")
