from ase.build import surface
from ase.lattice.cubic import BodyCenteredCubic

a = 2.87
bulk = BodyCenteredCubic(directions=[[1,0,0],[0,1,0],[0,0,1]], size=(1,1,1), symbol='Fe', pbc=True, latticeconstant=a)
slab = surface(bulk, (1,1,0), size=(2,2,4), vacuum=10)
print(f"Number of atoms: {len(slab)}")
print("Cell (Angstroms):")
print(slab.get_cell().array)
