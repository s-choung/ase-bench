from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.io import write

atoms = fcc111('Cu', size=(3, 3, 3), vacuum=12.0)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell info:\n{atoms.get_cell()}")

calc = EMT()
atoms.set_calculator(calc)
fix = FixAtoms(mask=[atom.tag > 2 for atom in atoms])
atoms.set_constraint(fix)

dyn = BFGS(atoms, trajectory='Cu100.traj')
dyn.run(fmax=0.02)

write('Cu100.xyz', atoms)
