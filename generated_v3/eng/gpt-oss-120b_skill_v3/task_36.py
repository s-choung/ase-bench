from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Ag FCC bulk (initial lattice constant from ASE default)
base = bulk('Ag', 'fcc')
base.calc = EMT()
a0 = base.get_cell_lengths_and_angles()[0]   # cubic lattice constant

# 7 scaling factors from -5% to +5%
scales = np.linspace(0.95, 1.05, 7)

volumes, energies = [], []
for s in scales:
    atoms = base.copy()
    atoms.set_cell(atoms.get_cell() * s, scale_atoms=True)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

# Birch–Murnaghan EOS fit
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B_eV = eos.fit()                     # B in eV/Å³
a_eq = v0 ** (1/3)                           # cubic lattice constant
B_GPa = B_eV * 160.21766208                  # 1 eV/Å³ = 160.21766208 GPa

print(f'Equilibrium lattice constant: {a_eq:.4f} Å')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
