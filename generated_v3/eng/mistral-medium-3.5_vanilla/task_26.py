from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

atoms = Atoms('Ni', cell=(3.52, 3.52, 3.52), cubic=True)
atoms.calc = EMT(precon='auto')
dyn = PreconLBFGS(atoms, precon='auto')
dyn.run(fmax=0.01)

print(f"Steps: {dyn.get_number_of_steps()}")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Cell: {atoms.cell.lengths()}")
