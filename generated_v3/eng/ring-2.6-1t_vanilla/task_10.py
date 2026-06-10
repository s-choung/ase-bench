from ase.build import nanoparticle

oct = nanoparticle.Octahedron("Cu", length=5)
print(len(oct), oct.positions.shape)
