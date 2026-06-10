from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

# Initial volume
initial_volume = atoms.get_volume()
print(f'Initial volume: {initial_volume:.2f} Å³')

# NPT MD
md = NPTBerendsen(atoms, timestep=5*units.fs, temperature=300, 
                  taut=100*units.fs, pressure=1, taup=1000*units.fs, 
                  compressibility=1e-4, trajectory=None)

md.run(200)

# Final volume and pressure
final_volume = atoms.get_volume()
stress = atoms.get_stress()
# Hydrostatic pressure (GPa -> bar)
pressure = -sum(stress[:3]) / 3 * 10000  # 1 GPa = 10000 bar
print(f'Final volume: {final_volume:.2f} Å³')
print(f'Final pressure: {pressure:.2f} bar')
