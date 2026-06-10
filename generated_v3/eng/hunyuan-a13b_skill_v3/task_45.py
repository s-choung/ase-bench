from ase import Atoms, Bond
from ase.calculators import EMT
from ase.constraints import FixBondLength

# Create H2 molecule
molecule = Atoms('H2', positions=[[0, 0, 0], [1, 0, 0]], cell=[2, 0, 0], pbc=True,orns=False)

# Calculate energy without constraint
molecule.calc = EMT()
initial_length = molecule.get_distance(0, 1)
initial_energy = molecule.get_potential_energy()
print(f"Initial bond length: {initial_length:.3f} Å")
print(f"Initial energy: {initial_energy:.6f} eV")

# Apply constraint
bond_indices = [(0, 1)]
constraint = FixBondLength(bond_indices[0], bond_indices[1], length=0.9)
molecule.set_constraint([constraint])

# Recalculate energy
final_energy = molecule.get_potential_energy()
final_length = molecule.get_distance(0, 1)
print(f"Final bond length: {final_length:.3f} Å")
print(f"Final energy: {final_energy:.6f} eV")
