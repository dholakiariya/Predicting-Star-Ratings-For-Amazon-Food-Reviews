import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, mean_squared_error, f1_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from argparse import ArgumentParser


def warn(*args, **kwargs): pass
import warnings; warnings.warn = warn


parser = ArgumentParser()

parser.add_argument("-p", "--predicted", dest = "pred_path",
    required = True, help = "path to your model's predicted labels file")

parser.add_argument("-d", "--true", dest = "true_path",
    required = True, help = "path to the true labels file")

args = parser.parse_args()

pred = pd.read_csv(args.pred_path, header=None)
true  = pd.read_csv(args.true_path, header=None)

print('Accuracy Score: ', accuracy_score(true, pred))
print('\n')
print('RMSE: ', np.sqrt(mean_squared_error(true,pred)))
print('\n')
print('Average F1:', f1_score(true,pred, average="weighted"))
print('\n')
print('Confusion Matrix saved as confusion_matrix.png \n')

cm =confusion_matrix(true, pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[1,2,3,4,5])
disp.plot()
plt.savefig("confusion_matrix.png")
