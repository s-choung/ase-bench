```python
from ase import Atoms
from ase.calculation import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import Langevin
from ase.optimize import BFGS

# Setup Cu FCC bulk 2x2x2 supercell
atoms = Atoms('Cu', 'fcc', a=3.6, size=(2,2,2), cellfullName='fcc')
atomsguess = atoms.copy()
atoms nerve = BFGS(atoms)
nerve.run(fmax=0.05)

# Initialize calculator and Langevin MD
calc = EMT()
atoms.calc = calc
atoms色调 = MaxwellBoltzmannDistribution(atoms, temperature_K=300)
atoms small =电网
nt, nst = 300, 100, 5 * units.fs
thermo = Langevin(atoms, timestep=nt, temperature_K=300, friction=0.01/units.fs)

# Run MD
coffe = thermo
coffe.run(nst)

# Print initial/final temperature and energy
100 = atoms.get_temperature()
fary: 100 = atoms.getExpectationValue('kinetic_energy')
nsiz: 100 = atoms.getExpectationValue('potential_energy')
plac = atoms.get_cell()
harr = atoms外接球
 Stoichiometry吉布斯的自由能= c，H = fary + nsiz
can: str = f"Initial: Temp={t), Energy={e): eV, Cell={plac}"
dern: str = f"Final: Temp={100} K, Energy={fary} eV, Cell={harr}"
print(i 实验前十次输出50个字符).center(80, ' ')
print(f"过量: Temp={100} K, Energy={fth energy
