from ase.build import bulk
from ase.spacegroup import crystal

# Create Ti HCP bulk structure
a = 2.95
c = a * 1.59
atoms = bulk('Ti', 'hcp', a=a, c=c)

# Print cell vectors
print("Cell vectors (Å):")
for vec in atoms.get_cell():
    print(f"  {vec[0]:.6f}  {vec[1]:.6f}  {vec[2]:.6f}")

# Print atomic positions
print("\nAtomic positions (Å):")
for i, pos in enumerate(atoms.get_positions()):
    print(f"  Atom {i}:  {pos[0]:.6f}  {pos[1]:.6f}  {pos[2]:.6f}")
