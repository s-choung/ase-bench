import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = {'Cu': 'Cu', 'Ag': 'Ag', 'Au': 'Au'}
results = []

for name, symbol in metals.items():
    energies = []
    volumes = []
    
    # Generate lattice constants from 5% to 15% strain
    base_cell = bulk(symbol, 'fcc', a=3.6) # Approximate starting point
    a0 = base_cell.get_cell()[0, 0]
    
    for scale in np.linspace(0.9, 1.1, 7):
        atoms = bulk(symbol, 'fcc', a=a0 * scale)
        atoms.calc = EMT()
        energies.append(atoms.get_potential_energy())
        volumes.append(atoms.get_volume())
    
    # EOS Fitting
    eos = EquationOfState(volumes, energies)
    v0, e0, b = eos.fit()
    
    # Convert volume back to lattice constant for FCC: V = a^3 / sqrt(2)
    a_eq = (v0 * np.sqrt(2))**(1/3)
    
    results.append((name, a_eq, b / 1e5)) # Convert B from eV/A^3 to GPa

print(f"{'Metal':<6} | {'a0 (Å)':<10} | {'B (GPa)':<10}")
print("-" * 30)
for name, a, b in results:
    print(f"{name:<6} | {a:<10.4f} | {b:<10.2f}")
