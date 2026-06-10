import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', cubic=True)
    atoms.calc = EMT()
    cell = atoms.get_cell()
    
    volumes, energies = [], []
    for x in np.linspace(0.94, 1.06, 9):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
        
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    a0 = v0 ** (1/3)
    B_GPa = B / GPa
    results.append((metal, a0, B_GPa))

print(f"{'Metal':<6} | {'a0 (Å)':<10} | {'B0 (GPa)':<10}")
print("-" * 33)
for metal, a0, b0 in results:
    print(f"{metal:<6} | {a0:<10.4f} | {b0:<10.2f}")
