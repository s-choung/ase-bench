import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc')
    calc = EMT()
    volumes = []
    energies = []
    
    for scale in np.linspace(0.95, 1.05, 7):
        atoms_copy = atoms.copy()
        atoms_copy.set_cell(atoms_copy.get_cell() * scale, scale_atoms=True)
        atoms_copy.calc = calc
        volumes.append(atoms_copy.get_volume())
        energies.append(atoms_copy.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 / 4)**(1/3)
    results.append([metal, a0, B / kJ * 1000])

print(f"{'Metal':<5} {'a₀ (Å)':<10} {'B (GPa)':<10}")
print("-" * 28)
for metal, a0, B in results:
    print(f"{metal:<5} {a0:<10.3f} {B:<10.1f}")
