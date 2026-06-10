from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
initial_a = {'Cu': 3.61, 'Ag': 4.09, 'Au': 4.08}
results = {}

for metal in metals:
    atoms = bulk(metal, 'fcc', a=initial_a[metal])
    atoms.calc = EMT()
    
    cell = atoms.get_cell()
    volumes, energies = [], []
    for scale in np.linspace(0.97, 1.03, 7):
        atoms.set_cell(cell * scale, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    B_GPa = B * 160.21766208
    results[metal] = (a0, B_GPa)

print(f"{'Metal':<6} {'a0 (Å)':>10} {'B0 (GPa)':>12}")
for metal, (a0, B0) in results.items():
    print(f"{metal:<6} {a0:>10.3f} {B0:>12.1f}")
