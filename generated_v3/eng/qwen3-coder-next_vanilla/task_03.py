from ase import Atoms
from ase.lattice import hexagonal

# Create MoS2 monolayer (2H phase)
a = 3.18  # lattice constant in Å
c = 12.5  # out-of-plane parameter for monolayer (approximately 3x S-Mo-S layer spacing)

# Create the unit cell with appropriate vacuum
cell = [[a, 0, 0], 
        [-a/2, a*3**0.5/2, 0], 
        [0, 0, c + 10.0]]  # 10 Å vacuum added in z-direction

# Atomic positions in fractional coordinates
# Mo at (0, 0, 0.25), S at (0, 0, 0.125) and (0, 0, 0.375) for 2H-MoS2 monolayer
atoms = Atoms('MoS2',
              positions=[[0, 0, 0.25*c],
                         [0, 0, 0.125*c],
                         [0, 0, 0.375*c]],
              cell=cell,
              pbc=[True, True, False])

# Print cell size
print("Cell size (Å):", atoms.get_cell_lengths_and_angles())
