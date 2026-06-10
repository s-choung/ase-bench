from ase.spacegroup import crystal, get_spacegroup
from ase.io import write, read

atoms = crystal(
    symbols=['Na', 'Cl'],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90],
)

write('nacl.cif', atoms)
atoms2 = read('nacl.cif')

sg = get_spacegroup(atoms2)
print(sg)
print('Number of atoms:', len(atoms2))
