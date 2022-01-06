# Output folder

 **score.py** contains the code for the evaluation script we're using for all of our baselines and extensions. 

In order to run scoring.py, you need two csv files in the same directory as the Scoring.py file: one containing the star ratings predictions from a model and another containing the gold standard star ratings from either the development or test set. There are several different gold standard output files due to dataloading causing reshuffling on the original dataset when used for the extensions. The table below shows which csv file corresponds to which model as well as which csv file to use as the gold standard labels.



|  Model |  Predictions on Test Set | Gold Standard Labels | 
| --|--|--|
| Average Rating Baseline | avg_baseline_output.csv| y_test_true.csv |
|Random Rating Baseline | random_baseline_output.csv |y_test_true.csv| 
| Naive Bayes Classifier Baseline | naive-bayes-strong-baseline_labels.csv| y_test_true.csv| 
| Extension 1 (RoBERTa Model) | extension1_y_pred.csv | extension1_y_true.csv | 
|Extension 2 (Bi-LSTM Model) | extension2_y_pred.csv | extension2_y_true.csv | 


Once you know which model you want to run, you can run 

	python score.py --predicted [name of predictions csv file] --true [name of gold standard ratings csv file] 

The following results will be returned:

 - **Accuracy Score:** number of label predictions exactly matching the gold standard label / total number of labels 
 - **Root Mean Squared Error (RMSE) :** defined as  ![equation](https://latex.codecogs.com/gif.latex?\sqrt{\frac{1}{n_{samples}}&space;\sum_{i=0}^{n_{samples}&space;-1}(y_i-&space;\hat{y_i})^2}2)
 
 - **Average F1:** generally defined as (2 * precision* recall) / (precision + recall) using weighted average of the F1 scores for each label.
 
 - **Confusion Matrix:** visually shows the number of instances for each combination of true and predicted labels in a png file called  - **confusion_matrix.png** that's added to the directory 
 
 
## Example 
 To evaluate the performance of the average rating baseline, run in the command line

	python score.py --predicted avg_baseline_output.csv --true y_test_true.csv
	
The following output will appear and confusion_matrix.png is added to the directory: 

	Accuracy Score:  0.2
	RMSE: 1.4142135623730951
	Average F1: 0.06666666666666668
	Confusion Matrix saved as confusion_matrix.png
	
and confusion_matrix.png is added to the directory.
