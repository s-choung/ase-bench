from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
init_a = {'Cu': 3.61, 'Ag': 4.09, 'Au': 4.08}

results = []
for metal in metals:
    atoms = bulk(metal, 'fcc', a=init_a[metal])
    cell = atoms.get_cell()
    volumes, energies, scales = [], [], np.linspace(0.96, 1.04, 9)
    for x in scales:
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 / 4)**(1/3)  # FCC conventional cell: 4 atoms
    results.append({'metal': metal, 'a0': a0, 'B': B / 100})  # Bulk modulus GPa

print(f"{'Metal':<4} {'a0 (Å)':>10} {'Bulk Modulus (GPa)':>22}")
for r in results:
    print(f"{r['metal']:<4} {r['a0']:10.4f} {r['B']:22.2f}")
