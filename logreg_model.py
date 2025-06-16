import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression as logreg
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from data_clean import clean_data
from itertools import product

df = clean_data()
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

X = df[['Principal', 'terms', 'past_due_days', 'age', 'Gender']]
y = df['loan_status_encoded']

split = int(len(df) * 0.8)
X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

c_val = [0.01, 0.1, 1, 10]
solver = ['lbfgs']
max_iters = [200, 500, 1000, 1500]

results = []

for C, solver, max_iter in product(c_val, solver, max_iters):
    model = logreg(C=C, solver=solver, max_iter=max_iter, multi_class='multinomial')

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    mae = np.mean(np.abs(y_test - y_pred))
    rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))

    results.append({
        'C': C,
        'solver': solver,
        'max_iter': max_iter,
        'accuracy': acc,
        'mae': mae,
        'rmse': rmse
    })

results_df = pd.DataFrame(results)

results_df.to_csv('results/results_df.csv', index=False)