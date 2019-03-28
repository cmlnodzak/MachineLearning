

# First, let's start by making predictions.

def predict(row,coefficients):
    yhat = coefficients[0]
    for i in range(len(row)-1):
        yhat += coefficients[i +1] * row[i]
    return yhat


# Now we can estimate coefficients by implementing stochastic gradient descent.

def coefficients_sgd(train, l_rate, n_epoch):
    coef = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0 
        for row in train:
            yhat = predict(row,coef)
            error = yhat - row[-1]
            sum_error +=error**2
            coef[0] = coef[0] - l_rate * error
            for i in rang(len(row)-1):
                
