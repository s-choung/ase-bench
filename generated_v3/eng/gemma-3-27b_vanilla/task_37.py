from ase.build import molecule
from ase.calculators.emt import EMT
from ase.thermo import IdealGasThermo
from ase.optimize import BFGS
from ase.constraints import FixAtoms

atoms = molecule('N2', geometry='linear', symmetrynumber=2)

calc = EMT()
atoms.calc = calc

dyn = BFGS(atoms, trajectory='n2.traj')
dyn.run(fmax=0.02)

vib = atoms.calc.Vibrations()
freqs = vib.frequencies

igt = IdealGasThermo(calc)
g = igt.get_gibbs_energy(temperature=298.15, pressure=1.0)

print(g)
