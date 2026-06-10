from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', cubic=True)
    volumes, energies = [], []
    for scale in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(a.cell * scale, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume() / len(a))
        energies.append(a.get_potential_energy() / len(a))
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (4 * v0) ** (1/3)
    B_GPa = B * 160.21766208
    results.append((metal, a0, B_GPa))

print("Metal | a0 (Å) | Bulk Modulus (GPa)")
print("----------------------------------")
for metal, a0, B in results:
    print(f"{metal:5s} | {a0:6.3f} | {B:10.1f}")
