from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()

def get_pressure(atoms):
    stress = atoms.get_stress()[:3]
    return -stress.sum() / 3.0 / units.GPa

v_init = atoms.get_volume()
p_init = get_pressure(atoms)

dyn = NPTBerendsen(atoms, timestep=5 * units.fs, temperature_K=300,
                   pressure=1e-4, taut=100 * units.fs, taup=1000 * units.fs)
dyn.run(200)

v_final = atoms.get_volume()
p_final = get_pressure(atoms)

print(f"Initial: Volume = {v_init:.2f} Å^3, Pressure = {p_init:.5f} GPa")
print(f"Final:   Volume = {v_final:.2f} Å^3, Pressure = {p_final:.5f} GPa")
