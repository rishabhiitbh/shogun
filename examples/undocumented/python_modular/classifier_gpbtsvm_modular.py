#!/usr/bin/env python
from tools.load import LoadMatrix
lm=LoadMatrix()

traindat = lm.load_numbers('../data/fm_train_real.dat')
testdat = lm.load_numbers('../data/fm_test_real.dat')
label_traindat = lm.load_labels('../data/label_train_twoclass.dat')

parameter_list = [[traindat,testdat,label_traindat,2.1,1,1e-5],[traindat,testdat,label_traindat,2.2,1,1e-5]]

def classifier_gpbtsvm_modular (fm_train_real=traindat,fm_test_real=testdat,label_train_twoclass=label_traindat,width=2.1,C=1,epsilon=1e-5):


	from modshogun import RealFeatures, BinaryLabels
	from modshogun import GaussianKernel
	from modshogun import GPBTSVM

	feats_train=RealFeatures(fm_train_real)
	feats_test=RealFeatures(fm_test_real)
	kernel=GaussianKernel(feats_train, feats_train, width)
	labels=BinaryLabels(label_train_twoclass)

	svm=GPBTSVM(C, kernel, labels)
	svm.set_epsilon(epsilon)
	svm.train()

	kernel.init(feats_train, feats_test)
	svm.apply().get_labels()
	predictions = svm.apply()
	return predictions, svm, predictions.get_labels()


if __name__=='__main__':
	print('GPBTSVM')
	classifier_gpbtsvm_modular(*parameter_list[0])
