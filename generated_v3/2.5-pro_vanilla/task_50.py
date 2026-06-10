```python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    # 1. Create initial FCC structure and set calculator
    atoms = bulk(metal, 'fcc', a=4.0)
    atoms.calc = EMT()

    # 2. Calculate energies for a range of volumes
    cell = atoms.get_cell()
    volumes = []
    energies = []
    for scale in np.linspace(0.95, 1.05, 11):
        atoms.set_cell(cell * scale, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    # 3. Perform EOS fitting
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()

    # 4. Calculate equilibrium lattice constant and bulk modulus
    # v0 is the volume of the primitive cell (1 atom).
    # For FCC, conventional cell volume is a^3 and contains 4 atoms.
    # So, v0 = a^3 / 4  =>  a = (4 * v0)^(1/3)
    a0 = (4 * v0)**(1/3.0)
    B_gpa = B / GPa

    results.append({'metal': metal
