from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto', trajectory='opt.traj')
opt.run(fmax=0.01)

nsteps = opt.get_number_of_steps()
energy = atoms.get_potential_energy()
cell_params = atoms.get_cell_lengths_and_angles()

print(f"Steps: {nsteps}")
print(f"Final energy: {energy:.6f} eV")
print(f"Cell parameters: a={cell_params[0]:.6f}, b={cell_params[1]:.6f}, c={cell_params[2]:.6f}, "
      f"α={cell_params[3]:.2f}°, β={cell_params[4]:.2f}°, γ={cell_params[5]:.2f}°")
