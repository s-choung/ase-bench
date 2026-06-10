from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

# Create Cu FCC 3x3x3 supercell
cu = Atoms('Cu', cell=(3*3.61, 3*3.61, 3*3.61), pbc=True) * (3, 3, 3)
cu.calc = EMT()
cu.rattle(stdev=0.05)

# Initialize dynamics
dyn = NPTBerendsen(cu, temperature_K=300, pressure_au=1./(units.kJ/units.mol),
                   taut=100*units.fs, taup=1000*units.fs, timestep=5*units.fs)

print(f"Initial volume: {cu.get_volume():.2f} Å³")
print(f"Initial pressure: {cu.get_stress(voigt=False)[:3, :3].trace()/3/units.GPa:.2f} GPa")

# Run MD
dyn.run(200)

print(f"Final volume: {cu.get_volume():.2f} Å³")
print(f"Final pressure: {cu.get_stress(voigt=False)[:3, :3].trace()/3/units.GPa:.2f} GPa")
