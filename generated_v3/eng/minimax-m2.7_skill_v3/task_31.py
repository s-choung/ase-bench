from ase import Atoms, units
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05)
atoms = atoms * (2, 2, 2)

# Convert 10 GPa to eV/Å³ (1 eV/Å³ = 160.2 GPa)
pressure_gpa = 10.0
pressure_ev_ang3 = pressure_gpa / 160.2

print(f"Pressure: {pressure_gpa} GPa = {pressure_ev_ang3:.6f} eV/Å³")

# Initial volume
initial_volume = atoms.get_volume()
print(f"Initial cell volume: {initial_volume:.2f} Å³")

# Setup calculator and MD
atoms.calc = EMT()
dyn = NPTBerendsen(
    atoms,
    timestep=1 * units.fs,
    temperature_K=500,
    external_pressure=pressure_ev_ang3,
    tau_t=0.1 * units.fs,
    tau_p=0.5 * units.fs
)

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn.run(100)

final_volume = atoms.get_volume()
print(f"Final cell volume: {final_volume:.2f} Å³")
print(f"Volume change: {(final_volume - initial_volume) / initial_volume * 100:.2f}%")
