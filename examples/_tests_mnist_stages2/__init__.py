# flake8: noqa
from catalyst.dl import registry
from catalyst.dl.experiments.runner import SupervisedRunner as Runner
from .experiment import Experiment
from .model import SimpleNet

registry.Model(SimpleNet)
