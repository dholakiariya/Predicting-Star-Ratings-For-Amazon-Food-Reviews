# Strong baseline

To run StrongBaseline.py, make sure that there is a folder called **data**  in the same directory containing the **train_data.csv**, **dev_data.csv**, and **test_data.csv** files. When this environment is set up, run the following command in the command line:

	python StrongBaseline.py

Within the same directory, a csv file called **prediction_labels.csv** contains the predicted review ratings from a Naive Bayes Classifier using TF-IDF vectorization on the test set.

The following scores were achieved with this baseline calculated using **score.py**


Metric | Value
| ------- | ------- |
| Accuracy | 0.491| 
| RMSE | 1.165| 
| Average F1 | 0.492| 
