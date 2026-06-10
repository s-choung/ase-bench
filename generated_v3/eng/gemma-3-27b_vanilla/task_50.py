from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

metals = {'Cu': 'Cu', 'Ag': 'Ag', 'Au': 'Au'}

results = {}

for symbol, element in metals.items():
    atoms = bulk(element, 'fcc', a=3.6)
    calc = EMT()
    atoms.set_calculator(calc)
    dyn = BFGS(atoms, trajectory='emt_opt.traj')
    dyn.run(fmax=0.02)
    
    energies = []
    volumes = []
    for a in np.linspace(3.0, 4.0, 7):
        atoms = bulk(element, 'fcc', a=a)
        atoms.set_calculator(calc)
        energy = atoms.get_potential_energy()
        energies.append(energy)
        volumes.append(atoms.get_volume())
    
    eos = EquationOfState(volumes, energies)
    a_eq, K = eos.fit()
    results[symbol] = (a_eq, K)

print("Metal | Equilibrium Lattice Constant (Angstrom) | Bulk Modulus (eV)")
print("------|-------------------------------------------|-----------------")
for symbol, (a, K) in results.items():
    print(f"{symbol}   | {a:.3f}                             | {K:.2f}")
