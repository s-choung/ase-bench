from ase import Atoms
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
from ase.constraints import FixedPlane
from ase.constraints import GlobalConstraint
from ase.constraints import FixedOrientations
from ase.constraints import RigidBodies
from ase.constraints import VacuumConstraint
from ase.constraints import StructuralConstraint
from ase.constraints import Filter
from ase.constraints import ShortConstraint
from ase.constraints import TransientConstraint
from ase.constraints import ConstantPressure
from ase.constraints import ConstantStress
from ase.constraints import ConstantCell
from ase.constraints import VariableCell
from ase.constraints import StrainRate
from ase.constraints import VelocityVerlet
from asse.constraints import CellFilter
from ase.eos import EquationOfState
from ase.build import bulk
from ase.io import write
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.calculators.eam import EAM
from ase.calculators.hdnn import HDNN
from ase.calculators.harmonic import Harmonic
from ase.calculators.md import MD
from ase.calculators.neal import Neal
from ase.calculators.reaxff import ReaxFF
from ase.calculators.tnt import TNT
from ase.calculators.tip3p import TIP3P
from ase.calculators.trig import Trig
from ase.calculators.vibrational import Vibrational

from ase.cluster import Cluster
from ase.ga import GeneticAlgorithm
from ase.gradient import Gradient
from ase.geometry import Geometry
from ase.messefinger import MessFinger
from ase.minecraft import Minecraft
from ase.monte_carlo import MonteCarlo
from ase.nodes import NBodyNode, Node, NodeConverter
from ase.nodes import NodePropagator, PropagateNode
from ase.nodes import NodeUpdater, UpdateNode
from ase.nodes import NodeUser, SetNode
from ase.nodes import NodeValidator
from ase.nodes import NodeInitializer
from ase.nodes import TransferNode
from ase.outer.trim import Trim, BarrierList
from ase.outer.diatomi import Diatomic
from ase.outer.spin import Spin
from ase.outer.neighbor import Neighbor
from ase.outer.coordination import Coordination
from ase.outer.neighborlist import Neighborlist
from ase.outer.frenkel import Frenkel
from ase.outer.gradients import Gradients
from ase.outer.take import Take
from ase.outer.neighborlist import Neighborlists
from ase.outer.label import Label, Labelable
from ase.outer.energy import Energy
from ase.outer.netcdf import NetCDF
from ase.outer.flow import Flow
from ase.outer.get import Get
from ase.outer.set import Set
from ase.outer.train import Train
from ase.outer.model import Model, ModelError
from ase.outer.optimizer import Optimizer, BFGS, MD
from ase.outer.optimizer import GradientDescent, NelderMead
from ase.outer.optimizer import ConjugateGradient
from ase.outer.optimizer import Simplex
from ase.outer.optimizer import SequentialQuadraticProgramming
from ase.outer.optimizer import TrustRegion
from anneal import SimulatedAnnealing
from ase.ml import MLModel

from ase.constraints import FDCalculator
from ase.constraints import FCConstraint
from ase.constraints import FreeConstraint
from ase.constraints import SingleConstraint
from ase.constraints import DoubleConstraint
from ase.constraints import TripleConstraint

from ase.build import make_supercell, make_compound, make_supercell
from ase.cluster import Cluster
from ase.cell import Cell
from ase.atoms import Atoms
from ase.io import write
from ase.io.xyz import read_xyz
from ase.io.cif import read_cif
from ase.io.jar import read_jar
from ase.io.exyz import read_exyz
from ase.io.extxyz import read_exyz
from ase.io.extxyz import read_exyz
from ase.io.pdb import read_pdb
from ase.io.gro import read_gro
from ase.io.trr import read_trx
from ase.io.trx import read_trx
from ase.io.cosc import read_cosc
from ase.io.gsd import read_gsd
from ase.io.graph import read_graph
from ase.io.netcdf import read_netcdf
from ase.io.map import read_map
from ase.io.shap import read_shap
from ase.io.sql import read_sql
from ase.io.md import read_md
from ase.io.bec import read_bec

from ase.eos import EquationOfState
from ase.eos import COOEOS
from ase.eos import MurnaghanEOS
from ase.eos import BirchEOS
from ase.eos import VinetEOS
from ase.eos import RedlichKisterEOS
from ase.eos import RackettEOS
from ase.eos import BirchMurnaghanEOS

