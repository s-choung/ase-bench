from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs

# Initialize Cu FCC structure
cu = Atoms('Cu', crystalstructure='fcc', a=3.61, pbc=True)
cu *= (2, 2, 2)

# Configure EMT calculator
cu.calc = EMT()

# Dynamics setup
dyn = Langevin(cu, 5*fs, 300*fs, temperature_K=300)

# Output initial info
e_init = cu.get_potential_energy()
print(f"Initial Temp: {cu.get_temperature()}K Energy: {e_init:.3f} eV")

# Run MD
dyn.run(100)

# Output final info
e_final = cu.get_potential_energy()
print(f"Final Temp: {cu.get_temperature()}K Energy: {e_final:.3f} eV")
