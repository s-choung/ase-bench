from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Cu FCC 3x3x3 supercell
cu = bulk('Cu', 'fcc', a=3.615)
atoms = make_supercell(cu, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])
atoms.set_calculator(EMT())

# MD parameters
timestep = 5 * units.fs
taut = 100 * units.fs
taup = 1000 * units.fs

# Initial properties
init_vol = atoms.get_volume()
init_stress = atoms.get_stress()
init_press = -init_stress[:3].mean() * 1.602e6  # bar

print(f'Initial volume: {init_vol:.4f} Å³')
print(f'Initial pressure: {init_press:.2f} bar')

# Run NPT MD
md = NPTBerendsen(atoms, timestep, temperature=300, pressure=1 * units.bar,
                  taut=taut, taup=taup)
md.run(200)

# Final properties
final_vol = atoms.get_volume()
final_stress = atoms.get_stress()
final_press = -final_stress[:3].mean() * 1.602e6

print(f'Final volume: {final_vol:.4f} Å³')
print(f'Final pressure: {final_press:.2f} bar')
