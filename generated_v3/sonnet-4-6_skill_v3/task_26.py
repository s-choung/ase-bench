from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()

filt = FrechetCellFilter(atoms)
opt = PreconLBFGS(filt, precon='auto')
opt.run(fmax=0.01)

energy = atoms.get_potential_energy()
cell = atoms.get_cell_lengths_and_angles()
a = cell[0]

print(f"Steps: {opt.get_number_of_steps()}")
print(f"Final energy: {energy:.6f} eV")
print(f"Cell parameter a: {a:.4f} Å")
