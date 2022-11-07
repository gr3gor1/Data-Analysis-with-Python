import numpy as np
#convert to 3x3 array
def convert(list):
  new = []
  counter = 0 
  dummy = []
  for i in range(0,len(list)):
    counter = counter +1
    dummy.append(list[i])
    if(counter==3):
      counter = 0 
      new.append(dummy)
      dummy = []

  new = np.array(new)
  return new

def calculate(list):
  
  calculations = convert(list)
  #find mean values
  mean = []
  mean.append(np.ndarray.tolist(np.mean(calculations,axis=0)))
  mean.append(np.ndarray.tolist(np.mean(calculations,axis=1)))
  mean.append(np.mean(calculations))
  #find variance values
  var = []
  var.append(np.ndarray.tolist(np.var(calculations,axis=0)))
  var.append(np.ndarray.tolist(np.var(calculations,axis=1)))
  var.append(np.var(calculations))
  #find std values
  std = []
  std.append(np.ndarray.tolist(np.std(calculations,axis=0)))
  std.append(np.ndarray.tolist(np.std(calculations,axis=1)))
  std.append(np.std(calculations))
  #find max values
  amax = []
  amax.append(np.ndarray.tolist(np.amax(calculations,axis=0)))
  amax.append(np.ndarray.tolist(np.amax(calculations,axis=1)))
  amax.append(np.amax(calculations))
  #find min values
  amin = []
  amin.append(np.ndarray.tolist(np.amin(calculations,axis=0)))
  amin.append(np.ndarray.tolist(np.amin(calculations,axis=1)))
  amin.append(np.amin(calculations))
  #find sum values
  sum = []
  sum.append(np.ndarray.tolist(np.sum(calculations,axis=0)))
  sum.append(np.ndarray.tolist(np.sum(calculations,axis=1)))
  sum.append(np.sum(calculations))
  #create final dictionary
  dict={'mean':mean,'variance': var,
        'standard deviation':std,
        'max':amax,
        'min':amin,
        'sum':sum
  }
  #in case of error
  if(len(list)<9 or len(list)>9):
    raise ValueError('List must contain nine numbers.')
  
  return dict
