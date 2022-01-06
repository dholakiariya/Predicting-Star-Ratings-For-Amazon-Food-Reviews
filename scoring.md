

# Scoring.md

 **score.py** contains the code for the evaluation script we're using for all of our baselines and future extensions. 

In order to run scoring.py, you need two csv files in the same directory as the Scoring.py file: one containing the star ratings predictions from a model and another containing the gold standard star ratings from either the development or test set. In this milestone submission, the two gold standard csv files are added: **y_dev_true.csv** which contains the gold standard/true ratings on the development set and **y_test_true.csv** which constains the gold standard/true ratings on the test set.

Once you have those, you can run 

	python score.py --predicted [name of predictions csv file] --true [name of gold standard ratings csv file] 

The following results will be returned:

 - **Accuracy Score:** number of label predictions exactly matching the gold standard label / total number of labels 
 - **Root Mean Squared Error (RMSE) :** defined as  ![equation](https://latex.codecogs.com/gif.latex?\sqrt{\frac{1}{n_{samples}}&space;\sum_{i=0}^{n_{samples}&space;-1}(y_i-&space;\hat{y_i})^2}2)
 
 - **Average F1:** generally defined as (2 * precision* recall) / (precision + recall) using weighted average of the F1 scores for each label.
 
 - **Confusion Matrix:** visually shows the number of instances for each combination of true and predicted labels in a png file called **confusion_matrix.png** that's added to the directory 
 
## Example 
After running **simple-baseline.py**, a file called **avg_baseline_output.csv** which contains the average rating baseline predictions for the test file is added to the directory. To evaluate the performance of this baseline, run in the command line

	python score.py --predicted avg_baseline_output.csv --true y_test_true.csv
	
The following output will appear and confusion_matrix.png is added to the directory: 

	Accuracy Score:  0.2
	RMSE: 1.4142135623730951
	Average F1: 0.06666666666666668
	Confusion Matrix saved as confusion_matrix.png
	
and confusion_matrix.png is added to the directory. The actual png file for this is added to the submission of this milestone as an example and was renamed as "confusion_matrix_for_avg_baseline.png". Another confusion matrix example for our strong baseline is also provided as an example: "confusion_matrix_naive_bayes.png".


  

  


