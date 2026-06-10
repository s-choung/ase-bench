from ase.build import cut
from ase.calculators.emt import EMT
from ase.io import write

atoms = cut(
    'Cu',
    (2, 1, 1),
    layers=3,
    vacuum=10.0,
    filename='cu_surface.cube'
)

calc = EMT()
atoms.calc = calc

print(f"Number of atoms: {len(atoms)}")
print(f"Cell: \n{atoms.cell}")
write('cu_surface.xyz', atoms)
