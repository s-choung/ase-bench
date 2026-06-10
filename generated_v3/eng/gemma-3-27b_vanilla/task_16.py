from ase.build import fcc110, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.io import write

atoms = fcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(f"Number of atoms: {len(atoms)}")
print(f"Cell size: {atoms.cell}")

calc = EMT()
atoms.calc = calc

fixed_layer_mask = [atom.tag > 2 for atom in atoms]
constraint = FixAtoms(mask=fixed_layer_mask)
atoms.set_constraint(constraint)

dyn = BFGS(atoms, trajectory='Fe_bcc110.traj')
dyn.run(fmax=0.02)
write('Fe_bcc110_relaxed.xyz', atoms)
