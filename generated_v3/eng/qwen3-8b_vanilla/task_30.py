from ase import Atoms
from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md import NPTBerendsen
from ase.units import fs, bar

atoms = bulk('Cu', 'fcc', cubic=True)
supercell = make_supercell(atoms, [[3,0,0],[0,3,0],[0,0,3]])
atoms.set_calculator(EMT())

initial_volume = atoms.get_volume()
dynamics = NPTBerendsen(atoms, temperature_K=300, pressure=1.0*bar, taut=100*fs, taup=1000*fs, dt=5*fs)
dynamics.run(200)
final_volume = atoms.get_volume()

print(f"Initial volume: {initial_volume}")
print(f"Final volume: {final_volume}")
print(f"Pressure: {1.0*bar}")
