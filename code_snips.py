# fetching 
import os
import urllib.request
# create ssl context required
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if not os.path.isdir('img_align_celeba'):
  os.mkdir('img_align_celeba')

for img_i in range(1, 11):

    f = '000%03d.jpg' % img_i
    url = 'https://s3.amazonaws.com/cadl/celeb-align/' + f
    print(url, end='\r')
    urllib.request.urlretrieve(url, os.path.join('img_align_celeba', f))
    
print [file_i for file_i in os.listdir('img_align_celeba') if '.jpg' in file_i] # os.listdir() takes one argument - Folder Path.
                                                                                # If path is None, uses the path='.'


# Loading an image

import matplotlib.pyplot as plt

#We'll now tell matplotlib to "inline" plots using an ipython magic function:
%matplotlib inline

help(plt)

plt.imread?  # bring functions documentation

"""
Read an image from a file into an array.

*fname* may be a string path, a valid URL, or a Python
file-like object.  

- If using a file object, it must be opened in binary mode.

If *format* is provided, will try to read file of that type,
otherwise the format is deduced from the filename.  

- If nothing can be deduced, PNG is tried.

Return value is a :class:`numpy.array`. 
- For grayscale images, the return array is MxN.  
- For RGB images, the return value is MxNx3.
- For RGBA images the return value is MxNx4.

"""

# plt.imread will not know where that file is. We can tell it where to find the file by using os.path.join

plt.imread(os.path.join(file_folder, image.png))

  
