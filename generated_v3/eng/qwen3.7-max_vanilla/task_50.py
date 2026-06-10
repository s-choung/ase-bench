import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for el in metals:
    atoms = bulk(el, 'fcc', cubic=True)
    atoms.calc = EMT()
    cell0 = atoms.get_cell()
    volumes, energies = [], []
    
    for strain in np.linspace(-0.06, 0.06, 9):
        scale = (1 + strain)**(1/3)
        atoms.set_cell(cell0 * scale, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
        
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    
    a0 = v0**(1/3)
    B_GPa = B * 160.21766208
    results.append((el, a0, B_GPa))

print(f"{'Metal':<6} | {'a0 (Å)':>8} | {'B (GPa)':>8}")
print("-" * 28)
for el, a0, B in results:
    print(f"{el:<6} | {a0:>8.4f} | {B:>8.2f}")
