import ase
from ase import Atoms
from ase.calculators.emt import EMT
from ase.io import write
import numpy as np

metals = ['Cu', 'Ag', 'Au']
symbols = ['Cu', 'Ag', 'Au']

for metal in metals:
    calc = EMT()
    atoms = Atoms(symbols[metals.index(metal)],
                  lattice=(3.615, 3.615, 3.615),  # Approximate lattice parameters
                  is_cell=True)
    calc.set_local_radius(0.45)
    atoms.set_calculator(calc)
    atoms.get_potential_energy()

    eq_structure = atoms.get_initial_structure()
    lattice_constant = eq_structure.get_lattice()[0]
    bulk_modulus = calc.bulk_modulus(eq_structure)

    print(f"Metal: {metal}")
    print(f"  Lattice Constant (Å): {lattice_constant:.3f}")
    print(f"  Bulk Modulus (Gpa): {bulk_modulus:.3f}")
    print("-" * 30)
