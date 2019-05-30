import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def gera_base_linear(seed,n_row,min_v,max_v):
    
    n = n_row
    np.random.seed(seed)

    x = np.linspace(min_v,max_v,n) # 100 values between 0 and 200
    delta = np.random.uniform(-20,20,size=(n,))
    y = .5 * x + 10 + delta * (1 + x/200)
    
    #Plot dos pontos gerados aleatoriamente
    plt.plot(x,y,'.')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Dataset')
    plt.savefig('out\dataset_exemplo_fig.png')
    plt.show()
    
    return x, delta, y 
	
def gera_pandas_base_linear(x,y,delta):
	df = pd.DataFrame()
	df["y"] = y
	df["x"] = x
	df["delta"] = delta
	df.head()
	
	return df