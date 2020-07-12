# kaggle-titanic
Kaggle competition on titanic prediction
In this project, we want to training titanic classification data

```markdown
- model Contains:
if model == 'svm':
    svm_training
elif model == 'knn':
    knn_training
elif model == 'tree':
    decision_tree_training
elif model == 'rf':
    rf_training
elif model == 'gnb':
    gnb_training
elif model == 'gb':
    gradient_boosting_training
elif model == 'ada':
    ada_boost_training
```

## Get started

<details>
<summary>1. If windows.</summary>

```markdown
## Step 1: Add PROJECT_PATH to your environment
$ setx /m PROJECT_PATH <PROJECT_PATH>

## Step 2: Install the python package
#### CPU version
$ pip install -r requirements.txt

## Step 3: Change the config yaml file.

## Step 4: Run the service pipeline.
$ python main.py --mode etl
$ python main.py --mode train_eval --model svm
$ python main.py --mode train_eval --model knn
$ python main.py --mode train_eval --model tree
$ python main.py --mode train_eval --model rf
$ python main.py --mode train_eval --model gnb
$ python main.py --mode train_eval --model gb
$ python main.py --mode train_eval --model ada
```
</details>

<details>
<summary>2. If linux.</summary>

```markdown
## Step 1: Add PROJECT_PATH to your environment.
$ export PROJECT_PATH=/home/app/workdir

## Step 2: Install the python package.
$ pip3 install -r requirements.txt

## Step 3: Change the config yaml file.

## Step 4: Run the service pipeline.
$ python main.py --mode etl
$ python main.py --mode train_eval --model svm
$ python main.py --mode train_eval --model knn
$ python main.py --mode train_eval --model tree
$ python main.py --mode train_eval --model rf
$ python main.py --mode train_eval --model gnb
$ python main.py --mode train_eval --model gb
$ python main.py --mode train_eval --model ada
```
</details>

## Model result
- SVM
```
              precision    recall  f1-score   support

           0       0.84      0.96      0.90        27
           1       0.93      0.72      0.81        18

    accuracy                           0.87        45
   macro avg       0.88      0.84      0.85        45
weighted avg       0.87      0.87      0.86        45
```

- KNN
```
              precision    recall  f1-score   support

           0       0.80      0.89      0.84        27
           1       0.80      0.67      0.73        18

    accuracy                           0.80        45
   macro avg       0.80      0.78      0.78        45
weighted avg       0.80      0.80      0.80        45
```

- Decision
```
              precision    recall  f1-score   support

           0       0.82      1.00      0.90        27
           1       1.00      0.67      0.80        18

    accuracy                           0.87        45
   macro avg       0.91      0.83      0.85        45
weighted avg       0.89      0.87      0.86        45
```

- RandomForest:
```
              precision    recall  f1-score   support

           0       0.79      0.85      0.82        27
           1       0.75      0.67      0.71        18

    accuracy                           0.78        45
   macro avg       0.77      0.76      0.76        45
weighted avg       0.78      0.78      0.78        45
```

- GaussianNB:
```
              precision    recall  f1-score   support

           0       0.79      0.70      0.75        27
           1       0.62      0.72      0.67        18

    accuracy                           0.71        45
   macro avg       0.71      0.71      0.71        45
weighted avg       0.72      0.71      0.71        45
```

- gradient boosting:
```
              precision    recall  f1-score   support

           0       0.78      0.93      0.85        27
           1       0.85      0.61      0.71        18

    accuracy                           0.80        45
   macro avg       0.81      0.77      0.78        45
weighted avg       0.81      0.80      0.79        45
```

- ada_boost:
```
              precision    recall  f1-score   support

           0       0.81      0.78      0.79        27
           1       0.68      0.72      0.70        18

    accuracy                           0.76        45
   macro avg       0.75      0.75      0.75        45
weighted avg       0.76      0.76      0.76        45
```

## Version, author and other information:
- See the relation information in [setup file](setup.py).

## License
- See License file [here](LICENSE).