
# Simple-baseline

To run simple-baseline.py, make sure that there is a folder called **data**  in the same directory containing the **train_data.csv**, **dev_data.csv**, and **test_data.csv** files. When this environment is set up, run the following command in the command line:

	python simple-baseline.py

Within the same directory, two csv files called **avg_baseline_output.csv** and **random_baseline_output.csv** will be added. 
**avg_baseline_output.csv** contains the predicted review ratings from the average review rating baseline on the test set while **random_baseline_output.csv** contains the predicted review ratings from the random review rating baseline on the test set.

The average review rating baseline first calculates the average star rating from all of the  Amazon reviews in the training set and assigns that value to all of the reviews in the test set. 

The random review rating baseline assigns a random rating from 1 to 5 to each of the Amazon reviews in the test set.

The following scores were achieved with these baselines calculated using **score.py**

| | Average Baseline |  Random Baseline|
| --|--|--|
|Accuracy: | 0.200 | 0.198 |
|RMSE: | 1.414 | 2.006| 
| Average F1:| 0.067| 0.198| 

