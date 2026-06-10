from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Initial Ag FCC bulk
atoms = bulk('Ag', 'fcc')
initial_cell = atoms.get_cell()

volumes, energies = [], []

# +/-5% lattice constant variation (7 points)
for x in np.linspace(0.95, 1.05, 7):
    scaled = atoms.copy()
    scaled.set_cell(initial_cell * x, scale_atoms=True)
    scaled.calc = EMT()
    volumes.append(scaled.get_volume())
    energies.append(scaled.get_potential_energy())

# Birch-Murnaghan EOS fit
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, _, B = eos.fit()

# Equilibrium lattice constant (FCC: v0 = a0³)
a0 = v0 ** (1/3)

# Convert bulk modulus to GPa (1 eV/Å³ = 160.21766208 GPa)
B_gpa = B * 160.21766208

# Print results
print(f'Equilibrium lattice constant: {a0:.3f} Å')
print(f'Bulk modulus: {B_gpa:.1f} GPa')
