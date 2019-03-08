import numpy as np

class convolution:
    
    def __init__(self):
        main_arr=np.array(([1,2,3],
                           [4,5,6],
                           [7,8,9],
                           [10,11,12],
                           [13,14,15]),dtype=int)
        arr=np.array(([0,0,0,0,0],
                      [0,1,2,3,0],
                      [0,4,5,6,0],
                      [0,7,8,9,0],
                      [0,10,11,12,0],
                      [0,13,14,15,0],
                      [0,0,0,0,0]),dtype=int)
        kernel= np.array(([-1,0,2],
                             [2,0,-1],
                             [-1,0,2]
                             ),dtype=int)
        extraction=np.zeros(shape=(3,3),dtype=int)

        for i in range (main_arr.shape[0]):
          for j in range(main_arr.shape[1]):
            for k in range(i,i+kernel.shape[0]):
              for l in range(j,j+kernel.shape[1]):
                print arr[k,l],
              print
            print

if __name__=="__main__":
    conv=convolution()
    
    
