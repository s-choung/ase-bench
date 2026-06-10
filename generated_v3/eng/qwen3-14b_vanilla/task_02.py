from ase.build import fcc111
import ase

atoms = fcc111('Pt', size=(4, 4, 4), vacuum=10)
top = atoms[0].position
c = [top[0], top[1], top[2] + 1.5]
o = [top[0], top[1], top[2] + 1.5 + 1.2]
atoms += ase.Atoms('CO', positions=[c, o])
print(len(atoms))
