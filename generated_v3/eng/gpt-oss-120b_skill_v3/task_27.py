from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# 2×2×2 FCC supercell of Ag
atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Initialise velocities at 500 K and remove centre‑of‑mass drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Bussi NVT dynamics, 5 fs timestep, target 500 K
dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500)

# Print temperature every 50 steps
def log_temp():
    step = dyn.get_number_of_steps()
    temp = atoms.get_temperature()
    print(f"Step {step:3d} – Temperature = {temp:.2f} K")

dyn.attach(log_temp, interval=50)
dyn.run(200)          # 200 MD steps
