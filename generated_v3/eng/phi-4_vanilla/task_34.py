from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import fcc111
from ase.md import Minimize
from ase.neb import NEB
from ase.neb import Interpolator
from ase.neb import IDPP

def create_task():
    # Create initial Cu(111) surface
    sys = fcc111('Cu', size=(4, 4, 3), vacuum=10)
    
    # Create Cu adatom and add to system
    adatom = Atoms('Cu', positions=[(0.5, 0.5, 2.5)])
    sys += adatom
    sys.set_cell([[1.5, 0, 0], [0, 1.5, 0], [0, 0, 1.5]])
    sys.center()
    sys.set_pbc((True, True, False))
    
    # Calculate the initial surface with EMT
    calc = EMT()
    sys.set_calculator(calc)
    base_potential = sys.get_potential_energy()

    # Create intermediate structures with IDPP
    paths = []
    
    for i in range(1, 5):
        temp = IDPP(sys, nimages=5)
        paths.append(temp.images[i-1])
        
    # Create NEB calculation to find the minimum energy path
    neb_calc = NEB(sys, paths=paths, calculator=EMT())
    Minimize(neb_calc, steps=10)

    # Print the energy barrier
    diff_in_trajectory = neb_calc.get_maximum_energy_difference()
    barrier = diff_in_trajectory - base_potential
    print("Energy barrier: {:.3f} eV".format(barrier))

create_task()
