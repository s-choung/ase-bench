from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.nptberendsen import NPTBerendsen

# Build structure
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

# Print initial cell volume and pressure
print('Initial volume:', atoms.get_volume())
print('Initial pressure:', atoms.get_pressure())

# Run NPT MD
dyn = NPTBerendsen(
    atoms,
    timestep=5*units.fs,
    temperature_K=300,
    taut=100*units.fs,
    pressure=1*units.bar,
    taup=1000*units.fs,
)
dyn.run(200)

# Print final cell volume and pressure
print('Final volume:', atoms.get_volume())
print('Final pressure:', atoms.get_pressure())
