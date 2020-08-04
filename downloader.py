import pickle
import wget
import os
import urllib.request
import sys
import errno
import requests
import shutil
import time
import os.path
from os import path
def load_obj(name ):
    with open('dict/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
if len(sys.argv) < 2:
  print("At least 1 Argument required")
  exit()
#PATH = '/projects/grail/portrait-rephotography/yoosehy/wiki_data/%s/' #'images/' + sys.argv[i] + '/'
PATH = 'images/%s/'
data = {}
year_mapper = {}
for i in range(1, len(sys.argv)):
  temp = load_obj(sys.argv[i])
  for name in temp:
    temp[name] = (sys.argv[i], temp[name])
  data.update(temp)
  print(sys.argv[i] + '  ' + str(len(temp)))

  try:
      os.mkdir(PATH % sys.argv[i])
  except OSError as e:
    pass

for name in data:
  year, (img_url, infobox) = data[name]
  print(name + ' : ' + img_url)
  #if '.' not in img_url:
  #  continue
  filepath = PATH % year
  #f = open(filepath + name + '.txt', 'wt')
  #f.write(str(infobox))
  #f.close()
  file_name, ext = os.path.splitext(img_url)
  if path.exists(filepath + name + ext):
    continue 
  #wget.download(img_url, 'images/' + name + ext)
  r = requests.get(img_url, stream = True)
  while r.status_code == 429:
    print('Waiting for API')
    time.sleep(0.5)
    r = requests.get(img_url, stream = True)
  if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filepath + name + ext,'wb') as f:
        shutil.copyfileobj(r.raw, f)
  else:
    print('Image download failed. Status code: ' + str(r.status_code))
  #urllib.request.urlretrieve(img_url, path + name + ext)

