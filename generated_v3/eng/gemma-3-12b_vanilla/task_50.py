from ase.build import fcc
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

metals = {"Cu": (1.0, 12), "Ag": (1.0, 12), "Au": (1.0, 12)}

for metal, (alat, n_atoms) in metals.items():
    atoms = fcc(metal, size=2.5, symbol=metal)
    calc = EMT()
    atoms.calc = calc
    eos = EquationOfState(atoms)
    eos.fit()
    V0 = eos.reference_volume
    B0 = eos.bulk_modulus
    a0 = (V0 / n_atoms)**(1/3)
    print(f"{metal}: a0 = {a0:.5f} Å, B0 = {B0:.5f} GPa")
