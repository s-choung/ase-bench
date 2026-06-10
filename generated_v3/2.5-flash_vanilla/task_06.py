from ase import build
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io import Trajectory
from ase.units import fs, kB
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# 1. Build the system
atoms = build.bulk('Cu', 'fcc', a=3.61).repeat((2, 2, 2))

# 2. Set up the calculator
atoms.set_calculator(EMT())

# 3. Set initial velocities for 300K
temperature_K = 300
MaxwellBoltzmannDistribution(atoms, temperature_K * kB)

# 4. Record initial state
initial_kinetic_energy = atoms.get_kinetic_energy()
initial_potential_energy = atoms.get_potential_energy()
initial_total_energy = initial_kinetic_energy + initial_potential_energy
initial_temperature = initial_kinetic_energy / (1.5 * len(atoms) * kB)

# 5. Set up Langevin MD
timestep_fs = 5
friction_coeff = 0.02  # Typical friction coefficient
dyn = Langevin(atoms, timestep_fs * fs, temperature_K * kB, friction_coeff)

# 6. Run MD
dyn.run(100)

# 7. Record final state
final_kinetic_energy = atoms.get_kinetic_energy()
final_potential_energy = atoms.get_potential_energy()
final_total_energy = final_kinetic_energy + final_potential_energy
final_temperature = final_kinetic_energy / (1.5 * len(atoms) * kB)

# 8. Print results
print(f"Initial Temperature: {initial_temperature:.2f} K")
print(f"Initial Total Energy: {initial_total_energy:.2f} eV")
print(f"Final Temperature: {final_temperature:.2f} K")
print(f"Final Total Energy: {final_total_energy:.2f} eV")
