from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

print(f"{'Metal':<6} {'a₀ (Å)':<10} {'B (GPa)':<10}")
print("-" * 28)

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', a=4.0)
    atoms.calc = EMT()
    
    volumes, energies = [], []
    for a in np.linspace(3.4, 4.4, 9):
        atoms.set_cell([a, a, a], scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    v0, e0, B = EquationOfState(volumes, energies).fit()
    a0 = v0**(1/3)
    B_gpa = B * 160.21766208
    
    print(f"{symbol:<6} {a0:<10.3f} {B_gpa:<10.1f}")
