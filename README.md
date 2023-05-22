# Moo-with-Voting-Ensmble
<Multi-objective Optimization with Majority Voting Ensemble of Classifiers for Prediction of HIV-1 Protease Cleavage Site -->
There are four datasets, namely data746, data1625, dataSchilling and dataImpens. First structural and physicochemical-based feature extraction techniques are applied to four data set. Initially, six classifiers are considered. The selection or rejection of different classifiers is determined automatically using the search capability of a MOO technique and majority voting ensemble are applied to the outputs
of selected classifiers. NSGA-II is applied for MOO where AUC and accuracy values are optimized simultaneously.

152 features.csv containg 19 different structural and physicochemical features of individual amino acids.
moo_voting_ensemble_10_fold.py computing the Multi objective optimization based classification with voting ensemble for individual dataset in 10 Fold setup.
MOO150122_crossDomain_voting_ernsmbl.ipynb computing the Multi objective optimization based classification with voting ensemble for out-of-sample setup.
