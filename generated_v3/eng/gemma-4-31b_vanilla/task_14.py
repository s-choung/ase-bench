from ase.spacegroup import crystal
from ase.calculators.emt import EMT

atoms = crystal(
    ['Na', 'Cl'],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    latticeconstant=5.64
)

atoms.calc = EMT()

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
