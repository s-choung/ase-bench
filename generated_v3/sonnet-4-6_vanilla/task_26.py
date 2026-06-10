from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.constraints import ExpCellFilter

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

ecf = ExpCellFilter(atoms)
opt = PreconLBFGS(ecf, precon='auto')
opt.run(fmax=0.01)

steps = opt.get_number_of_steps()
energy = atoms.get_potential_energy()
cell = atoms.get_cell()
a = cell[0][0]

print(f"Steps: {steps}")
print(f"Final energy: {energy:.6f} eV")
print(f"Cell parameter a: {a:.6f} Å")
