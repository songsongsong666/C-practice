#!/usr/bin/env python

import os.path
import os

test_dir = 'test'
if not os.path.isdir(test_dir):
    os.mkdir(test_dir)

# Writes random bytes to a file such that the file size will be between 1kb and 2kb
def create_file(path):
    import random
    bytes = [random.randint(0, 255) for x in range(0, 2**10 + random.randint(0, 2**10))]
    with open(path, 'wb') as file:
        file.write(bytearray(bytes))
    return path

# Return the file size given the path
def file_size(path):
    import os
    info = os.stat(path)
    return info.st_size

# Return a pathname to a random new file
def random_file():
    import tempfile
    file = tempfile.NamedTemporaryFile(dir = test_dir, delete = True)
    file.close()
    return file.name

# Run the cp program
def copy_file(path1, path2):
    import subprocess
    subprocess.call(['./cs5600-cp', path1, path2])

# Compute the md5 of a file path
def md5(path):
    import hashlib
    with open(path, 'rb') as file:
        md5 = hashlib.md5()
        md5.update(file.read())
        return md5.hexdigest()

# Compare md5 sums of two paths
def compare_md5(path1, path2):
    return md5(path1) == md5(path2)

if not os.path.exists('cs5600-cp'):
    print("Cannot find 'cs5600-cp'")
else:
    original = create_file(random_file())
    copied = random_file()
    print("Copying {} ({} bytes) to {}".format(original, file_size(original), copied))
    copy_file(original, copied)
    if os.path.exists(copied):
        if compare_md5(original, copied):
            print("passed")
        else:
            print("md5 comparison failed")
    else:
        print("expected to find {} but was unable to".format(copied))
