from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Setup Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

# Initial state
vol0 = atoms.get_volume()
press0 = atoms.get_stress(voigt=False).trace() / 3.0 / units.GPa
print(f"Initial Volume: {vol0:.2f} Å^3, Pressure: {press0:.2f} GPa")

# NPT Berendsen MD
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature=300 * units.kB,
    pressure=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility=4.57e-5 / units.bar  # Cu approx
)

dyn.run(200)

# Final state
vol1 = atoms.get_volume()
press1 = atoms.get_stress(voigt=False).trace() / 3.0 / units.GPa
print(f"Final Volume:   {vol1:.2f} Å^3, Pressure: {press1:.2f} GPa")
