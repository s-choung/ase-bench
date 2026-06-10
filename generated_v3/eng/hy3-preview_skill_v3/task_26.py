from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.6)
atoms.calc = EMT()

opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
steps = opt.run(fmax=0.01)

print(f"Number of steps: {steps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameters: {atoms.get_cell_lengths_and_angles()}")
