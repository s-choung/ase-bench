from ase.spacegroup import crystal
from ase.build import bulk

atoms = crystal(['Na', 'Cl'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225,
                cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
