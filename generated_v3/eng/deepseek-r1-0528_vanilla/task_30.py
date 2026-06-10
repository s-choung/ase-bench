from ase.build import bulk        
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Build FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True).repeat((3,3,3))
atoms.calc = EMT()

# Calculate initial properties
atoms.get_potential_energy()
initial_vol = atoms.get_volume()
s = atoms.get_stress() 
initial_p = -(s[0]+s[1]+s[2])/3 * 160.21766  # Convert eV/Å³ to GPa

# Setup and run NPT
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=0.0001,  # 1 bar in GPa
    taut=100 * units.fs,
    taup=1000 * units.fs,
    fixcm=True
)
dyn.run(200)

# Calculate final properties
final_vol = atoms.get_volume()
s = atoms.get_stress()
final_p = -(s[0]+s[1]+s[2])/3 * 160.21766

# Output
print(f'Initial volume = {initial_vol:.2f} Å³, Initial pressure = {initial_p:.4f} GPa')
print(f'Final volume = {final_vol:.2f} Å³, Final pressure = {final_p:.4f} GPa')
