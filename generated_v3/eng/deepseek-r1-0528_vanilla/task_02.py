from ase.build import fcc111
from ase.build import add_adsorbate
from ase import Atoms

slab = fcc111('Pt', size=(1,1,4), vacuum=10.0)
co = Atoms('CO', positions=[[0.0,0.0,0.0], [0.0,0.0,1.15]])
top_z = slab.positions[:,2].max()
top_indices = [i for i, atom in enumerate(slab) if atom.z > top_z - 0.1]
add_adsorbate(slab, co, height=2.4, position=top_indices[0])
print(len(slab))
