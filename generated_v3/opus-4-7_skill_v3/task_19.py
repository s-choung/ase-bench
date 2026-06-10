from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms('CO2',
              positions=[[0, 0, 0], [-1.16, 0, 0], [1.16, 0, 0]],
              cell=[10, 10, 10],
              pbc=False)

pos = atoms.get_positions()
D, D_len = get_distances(pos, pos)
print("Distance matrix (Å):")
print(D_len)
print(f"\nC-O1: {D_len[0,1]:.4f} Å")
print(f"C-O2: {D_len[0,2]:.4f} Å")
print(f"O1-O2: {D_len[1,2]:.4f} Å")
