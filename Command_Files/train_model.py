#!/usr/bin/env python

import sys

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectPercentile, f_regression
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline

def train_val(X_features, y_age, age_class):
    n_splits = 10

    X_train_container = []
    X_val_container = []
    y_train_container = []
    y_val_container = []

    for i in range(n_splits):
        X_train, X_val, y_train, y_val = train_test_split(
                                                        X_features, # x
                                                        y_age, # y
                                                        test_size = 0.25, # 75%/25% split  
                                                        shuffle = True, # Shuffle dataset
                                                                        # before splitting
                                                        stratify = age_class,  # keep
                                                                               # distribution
                                                                               # of ageclass
                                                                               # consistent
                                                                               # betw. train
                                                                               # & test sets.
                                                                           )

        X_train_container.append(X_train)
        X_val_container.append(X_val)
        y_train_container.append(y_train)
        y_val_container.append(y_val)
    
    # Print size of our training and test groups
    print('training:', len(X_train),
         'testing:', len(X_val))

    return X_train_container, X_val_container, y_train_container, y_val_container

def model_fit(X_train_container, y_train_container):
    # Build a tiny pipeline that does feature selection (top 20% of features), 
    # and then prediction with our linear svr model.
    model = Pipeline([
        ('feature_selection',SelectPercentile(f_regression,percentile=20)),
        ('prediction', l_svr)
                     ])
    y_pred_all = []
    y_index_all = []

    for j in range(len(X_train_container)):

        y_pred = [] # Container to catch predictions from each fold
        y_index = [] # Index for each prediction

        # First we create 10 splits of the data
        skf = KFold(n_splits=10, shuffle=True, random_state=123)

        # For each split, assemble the train and test samples 
        for tr_ind, te_ind in skf.split(X_train_container[j]):
            X_tr = X_train_container[j][tr_ind]
            y_tr = y_train_container[j].values[tr_ind]
            X_te = X_train_container[j][te_ind]
            y_index += list(te_ind) # Store the index of samples to predict
    
            # Run pipeline 
            model.fit(X_tr, y_tr) # Fit data to the model using mini pipeline
            predictions = model.predict(X_te).tolist() # Get predictions for this fold
            y_pred += predictions # Add to list of predictions
        
        y_index_all.append(y_index)
        y_pred_all.append(y_pred)
        
    return y_index_all, y_pred_all

def main():
    X_features = sys.argv[1]
    y_age = sys.argv[2]
    age_class = sys.argv[3]
    print(X_features)
    #X_train_container, X_val_container, y_train_container, y_val_container = train_val(X_features, y_age, age_class)
    #y_index_all, y_pred_all = model_fit(X_train_container, y_train_container)
    #return y_index_all, y_pred_all

if __name__ == "__main__":
    main()