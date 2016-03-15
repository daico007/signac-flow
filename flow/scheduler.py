import warnings
from .moab import MoabScheduler
from .slurm import SlurmScheduler


try:
    from .apscheduler import APScheduler  # noqa
except ImportError:
    warnings.warn("Failed to import apscheduler. "
                  "The test scheduler will not be available.",
                  ImportWarning)

    class APScheduler(object):
        """This is a mock class.

        Install apscheduler to enable the test environment."""

        def __init__(self, *args, **kwargs):
            raise ImportError("Install apscheduler to enable this scheduler.")

__all__ = ['MoabScheduler', 'SlurmScheduler', 'APScheduler']
