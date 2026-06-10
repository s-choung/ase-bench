from ase import Atoms, Atom
from ase.build import make_supercell
from ase.visualize import view

# Pt(111) bulk lattice vectors
a = 3.94  # Pt lattice constant (Å)

# Primitive fcc unit cell
cell = Atoms('Pt',
            positions=[[0,0,0], [0.5*a,0.5*a,0], [0,0.5*a,0.5*a], [0.5*a,0,0.5*a]],
            cell=[[a,0.,0.], [0.,a,0.], [0.,0.,a]],
            pbc=True)

# Reduced primitive cell (two layers)
cell_red = Atoms('Pt', cell)

# Build the slab
for i in range(10):
    slab = cell_red + Atom('Pt', 0, 0, i*a)
    slab.set_cell(cell_red.cell, scale_atoms=False)

# Create a 4‑layer slab (repeat in c‑direction twice)
slab4 = make_supercell(slab, [[1,0,0],[0,1,0],[0,0,2]])
slab4.center(vacuum=10)  # vacuum of 10 Å above the slab

# Adsorb CO on an on‑top site above the first layer
slab4.add(Atom('C', 0, 0, -0.3*a))   # carbon directly above a Pt atom
slab4.add(Atom('O', 0, 0, 0.3*a))    # oxygen overlaps with the Pt atom (ontop)

print(slab4.get_number_of_atoms())
