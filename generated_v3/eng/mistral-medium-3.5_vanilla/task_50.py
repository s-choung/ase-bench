from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = FaceCenteredCubic(symbol=metal, latticeconstant=3.5, size=(1, 1, 1))
    atoms.calc = EMT()

    volumes = []
    energies = []
    for a in np.linspace(3.0, 4.5, 15):
        atoms.set_cell([a, a, a], scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = (v0 * 4) ** (1/3)  # FCC: a = (4V_0)^(1/3)
    results.append((metal, a0, B))

print("Metal | Lattice Constant (Å) | Bulk Modulus (GPa)")
print("-----------------------------------------------")
for metal, a0, B in results:
    print(f"{metal:5} | {a0:22.3f} | {B/units.GPa:18.2f}")
