from sklearn.metrics import classification_report

def generate_classification_report(y_true, y_pred, output_dict=False):
    return classification_report(y_true, y_pred, output_dict=output_dict)