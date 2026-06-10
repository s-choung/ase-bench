from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EOSFit
import numpy as np

# FCC Cu
cu = bulk('Cu', 'fcc', a=3.6)
cu.set_calculator(EMT())

# Lattice constants to sample
a_vals = np.linspace(3.4, 3.8, 7)

volumes, energies = [], []
for a in a_vals:
    atoms = cu.copy()
    atoms.set_cell([a, a, a], scale_atoms=True)
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

# EOS fit
v0, B_eV_A3, _ = EOSFit(volumes, energies).fit()

# Convert bulk modulus to GPa (1 eV/Å³ = 160.21766208 GPa)
B_GPa = B_eV_A3 * 160.21766208
a0 = v0 ** (1/3)

print(f'Equilibrium lattice constant: {a0:.4f} Å')
print(f'Equilibrium volume per cell: {v0:.4f} Å³')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
