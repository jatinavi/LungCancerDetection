Y_pred = model.predict(X_val)
Y_val = np.argmax(Y_val, axis=1)
Y_pred = np.argmax(Y_pred, axis=1)


#Confusion metrix

metrics.confusion_matrix(Y_val, Y_pred)

#Classification report

print(metrics.classification_report(Y_val, Y_pred,
									target_names=classes))
