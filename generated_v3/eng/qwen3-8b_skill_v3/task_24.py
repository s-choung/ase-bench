from ase import bulk, EMT, LBFGS

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
atoms.calc = EMT()
opt = LBFGS(atoms)
opt.run(fmax=0.01)
print(f"Steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy()}")
