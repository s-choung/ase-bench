import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# FCC Ag bulk
a0 = 4.09  # initial lattice constant (Å)
atoms = bulk('Ag', 'fcc', a=a0)
atoms.calc = EMT()

volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(a.get_cell() * scale, scale_atoms=True)
    energies.append(a.get_potential_energy())
    volumes.append(a.get_volume())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v_eq, e_eq, B_ev = eos.fit()                     # B in eV/Å³
B_GPa = B_ev * 160.21766208                     # conversion to GPa
a_eq = v_eq ** (1/3)                             # cubic cell → a

print(f'Equilibrium lattice constant: {a_eq:.4f} Å')
print(f'Bulk modulus: {B_GPa:.1f} GPa')
