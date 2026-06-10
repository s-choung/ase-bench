from ase import Atoms, units
from ase.build import fcc
from ase.calculators.emt import EMT
from ase.md.npt_berendsen import NPTBerendsen

atoms = fcc('Cu', size=(3, 3, 3), cubic=True)
atoms.calc = EMT()

vol_init = atoms.get_volume()
print(f"Initial volume: {vol_init:.2f} Å³")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature=300,
    taut=100 * units.fs,
    pressure=1.0,
    taup=1000 * units.fs
)

dyn.run(200)

vol_final = atoms.get_volume()
stress = atoms.get_stress()
pressure = - (stress[0, 0] + stress[1, 1] + stress[2, 2]) / 3 * (units.eV / units.Angstrom**3) / units.bar
print(f"Final volume: {vol_final:.2f} Å³")
print(f"Final pressure: {pressure:.2f} bar")