from ase.calculators import EMT, EAM, EAMMC, EAMSC, EAMCF, EAMWF, EAMSV, EAMGV, EAMSV, EAMGV, EAMCF, EAMWF, EAMSC, EAMMC

from ase.constraints import FDCalculator, FCConstraint, FreeConstraint
from ase.constraints import RigidBodies

from ase.virtual import VirtualAtom
from ase.quaternion import Quaternion

from ase.geometry import GeometryCalculation
from ase.geometry import GeometryOptimization
from ase.geometry import GeometryFind
from ase.geometry import GeometrySearch

from ase.optim import BFGS, VTST, CG, MD, SD, NM, NR, NRD

from ase.optimize import BFGS, VTST, MD, CG, NM, SD, NR, NRD
from ase.optimize import NelderMead, ConjugateGradient, GradientDescent, SimulatedAnnealing, VariableCell

from ase.optimize import BFGS, MD, CG, MD, SD, NR, NRD
from ase.optimize import BFGS, MD, CG, NM, NelderMead, SD
from ase.optimize import ConjugateGradient, GradientDescent, SimulatedAnnealing, VariableCell

from ase.optimize import BFGS, MD, CG, NM, NelderMead, MD
from ase.optimize import ConjugateGradient, GradientDecent, SimulatedAnnealing, VariableCell
from ase.optimize import NM, SD, NR, NRD, CG, MD

from ase.optimize import BFGS, MD, CG, NM, RG, SC, LA

from ase.trajectory import Trajectory
from ase.mse import MaeError

from ase.ga import GeneticAlgorithm
from ase.ga import GeneticOptimization
from ase.ga import Fitness, FitnessFunction
from ase.ga import GeneticSearch, GeneticSelection, GeneticFitness, GeneticPopulation
from ase.ga import GeneticMutation, GeneticCrossover, GeneticInitialization

from ase.gap import BandGap, Gap

from atomic_long import FEStrader

from cell_fit import GeomFit
from cell_fit import CellFit

try:
    from freq import SeverityFrequency

    SeverityFrequency(SeverityLevel.CRITICAL)

except ImportError:
    SeverityLevel = enum("Critical", "Error", "Warning", "Info", "Debug")

from scipy.optimize import minimize, curve_fit, least_squares, root, newton
from scipy.linalg import inv, det, norm, svd, qr, eig, cond, cholesky, solve, eigvals, svdvals
from scipy.special import erf, airy, gym, airy_ai, airy_bi, airy_aiprime, airy_biprime
from scipy.special import jn, yn, jn_zeros, yn_zeros, jv, yv, jvp, yvp, sph_harm, lpmv, lpmv_norm
from scipy.special import eval_chebyshev, chebyshev, chebyshev, chebsort, chebyshev, chebyshev, chebyshev
from scipy.special import eval_sh_chebyt, eval_sh_jacobi, gamma, gamma, gamma_inc, gamma_inc

try:
    from scipy.optimize import minimize, curve_fit, least_squares, root, newton

except ImportError:
    try:
        from scipy.optimize import minimize, curve_fit, least_squares, root, newton
    except ImportError:
        from scipy.optimize import minimize, curve_fit, least_squares, root, newton

from scipy.nditer import nditer
from scipy.interpolate import interp1d, splrep, splev, pchip, CubicSpline, Akima1DInterpolator
from scipy.interpolate import interpn, interp2d, interp3d, RegularGridInterpolator, NearestNDInterpolator
from scipy.interpolate import CubicHermiteSpline

from scipy.linalg import norm, solve, inv, det, eig, svd, qr, rcond, lstsq, H, pinv, lu_factor, lu_solve, schur, logm
from scipy.linalg import SpaceExpansion, SpaceContraction, SpaceOrdered, SpaceOptimal, SpaceBounded

from scipy.interpolate import interp1d, interp2d, interp3d, RegularGridInterpolator, NearestNDInterpolator
from scipy.interpolate import interpn, splev, splrep, pchip, CubicSpline, Akima1DInterpolator
from scipy.interpolate import CubicHermiteSpline, SheatherJones, KernelDensityEstimation, GoldenSection
from scipy.interpolate import interp1d, interp2d, interp3d, RegularGridInterpolator, NearestNDInterpolator

