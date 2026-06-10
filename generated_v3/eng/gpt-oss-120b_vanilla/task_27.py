# 500 K NVT MD of a 2×2×2 Ag fcc supercell (Bussi thermostat)
# ASE built‑in calculators only; no GUI.

from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nvt import NVT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# 1. Build 2×2×2 Ag fcc supercell
atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))

# 2. Attach a simple EMT calculator (works for many metals)
atoms.calc = EMT()

# 3. Initialise velocities to 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# 4. Set up NVT MD with the Bussi thermostat
dt = 5 * units.fs                     # 5 fs time step
target_T = 500                        # K
thermostat_time = 0.1 * units.ps      # coupling time (≈100 fs)

dyn = NVT(atoms, dt, temperature_K=target_T, taut=thermostat_time)

# 5. Define a callback that prints the instantaneous temperature
def log_temperature():
    T = atoms.get_temperature()
    step = int(dyn.get_time() / dt)   # current MD step
    print(f"Step {step:4d} – Temperature = {T:6.2f} K")

# 6. Register the callback every 50 steps
dyn.attach(log_temperature, interval=50)

# 7. Run 200 MD steps (1 ps total)
dyn.run(200)
