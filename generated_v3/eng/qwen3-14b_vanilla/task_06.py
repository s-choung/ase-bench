from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin

# Create 2x2x2 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6)
atoms = make_supercell(atoms, [[2,0,0],[0,2,0],[0,0,2]])
atoms.set_calculator(EMT())

# Initial values
initial_energy = atoms.get_potential_energy()
initial_temp = atoms.get_temperature()

# Langevin MD
d = Langevin(atoms, timestep=5e-15, temperature=300)
d.run(100)

# Final values
final_energy = atoms.get_potential_energy()
final_temp = atoms.get_temperature()

print(f"Initial Temperature: {initial_temp:.2f} K")
print(f"Initial Energy: {initial_energy:.6f} eV")
print(f"Final Temperature: {final_temp:.2f} K")
print(f"Final Energy: {final_energy:.6f} eV")
