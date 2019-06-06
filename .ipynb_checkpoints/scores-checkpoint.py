import numpy as np

def score_rss(y, ypred):
    # parametros de entrada: series (colunas do dataframe)
    # y: é o valor do dataset
    # y_pred: valor da reta que estamos avaliando
    
    rs = (y - ypred)*(y - ypred)
    
    return rs.sum()

def rss(y, y_pred):
  '''parâmetros de entrada: pd.series (colunas do dataframe)
  y: é o valor real do dataset
  y_pred: valor da predição da reta que estamos avaliando
  '''
  return ((y - y_pred)**2).sum()


def rse(rss, n):
  '''Entradas são o rss e n (número de exemplos)'''
  
  return np.sqrt(rss / (n-2))
