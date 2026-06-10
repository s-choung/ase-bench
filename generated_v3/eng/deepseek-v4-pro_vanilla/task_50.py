from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

eV_to_GPa = 160.21766208

metals = ['Cu', 'Ag', 'Au']
guesses = {'Cu': 3.6, 'Ag': 4.1, 'Au': 4.1}  # initial lattice constant guess

results = []
for symbol in metals:
    atoms = bulk(symbol, 'fcc', a=guesses[symbol])
    atoms.calc = EMT()
    eos = EquationOfState(atoms, npoints=10, eps=0.1)
    eos.fit()
    v0 = eos.get_equilibrium_volume()
    a0 = v0 ** (1 / 3)
    B_GPa = eos.get_bulk_modulus() * eV_to_GPa
    results.append((symbol, a0, B_GPa))

print("Metal    a0 (Å)    B0 (GPa)")
for sym, a0, B in results:
    print(f"{sym:<8} {a0:.4f}    {B:.2f}")
