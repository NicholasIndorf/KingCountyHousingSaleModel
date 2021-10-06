import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def evaluate(y_tr, tr_preds, y_te, te_preds):
    """
    Evaluate the amount error bewteen the model prediction and the actual value for both a train and test set
    
    Input:
    y_tr -array like, actual values for price for my train data set
    tr_preds - array like predictd values for my price for my train dataset
    y_te -array like, actual values for price for my test data set
    te_preds - array like predictd values for my price for my test dataset
    
    output:
    None
    """
    
    print(f"Train r2: {r2_score(y_tr, tr_preds):.4f}")
    print(f"Test r2: {r2_score(y_te, te_preds):.4f}")
    print("*****")
    print(f"Train RMSE: ${mean_squared_error(y_tr, tr_preds, squared = False):,.2f}")
    print(f"Test RMSE: ${mean_squared_error(y_te, te_preds, squared = False):,.2f}")
    print("*****")
    print(f"Train MAE: ${mean_absolute_error(y_tr, tr_preds):,.2f}")
    print(f"Test MAE: ${mean_absolute_error(y_te, te_preds):,.2f}")
    
    #calculate residuals
    train_residuals = y_tr - tr_preds
    test_residuals = y_te - te_preds
    
    #Scatterplot our residuals
    plt.scatter(tr_preds, train_residuals, label='Train')
    plt.scatter(te_preds, test_residuals, label='Test')

    plt.axhline(y=0, color = 'red', label = '0')
    plt.xlabel('predictions')
    plt.ylabel('residuals')
    plt.legend()
    plt.show()