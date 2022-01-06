# Extension 2

To run `extension2.ipynb`, we require the following files:

**Google Colab** environment

1. A folder named **data** with **train_data.csv**, **dev_data.csv** and **test_data.csv** files present under it. 

This **data** folder should be at the same level as `extension2.ipynb`.

2. A file named `word2vec-google-news-300.vectors.npy`, which is the pretrained word2vec downloaded from `Gensim`.

This file should be at the same level as `extension2.ipynb`.

3. NOTE: If you are mounting your drive in order to access the data folder, you will need to update the `base_path` variable 

to where the data folder is located on your Drive.

For example, the current base path is `base_path = '/content/drive/MyDrive/530 Project/'`. 

You will need to update the path accordingly.

4. True labels for development and test data - **val_ytrue.csv** and **y_true.csv**

5. **evaluate.py** which is the evaluation script

6. When this environment is set up, run the notebook by selecting **Runtime** and choosing **Run all**

The notebook produces two prediction files (the system predictions) called **val_ypred.csv** and **y_pred.csv**

These are used by **evaluate.py** to generate the evaluation metrics.

The following scores were achieved with this baseline calculated using **evaluate.py**

Development Data

Metric | Value
| ------- | ------- |
| Accuracy | 0.6792| 
| RMSE | 0.7744| 
| Average F1 | 0.6798| 

Test Data

Metric | Value
| ------- | ------- |
| Accuracy | 0.6761| 
| RMSE | 0.7833| 
| Average F1 | 0.677| 
