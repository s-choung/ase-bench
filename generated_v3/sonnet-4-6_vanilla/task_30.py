from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
from ase.io import Trajectory

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True).repeat(3)
atoms.calc = EMT()

vol_init = atoms.get_volume()
stress_init = atoms.get_stress(voigt=True)
p_init = -stress_init[:3].mean() / units.GPa * 10000  # bar

print(f"Initial volume: {vol_init:.4f} Å³")
print(f"Initial pressure: {p_init:.4f} bar")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility_au=4.57e-5 / units.bar,
)

dyn.run(200)

vol_final = atoms.get_volume()
stress_final = atoms.get_stress(voigt=True)
p_final = -stress_final[:3].mean() / units.GPa * 10000  # bar

print(f"\nFinal volume: {vol_final:.4f} Å³")
print(f"Final pressure: {p_final:.4f} bar")
