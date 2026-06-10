from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.6)          # initial lattice constant
atoms.calc = EMT()

# before optimization
c0 = atoms.get_cell_lengths_and_angles()
e0 = atoms.get_potential_energy()
print(f"Before: a,b,c = {c0[0]:.4f} {c0[1]:.4f} {c0[2]:.4f} Å")
print(f"Energy = {e0:.6f} eV")

# optimize cell and positions
flt = FrechetCellFilter(atoms)
BFGS(flt, logfile=None).run(fmax=0.01)

# after optimization
c1 = atoms.get_cell_lengths_and_angles()
e1 = atoms.get_potential_energy()
print(f"After:  a,b,c = {c1[0]:.4f} {c1[1]:.4f} {c1[2]:.4f} Å")
print(f"Energy = {e1:.6f} eV")
