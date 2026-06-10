from ase import Atoms, EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[[0, 0, 0], [1.0, 0, 0]])
calc = EMT()
h2.calc = calc
e_initial = h2.get_potential_energy()
bond_length_initial = h2.get_distance(0, 1)

constraint = FixBondLength(h2, indices=(0, 1), bond_length=0.9)
h2.set_constraints([constraint])
e_constrained = h2.get_potential_energy()

print(f"Initial bond length: {bond_length_initial:.3f} Å")
print(f"Initial energy: {e_initial:.6f} eV")
print(f"Constrained bond length: 0.9 Å")
print(f"Constrained energy: {e_constrained:.6f} eV")
