from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.set_calculator(EMT())

opt = PreconLBFGS(atoms, precon='auto', fmax=0.01)
opt.run(fmax=0.01)

steps = opt.get_number_of_steps()
energy = atoms.get_potential_energy()
cell = atoms.get_cell()

print(f"Steps: {steps}")
print(f"Final energy: {energy} eV")
print(f"Cell parameters (Å): {cell[0][0], cell[1][1], cell[2][2]}")
