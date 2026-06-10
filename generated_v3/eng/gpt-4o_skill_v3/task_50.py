from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', a=3.6)
    atoms.calc = EMT()
    
    volumes, energies = [], []
    cell = atoms.get_cell()
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = (v0 / atoms.get_number_of_atoms())**(1/3)
    results.append((metal, a0, B / units.kJ * 1e24))  # Bulk modulus in GPa

print("{:<8} {:<12} {:<12}".format("Metal", "a0 (Å)", "B (GPa)"))
for metal, a0, B in results:
    print("{:<8} {:<12.4f} {:<12.4f}".format(metal, a0, B))
