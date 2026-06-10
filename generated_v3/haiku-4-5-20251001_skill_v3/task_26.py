from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameter: {atoms.get_cell_lengths_and_angles()[0]:.6f} Å")