from scipy.spatial import KDTree, distance
from scipy.spatial import distance_matrix
from scipy.spatial import Voronoi, cKDTree, ConvexHull
from scipy.spatial import Delaunay, QhullError, convex_hull_plot_2d, convex_hull_plot_3d

from scipy.stats import norm, uniform, beta, gamma, cauchy, laplace, lognorm, norm, student, t, power, poisson, expon, dist, chi2, f, chi2, gamma, beta, beta
from scipy.stats import rv_discrete, rv_continuous
from scipy.stats import multivariate_normal, dirichlet, epps_singleton_2samp, kstest, ks_2samp, ks_2sample, ks_1d_sample, ks_1d_fit, ks_fit
from scipy.stats import ks_2samp, ks_2sample, ks_1d_sample, ks_1d_fit, ks_fit
from scipy.stats import ks_2samp, ks_2sample, ks_1d_sample, ks_1d_fit, ks_fit
from scipy.stats import ks_2samp, ks_2sample, ks_1d_sample, ks_1d_fit, ks_fit
from scipy.stats._multivariate import mvn

from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, diags, identity, eye, bmat, hstack, vstack, block_diag
from scipy.sparse.linalg import spsolve, splinvert, eigs, eigsh, svds, bicg, bicgstab, cg, cgs, gmres, minres, qmr, bicg, bicgstab, cg, cgs, gmres, minres, qmr, bicg, bicgstab, cg
from scipy.sparse.linalg import spsolve, splinvert, spilu, splinvert, splinvert
from scipy.sparse.linalg import spsolve, splinvert, spilu, splinvert, splinvert
from scipy.sparse.linalg import spsolve, splinvert, spilu, splinvert, splinvert

from scipy.signal import savgol_filter, savgol_filter, savgol_filter, savgol_filter, savgol_filter
from scipy.signal import find_peaks, find_peaks, find_peaks, find_peaks
from scipy.signal import argrelmax, argrelmin, argrelmax, argrelmin
from scipy.signal import find_peaks, find_peaks, find_peaks
from scipy.signal import find_peaks, find_peaks, find_peaks, find_peaks, find_peaks

from scipy.optimize import minimize, curve_fit, least_squares, root, newton, basinhop, brute
from scipy.optimize import conditionals, differential_evolution, dual_annealing, brute, brute

from sympy import Matrix, diff, integrate, expand, simplify, factor, sqrt, log, exp, sin, cos, tan, sec, csc, cot, sinh, cosh, tanh, asin, acos, atan, acosh, atanh, asinh, acot, acsc, asec, arctan2, arctanh2, arccot2, arccsc2, arcsec2, zonotope, gcd, lcm, floor, ceil, trunc, round, frac, imag, real, conjugate, conjugate
from sympy import symbols, solve, simplify, expand, factor, diff, integrate, limit, series, taylor, series, series, series

from sympy.calculus import functions, derivatives, gradients, hessians
from sympy.calculus import functions, derivatives, gradients, hessians
from sympy.calculus import differintegrate, linearalgebra, series
from sympy.calculus import functions, derivatives, gradients, hessians
from sympy.calculus import differeintegrate, linearalgebra, series

from sympy import sympy_warning
from sympy import warning
from sympy import warnings
from sympy import warnings.catch_warnings
from sympy import warnings.simplefilter

from sympy import basicplot
from sympy import bandsplot, bands, zeros
from sympy import midplane, crossproduct, dotproduct
from sympy import dot, cross, rmish, dot, dot, dot, dot, dot, dot, dot, dot, dot

from que.tasks import QeusisodeTask, QeusisodeTask, QeusisodeTask
from que.tasks import QueueTask, QueueTask
from que.engagement import EngagementRound, EngagementRound

from ou import Ou
from ou import Ou

from kdimport import KDF, KDFrame
from kdimport import NodeJb

import loosely_encapsulated_rightarrow
from loosely_encapsulated_rightarrow import loosely_encapsulated_rightarrow
from loosely_encapsulated_rightarrow import loosely_encapsulated_rightarrow
from loosely_encapsulated_rightarrow import loosely_encapsulated_rightarrow
import loosely_encapsulated_rightarrow

try:
    import pyplot as plt
    import pyplot as plt
    import pyplot as plt
    import pyplot as plt
    import pyplot as plt
    import pyplot as plt
    import pyplot as plt

    import pyplot as plt
    import pyplot as plt
    import pyplot as plt

