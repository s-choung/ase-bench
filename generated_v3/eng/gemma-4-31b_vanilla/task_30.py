from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.61) * (3, 3, 3)
atoms.set_calculator(EMT())
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = NPTBerendsen(
    atoms, 
    timestep=5 * units.fs, 
    temperature_K=300, 
    press=1 * units.bar, 
    taup=1000 * units.fs, 
    taut=100 * units.fs
)

v0 = atoms.get_volume()
p0 = atoms.get_pressure()

dyn.run(200)

v_final = atoms.get_volume()
p_final = atoms.get_pressure()

print(f"Initial Volume: {v0:.3f}, Pressure: {p0:.3f}")
print(f"Final Volume: {v_final:.3f}, Pressure: {p_final:.3f}")
