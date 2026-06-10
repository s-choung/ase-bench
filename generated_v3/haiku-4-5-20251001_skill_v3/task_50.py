import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0)
    atoms.calc = EMT()
    
    cell = atoms.get_cell()
    volumes, energies = [], []
    
    for x in np.linspace(0.95, 1.05, 11):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    a0 = (4 * v0) ** (1/3)
    results[metal] = {'a0': a0, 'B': B}

print("\n" + "="*50)
print("EOS Fitting Results (EMT Calculator)")
print("="*50)
print(f"{'Metal':<10} {'a₀ (Å)':<15} {'B (eV/Ų)':<15}")
print("-"*50)
for metal in metals:
    a0 = results[metal]['a0']
    B = results[metal]['B']
    print(f"{metal:<10} {a0:<15.6f} {B:<15.6f}")
print("="*50 + "\n")