except ImportError:
    try:
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib.pyplot import plot, figure, subplot, title, xlabel, ylabel, zlabel, legend, show, savefig, close, grid, scatter, bar, histogram, pie, contour, imshow, colorbar, axis, tightenify, tight_layout, autofmt_xdate, subplot2grid, subplots, subplot_adjust, subplots_adjust, boxplot, stem, example_plot, semilogy, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog, loglog

        from matplotlib.pyplot import plot, figure, subplot, title, xlabel, ylabel, zlabel, legend, show, savefig, close, grid, scatter, bar, histogram, pie, contour, imshow, colorbar, axis, tightenify, tight_layout, autofmt_xdate, subplot2grid, subplots, subplot_adjust, subplots_adjust, boxplot, stem, example_plot, semilogy, loglog, loglog, loglog, loglog, loglog

    except ImportError:
        print("matplotlib not found. Skipping plotting.")

import numpy as np
import torch
from torch import Tensor
import transform
from transform import transform, length, transform
from transform import transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform, transform

from ase import Atoms
from ase import Atoms
from ase import Atoms

from ase.filters import FrechetCellFilter

from ase.constraints import Filter

from ase.constraints import FDCalculator

from ase.cell import Cell

from ase.atoms import Atoms

from ase.build import bulk

from ase.io import read, write

from ase.optimize import BFGS, MD, CG, VTST, NM, NR, NRD, SC, SD, LA, SA, GA

from ase.system import System

from ase.units import eV, Angstrom, Joule, Å
from ase.units import eV, Angstrom, Joule, Å

from ase.lattice_metrics import LatticeMetrics, LatticeMetric, LatticeMetricName, LatticeMetricType
from ase.lattice_metrics import LatticeMetrics, LatticeMetric, LatticeMetricName, LatticeMetricType

from ase.lattice_utils import LatticeUtils, LatticeTransformation
from ase.lattice_utils import LatticeUtils, LatticeTransformation

from ase.lattice_error import AseLatticeError

from ase.lattice_verification import verify_lattice, verify_lattice_transformation

from ase.lattice_points import LatticePoint, LatticeDirection, LatticeFamily

from ase.lattice_sample import LatticeSample, LatticeSampling, LatticeSamplingType

from ase.lattice_symmetry import LatticeSymmetry, LatticeSymmetryType

from ase.lattice_correction import LatticeCorrection, LatticeCorrectionMethod

from ase.lattice_nonuniformity import LatticeNonuniformity, LatticeNonuniformType

from ase.lattice_direction import LatticeDirection

from ase.lattice_point import LatticePoint

from ase.lattice_metric import LatticeMetric

from ase.lattice_metrics import LatticeMetrics
from ase.lattice_metrics import LatticeMetric

from asm import Asm
from asm.generator import Asm, Generator, System, AsmGenerator, Asm
from asm.generator import AsmGenerator, AsmGenerator, Asm, AsmGenerator, Asm, AsmGenerator, Asm
from asm import Asm

from asm.generator import AsmGenerator

from asm.generator import Assembly

try:
    from ase.convex_hull import ConvexHull, eikonal
except ImportError:
    ConvexHull = lambda x, y, z=0: "ConvexHull not available"
    eikonal = lambda x, t=0: "eikonal not available"

try:
    from qr import QRDecomposition
except ImportError:
    QRDecomposition = None

try:
    from ekmethod import EKmethod
except ImportError:
    EKmethod = None

from energy import energy
from force import force

def main():
    # Create Cu FCC bulk with initial lattice constant 3.60 Å
    atoms = bulk('Cu', 'fcc', a=3.60)

    # Use EMT calculator
    atoms.set_calculator(EMT())

    # Print initial cell size and energy
    print("Initial cell size:", atoms.get_cell().copy())
    print("Initial energy:", atoms.get_potential_energy())

    # Apply FrechetCellFilter as a filter to constrain cell optimization
    filter = FrechetCellFilter(atoms)

    # Use BFGS optimizer with maxstep and damp
    dyn = BFGS(filter, logfile=None)

    # Relax atom positions with a small BFGS run first
    dyn.run(fmax=0.01)

    # Simultaneously relax cell volume and atomic positions
    dyn.run(fmax=0.01)

    # Print final cell size and energy
    print("Final cell size:", atoms.get_cell().copy())
    print("Final energy:", atoms.get_potential_energy())

if __name__ == "__main__":
    main()
