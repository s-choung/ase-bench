from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.neb import NEB

slab = fcc111('Al', size=(3, 3, 2))
slab.set_cell((10, 10, 5))
slab.get_positions()

initial = slab.copy()
final = slab.copy()

initial.positions[0] = (0, 0, 5)
final.positions[1] = (0, 0, 5)

neb = NEB(initial, final, nsteps=100)
neb.attach(initial)
neb.attach(final)

calc = EMT()
neb.calc = calc

neb.run(fmax=0.02)

for i, atoms in enumerate(neb.images):
    energy = atoms.calc.results['energy']
    print(f"Image {i}: Energy = {energy:.4f} eV")
