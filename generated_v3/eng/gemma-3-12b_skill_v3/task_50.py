from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']

for metal in metals:
    atoms = Atoms(symbol=metal, calculator=EMT())
    cell = np.array([[3.6, 0, 0], [0, 3.6, 0], [0, 0, 3.6]])
    atoms.set_cell(cell)
    atoms.set_pbc(True)

    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.get_potential_energy()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()

    print(f"Metal: {metal}")
    print(f"  Equilibrium volume: {v0:.3f} Bohr^3")
    print(f"  Bulk modulus: {B:.3f} GPa")
    print("-" * 20)
