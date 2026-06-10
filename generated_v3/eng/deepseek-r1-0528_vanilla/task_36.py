from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Initial lattice constant and percentage range
a0 = 4.09
n_points = 7
range_percent = 0.05
a_values = np.linspace(a0 * (1 - range_percent), a0 * (1 + range_percent), n_points)

# Calculate energies for each lattice constant
volumes = []
energies = []
for a in a_values:
    atoms = Atoms('Ag', positions=[[0, 0, 0]], cell=[a, a, a], pbc=True, latticeconstant=a)
    atoms *= (2, 2, 2)  # Create 2x2x2 supercell for FCC
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit EOS and extract properties
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B, _ = eos.fit()
a_eq = (4 * v0)**(1/3)  # Volume per fcc atom: a^3/4 => a = (4*v0)^(1/3)
B_GPa = B / 1e-1  # Convert from eV/A^3 to GPa (1 eV/A^3 = 160.21766208 GPa => ASE uses eV/Å³, so 1eV/Å³=160.217...GPa. But let's use correct factor)

print(f'Equilibrium lattice constant: {a_eq:.4f} Å')
print(f'Bulk modulus: {B_GPa * 160.21766208:.2f} GPa')  # Convert eV/Å³ to GPa
