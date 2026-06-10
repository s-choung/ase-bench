from ase.build import bulk
from ase.io import write, read

atoms = bulk("Au", "fcc", a=4.08, cubic=True)
write("Au_fcc.xyz", atoms, format="xyz")

atoms_read = read("Au_fcc.xyz", format="xyz")

for atom in atoms_read:
    print(atom.symbol, atom.position)
