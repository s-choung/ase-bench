from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create initial Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Set calculator
atoms.calc = EMT()

# Generate lattice constants around guess
n_steps = 11
volumes = []
energies = []
for a in np.linspace(3.3, 3.9, n_steps):
    atoms.set_cell([a, a, a], scale_atoms=True)
    atoms.set_pbc([True, True, True])
    energy = atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(energy)

# Fit equation of state
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert bulk modulus to GPa (1 eV/A^3 = 160.21766208 GPa)
B_GPa = B * 160.21766208

print(f'Equilibrium volume: {v0:.4f} Ang^3')
print(f'Bulk modulus: {B:.4f} eV/A^3 ({B_GPa:.2f} GPa)')
