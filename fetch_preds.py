from pyns import Neuroscout

api = Neuroscout()

dataset_name = 'Budapest'

mfccs = [f'mfcc_{i}' for i in range(20)]
mel = [f'mel_{i}' for i in range(64)]

all_vars = mfccs + mel

from pyns.fetch_utils import fetch_predictors


def fetch():
    predictors = fetch_predictors(all_vars, dataset_name='Budapest', subject='sid000005', run=1, rescale=True, resample=True)