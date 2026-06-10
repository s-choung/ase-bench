from ase import Atoms
from ase.visualize import view
from ase.calculators.lj import LennardJones
from ase.calculators.emt import EMT

# Fe bulk lattice constants (Å)
a = 2.866

# Create 4-atom bulk unit cell (basis vectors)
basis = [[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5],
         [0, 0.5, 0.5]]

atoms = Atoms('Fe4', positions=basis,
              cell=array([[a, 0, 0], [0, a, 0], [0, 0, a]]),
              pbc=True)

# Replace the LJ calculator with EMT (since only EMT is requested)
atoms.set_calculator(EMT())

# Surface transformation: (110) plane, 4 layers, (2,2,4)
new_pos = []
new_cell = []
z = -a*2

for layer in range(4):
    x = z + layer * (0.5 * a)
    new_pos.append([0.0, 0.0, x])
    new_cell.append([a, a, a])

atoms.resize(len(new_pos))
atoms.set_positions(new_pos)

# Resize cell in z to accommodate vacuum
atoms.cell[2] = 4 * a + 10.0  # z-direction (a*c) + vacuum ≈ 4*2.866 + 10

print(f"Number of atoms: {len(atoms)}")
print(f"Cell size (Å): {atoms.cell}")
