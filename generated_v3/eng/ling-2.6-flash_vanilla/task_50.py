from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

for metal, color in [('Cu', 'red'), ('Ag', 'blue'), ('Au', 'green')]:
    atoms = Atoms(metal, positions=[(0,0,0)], cell=(4,4,4)*4, pbc=True)
    atoms.set_calculator(EMT())
    volumes = []
    energies = []
    for scale in range(7, 12):
        atoms.set_cell((scale*4, scale*4, scale*4), scale_atoms=True)
        atoms.get_potential_energy()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    eos = EquationOfState(volumes, energies, 'birger')
    vol_eq = eos.fit_volume
    energy_eq = eos.fit(7.8) / vol_eq
    B = -eos.fit.b
    print(f'{metal:3s}  a={vol_eq**(1/3):.3f}  B={B/1e3:.1f} GPa')
