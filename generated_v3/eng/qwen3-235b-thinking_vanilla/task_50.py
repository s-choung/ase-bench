from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

results = []
elements = ['Cu', 'Ag', 'Au']

for elem in elements:
    atoms = bulk(elem, 'fcc', a=4.0, cubic=True)
    volumes, energies = [], []
    for scale in np.linspace(0.9, 1.1, 7):
        scaled_atoms = atoms.copy()
        scaled_atoms.set_cell(atoms.cell * scale, scale_atoms=True)
        scaled_atoms.calc = EMT()
        volumes.append(scaled_atoms.get_volume())
        energies.append(scaled_atoms.get_potential_energy())
    
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    B_GPa = B * 160.21766208
    results.append((elem, a0, B_GPa))

print(f"{'Element':<8}{'a0 (Å)':<12}{'B (GPa)':<10}")
for res in results:
    print(f"{res[0]:<8}{res[1]:<12.4f}{res[2]:<10.2f}")
