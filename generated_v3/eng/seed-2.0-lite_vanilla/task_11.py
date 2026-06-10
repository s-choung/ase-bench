from ase.build import bulk

# Create BCC Al cubic unit cell
al_atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# Print requested outputs
print("Unit cell:\n", al_atoms.cell)
print("Chemical formula:", al_atoms.get_chemical_formula())
