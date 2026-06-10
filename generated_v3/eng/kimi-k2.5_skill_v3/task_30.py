from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True) * (3, 3, 3)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def show(label):
    print(f"{label}: V = {atoms.get_volume():.3f} Å³, P = {atoms.get_pressure()/units.bar:.3f} bar")

show("Initial")
dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature=300, pressure=1.0,
                   taut=100*units.fs, taup=1000*units.fs, compressibility=7e-7)
dyn.run(200)
show("Final")
