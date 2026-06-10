from ase.build import bulk
from ase.lattice.cubic import FaceCenteredCubic
from ase.atoms import Atoms

a = 5.64

basis = [
    ('Na', (0.0, 0.0, 0.0)),
    ('Cl', (0.5, 0.5, 0.5))
]

cell = FaceCenteredCubic(symbol='Na', latticeconstant=a)

atoms = Atoms(
    symbols=['Na', 'Cl'],
    scaled_positions=[(0.0, 0.0, 0.0), (0.5, 0.5, 0.5)],
    cell=[[a, 0, 0], [0, a, 0], [0, 0, a]],
    pbc=True
)

atoms = bulk('NaCl', 'rocksalt', a=a)

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
print(f"Unique symbols: {set(atoms.get_chemical_symbols())}")
