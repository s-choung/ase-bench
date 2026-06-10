from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# System setup
atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (3, 3, 3)
atoms.calc = EMT()

# MD initialization
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Simulation parameters
v_initial = atoms.get_volume()
p_initial = atoms.get_pressure()

dyn = NPTBerendsen(
    atoms, 
    timestep=5 * units.fs, 
    temperature_K=300, 
    pressure=1 * units.bar, 
    taut=100 * units.fs, 
    taup=1000 * units.fs
)

# Run
dyn.run(200)

v_final = atoms.get_volume()
p_final = atoms.get_pressure()

print(f"Initial Volume: {v_initial:.3f}, Pressure: {p_initial:.3f}")
print(f"Final Volume: {v_final:.3f}, Pressure: {p_final:.3f}")
