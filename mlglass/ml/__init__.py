name = "Machine Learning Models"

__version__ = '0.0.1'
__author__ = 'Nikesh Bajaj'
import sys, os

sys.path.append(os.path.dirname(__file__))

#from .DeepNet import DeepNet
from .LogisticRegression import LR
from .Probabilistic import NaiveBayes
from .Trees import ClassificationTree, RegressionTree

__all__ = [ 'LR', 'NaiveBayes',
          'ClassificationTree', 'RegressionTree']
