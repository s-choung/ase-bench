from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

v_i = atoms.get_volume()
p_i = -atoms.get_stress()[:3].mean() / units.GPa

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature=300, pressure=1*units.bar,
                   taut=100*units.fs, taup=1000*units.fs, compressibility=1/(140*units.GPa))
dyn.run(200)

v_f = atoms.get_volume()
p_f = -atoms.get_stress()[:3].mean() / units.GPa

print(f"Initial Volume: {v_i:.2f} Å^3, Pressure: {p_i:.2f} GPa")
print(f"Final Volume:   {v_f:.2f} Å^3, Pressure: {p_f:.2f} GPa")
