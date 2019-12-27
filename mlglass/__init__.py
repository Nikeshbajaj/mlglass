name = "Machine Learning Glass"

__version__ = '0.0.1'
__author__ = 'Nikesh Bajaj'
import sys, os

sys.path.append(os.path.dirname(__file__))

#from .DeepNet import DeepNet
from ml.LogisticRegression import LR
from ml.Probabilistic import NaiveBayes
from ml.Trees import ClassificationTree, RegressionTree

__all__ = [ 'LR', 'NaiveBayes',
          'ClassificationTree', 'RegressionTree']