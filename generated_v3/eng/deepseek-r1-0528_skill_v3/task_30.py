from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

bar_per_ev_ang3 = 160.21766208 * 1e4

vol0 = atoms.get_volume()
press0 = atoms.get_isotropic_pressure() * bar_per_ev_ang3
print(f"Initial: {vol0=:.3f} Å³, Pressure={press0:.3f} bar")

md = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300,
                 pressure_bar=1.0, taut=100*units.fs, taup=1000*units.fs)
md.run(200)

vol_f = atoms.get_volume()
press_f = atoms.get_isotropic_pressure() * bar_per_ev_ang3
print(f"Final:   {vol_f=:.3f} Å³, Pressure={press_f:.3f} bar")
