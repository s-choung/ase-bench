from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

# Build Cu FCC 3x3x3 supercell
cu = bulk('Cu', 'fcc').repeat((3, 3, 3))
cu.calc = EMT()
cu.get_potential_energy()  # Trigger stress calculation for pressure

# Print initial state
initial_vol = cu.get_volume()
initial_press = cu.get_pressure() / units.bar
print(f"Initial Volume: {initial_vol:.2f} Å³, Initial Pressure: {initial_press:.2f} bar")

# MD setup
MaxwellBoltzmannDistribution(cu, temperature_K=300)
Stationary(cu)
md = NPTBerendsen(
    cu,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility=7.3e-12  # Typical Cu compressibility (Pa⁻¹)
)

# Run MD
md.run(200)

# Print final state
final_vol = cu.get_volume()
final_press = cu.get_pressure() / units.bar
print(f"Final Volume: {final_vol:.2f} Å³, Final Pressure: {final_press:.2f} bar")
