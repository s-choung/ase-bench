import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for symbol in metals:
    atoms = bulk(symbol, 'fcc', a=3.6)
    atoms.calc = EMT()
    
    volumes, energies = [], []
    cell = atoms.get_cell()
    
    # Sample 7 points around equilibrium (0.95 to 1.05 scale)
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    # Convert equilibrium volume to lattice constant a for FCC: V = a^3
    a0 = v0**(1/3)
    results.append((symbol, a0, B))

print(f"{'Metal':<10} {'a0 (Å)':<15} {'B (eV/Å^3)':<15}")
print("-" * 40)
for res in results:
    print(f"{res[0]:<10} {res[1]:<15.4f} {res[2]:<15.4f}")
