import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EOS

a_ref = 4.086  # Ag FCC reference lattice constant (Å)
a_list = np.linspace(0.95 * a_ref, 1.05 * a_ref, 7)
vols, eners = [], []
calc = EMT()

for a in a_list:
    atoms = Atoms('Ag4', cell=[a, a, a], pbc=True,
                  scaled_positions=[(0,0,0), (0,0.5,0.5),
                                    (0.5,0,0.5), (0.5,0.5,0)])
    atoms.calc = calc
    vols.append(a ** 3)
    eners.append(atoms.get_potential_energy())

eos = EOS('birchmurnaghan', vols=vols, energies=eners)
v0, _, B0 = eos.fit()
a0_eq = v0 ** (1/3)
B0_gpa = B0 * 160.21766208  # Convert eV/Å³ to GPa

print(f'Equilibrium lattice constant: {a0_eq:.4f} Å')
print(f'Bulk modulus: {B0_gpa:.2f} GPa')
