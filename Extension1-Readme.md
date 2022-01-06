# Extension 1

To run BestModel.ipynb, we require the following files:

**Google Colab** environment

1. A folder named **data** with **train_data.csv**, **dev_data.csv** and **test_data.csv** files present under it.

2. True labels for development and test data - **Y_true_Dev.csv** and **Y_true_Test.csv**

3. **evaluate.py** which is the evaluation script

4. When this environment is set up, run the notebook by selecting **Runtime** and choosing **Run all**

The notebook produces two prediction files called **Dev_Output.csv** and **Test_Output.csv**
These are used by **evaluate.py** to generate the evaluation metrics.

The following scores were achieved with this baseline calculated using **evaluate.py**

Development Data

Metric | Value
| ------- | ------- |
| Accuracy | 0.6795| 
| RMSE | 0.7388| 
| Average F1 | 0.678| 

Test Data

Metric | Value
| ------- | ------- |
| Accuracy | 0.683| 
| RMSE | 0.7049| 
| Average F1 | 0.683| 
