from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = {'Cu': 3.61, 'Ag': 4.09, 'Au': 4.08}

results = {}

for metal, initial_a in metals.items():
    atoms = bulk(metal, 'fcc', a=initial_a)
    atoms.calc = EMT()

    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(a.get_cell() * x, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = v0**(1/3)
    results[metal] = (a0, B)

print("Metal | Equilibrium Lattice Constant (Å) | Bulk Modulus (GPa)")
print("------|-----------------------------------|-----------------")
for metal, (a0, B) in results.items():
    print(f"{metal:5s} | {a0:30.4f} | {B:15.2f}")
