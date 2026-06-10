import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.npt import NPT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Setup Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Constants and conversion
temp = 500
pressure_gpa = 10
# 1 GPa = 6.2415e-3 eV/A^3
pressure_ev_a3 = pressure_gpa * 0.0062415

# Initialize MD
MaxwellBoltzmannDistribution(atoms, temperature_K=temp)
dyn = NPT(atoms, 
          timestep=1.0, 
          temperature_K=temp, 
          externalstress=pressure_ev_a3 * np.eye(3),
          ttime=25.0, 
          pfactor=50.0)

v_init = atoms.get_volume()
print(f"Initial Volume: {v_init:.3f} A^3")

# Run 100 steps
dyn.run(100)

v_final = atoms.get_volume()
print(f"Final Volume: {v_final:.3f} A^3")
