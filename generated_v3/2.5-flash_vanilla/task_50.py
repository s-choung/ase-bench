```python
from ase import Atoms
from ase.build import fcc
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = {}

print("Performing EOS fitting with EMT calculator...")

for metal in metals:
    # Create a 1x1x1 FCC unit cell
    # The initial lattice constant 'a' is just a starting point for scaling
    atoms = fcc(metal, size=(1,1,1), a=4.0) 
    atoms.calc = EMT()

    # Define a range of volumes by scaling the lattice constant
    # We'll scale the initial cell by factors from 0.95 to 1.05
    cell = atoms.get_cell()
    volumes = []
    energies = []

    for x in np.linspace(0.95, 1.05, 11): # 11 points for a good fit
        atoms_scaled = atoms.copy()
        atoms_scaled.set_cell(cell * x, scale_atoms=True)
        
        volumes.append(atoms_scaled.get_volume())
        energies.append(atoms_scaled.get_potential_energy())

    # Perform Equation of State fitting
    eos = EquationOfState(volumes, energies)
    v0, e0, b0 = eos.fit() # v0: equilibrium volume, e0: equilibrium energy, b0: bulk modulus
