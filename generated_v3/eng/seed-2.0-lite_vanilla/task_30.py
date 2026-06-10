from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Create 3x3x3 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms.repeat((3, 3, 3))
atoms.calc = EMT()

# Calculate initial system properties
init_vol = atoms.get_volume()
init_stress = atoms.get_stress()
init_press = -init_stress[:3].mean() / units.bar  # Convert to bar

# Set up NPT Berendsen dynamics
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature=300,
    pressure=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs
)

# Run 200 steps of NPT MD
dyn.run(200)

# Calculate final system properties
final_vol = atoms.get_volume()
final_stress = atoms.get_stress()
final_press = -final_stress[:3].mean() / units.bar

# Print results
print(f"Initial volume: {init_vol:.2f} Å³, Initial pressure: {init_press:.2f} bar")
print(f"Final volume: {final_vol:.2f} Å³, Final pressure: {final_press:.2f} bar")
