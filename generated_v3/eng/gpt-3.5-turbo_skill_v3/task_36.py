import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Create FCC Ag bulk structure
atoms = bulk('Ag', 'fcc', a=4.09)
atoms.calc = EMT()

# Vary lattice constant and calculate energies
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 7):
    atoms.set_cell(atoms.get_cell() * x, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit with Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert lattice constant to GPa
B_GPa = B / 160.217733  # Conversion factor from eV/Å³ to GPa

print(f'Equilibrium lattice constant: {v0**(1/3):.4f} Å')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
