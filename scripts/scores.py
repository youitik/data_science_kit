def score_rss(y, ypred):
    # parametros de entrada: series (colunas do dataframe)
    # y: é o valor do dataset
    # y_pred: valor da reta que estamos avaliando
    
    rs = (y - ypred)*(y - ypred)
    
    return rs.sum()