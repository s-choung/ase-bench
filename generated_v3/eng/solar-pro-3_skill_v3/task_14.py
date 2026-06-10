from ase import Atoms

NaCl = Atoms('NaCl',
             positions=[(0, 0, 0), (0.5, 0.5, 0.5)],   # Na at origin, Cl at body‑center
             cell=(5.64, 5.64, 5.64, 90, 90, 90),     # cubic Fm‑3m
             pbc=True)

NaCl.calc = EMT()   # Ensure a calculator is attached (optional for this demo)

print('Number of atoms:', len(NaCl))
print('Chemical symbols:', NaCl.get_chemical_symbols())
