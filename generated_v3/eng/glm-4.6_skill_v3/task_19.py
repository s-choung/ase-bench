from ase import Atoms

atoms = Atoms('COO', 
              positions=[[0, 0, 0], [0, 0, 1.16], [0, 0, -1.16]], 
              cell=[10, 10, 10], 
              pbc=False)

d_co = atoms.get_distances(0, 1)
d_oo = atoms.get_distances(1, 2)

print(f"C-O distance: {d_co[0]:.3f} Å")
print(f"O-O distance: {d_oo[0]:.3f} Å")
