import os
import gzip
import numpy as np

def _read32(bytestream):
  dt = np.dtype(np.uint32).newbyteorder('>')
  return np.frombuffer(bytestream.read(4), dtype=dt)[0]

def extract_labels(filename):
  """Extract the labels into a 1D uint8 np array [index]."""
  print('Extracting', filename)
  with gzip.open(filename) as bytestream:
    magic = _read32(bytestream)
    if magic != 2049:
      raise ValueError(
          'Invalid magic number %d in MNIST label file: %s' %
          (magic, filename))
    num_items = _read32(bytestream)
    buf = bytestream.read(num_items)
    labels = np.frombuffer(buf, dtype=np.uint8)
    return labels

def extract_images(filename):
  """Extract the images into a 4D uint8 np array [index, y, x, depth]."""
  print('Extracting', filename)
  with gzip.open(filename) as bytestream:
    magic = _read32(bytestream)
    if magic != 2051:
      raise ValueError(
          'Invalid magic number %d in MNIST image file: %s' %
          (magic, filename))
    num_images = _read32(bytestream)
    rows = _read32(bytestream)
    cols = _read32(bytestream)
    buf = bytestream.read(rows * cols * num_images)
    data = np.frombuffer(buf, dtype=np.uint8)
    data = data.reshape(num_images, rows, cols, 1)
    return data

def read_data_sets():

  training_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

  TRAIN_IMAGES = 'train-images-idx3-ubyte.gz'
  TRAIN_LABELS = 'train-labels-idx1-ubyte.gz'
  TEST_IMAGES = 't10k-images-idx3-ubyte.gz'
  TEST_LABELS = 't10k-labels-idx1-ubyte.gz'
  VALIDATION_SIZE = 5000

  train_images = extract_images(os.path.join(training_directory, TRAIN_IMAGES))
  train_labels = extract_labels(os.path.join(training_directory, TRAIN_LABELS))
  test_images = extract_images(os.path.join(training_directory, TEST_IMAGES))
  test_labels = extract_labels(os.path.join(training_directory, TEST_LABELS))

  validation_images = train_images[:VALIDATION_SIZE]
  validation_labels = train_labels[:VALIDATION_SIZE]
  train_images = train_images[VALIDATION_SIZE:]
  train_labels = train_labels[VALIDATION_SIZE:]

  return { 'train_images' : train_images,
            'train_labels': train_labels,
            'validation_images' : validation_images,
            'validation_labels' : validation_labels,
            'test_images' : test_images,
            'test_labels' : test_labels,
            }

if __name__ == '__main__':
    data = read_data_sets()
    image = data['train_images'][0]
    for row in image:
        for col in row:
            print('%3d' % col[0], end='')
        print("\n")
