from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', a=3.6)
    atoms.calc = EMT()
    BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

    cell = atoms.get_cell()
    volumes, energies = [], []
    for x in [0.95, 0.97, 0.99, 1.0, 1.01, 1.03, 1.05]:
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 / len(atoms)) ** (1/3)
    results.append((metal, a0, B))

print("{:<3} {:<8} {:<10}".format("Metal", "a0 (Å)", "B (GPa)"))
for metal, a0, B in results:
    print("{:<3} {:<8.4f} {:<10.2f}".format(metal, a0, B/1e9))
