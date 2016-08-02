"""Small library that points to the drivers data set.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function



from inception.dataset import Dataset


class DriversData(Dataset):

  def __init__(self, subset):
    super(DriversData, self).__init__('Drivers', subset)

  def num_classes(self):
    """Returns the number of classes in the data set."""
    return 10

  def num_examples_per_epoch(self):
    """Returns the number of examples in the data subset."""
    if self.subset == 'train':
      return 21000
    if self.subset == 'validation':
      return 1000

  def download_message(self):
    """Instruction to download and extract the tarball from Flowers website."""

    print('Failed to find any Driver %s files'% self.subset)
    print('')
    print('If you have already downloaded and processed the data, then make '
          'sure to set --data_dir to point to the directory containing the '
          'location of the sharded TFRecords.\n')
