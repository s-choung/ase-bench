from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
a_exp = {'Cu': 3.615, 'Ag': 4.085, 'Au': 4.078}  # experimental refs

results = {}
for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()
    
    volumes, energies = [], []
    for a in np.linspace(3.5, 4.5, 15):
        atoms.set_cell([a, a, a], scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 * 4) ** (1/3)  # 4 atoms in FCC conventional cell
    
    results[metal] = {'a0': a0, 'B': B, 'a_exp': a_exp[metal]}

print(f"{'Metal':<8} {'a₀ (Å)':<12} {'a_exp (Å)':<12} {'Δa (%)':<10} {'B (GPa)':<12}")
print("-" * 54)
for metal, r in results.items():
    delta = 100 * (r['a0'] - r['a_exp']) / r['a_exp']
    print(f"{metal:<8} {r['a0']:<12.4f} {r['a_exp']:<12.4f} {delta:<10.2f} {r['B']:<12.2f}")
