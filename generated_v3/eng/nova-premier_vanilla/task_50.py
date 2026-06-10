from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = {}

for m in metals:
    a0 = 4.0  # initial guess
    bulk = FaceCenteredCubic(m)
    vols = []
    engs = []
    for x in np.linspace(0.95, 1.05, 5):
        bulk.set_cell(bulk.cell * x, scale_atoms=True)
        bulk.calc = EMT()
        engs.append(bulk.get_potential_energy())
        vols.append(bulk.get_volume())
    eos = EquationOfState(vols, engs)
    v0, e0, B = eos.fit()
    a = (4 * v0 / len(bulk))**(1/3)
    results[m] = (a, B / 1e9)  # Convert bulk modulus to GPa

print("{:<5} {:<15} {:<15}".format("Metal", "Lattice (A)", "B (GPa)"))
for m, (a, B) in results.items():
    print("{:<5} {:<15.3f} {:<15.2f}".format(m, a, B))
