# Details of Datasets
All datasets are open source datasets and are available at 

1.	C. Tantithamthavorn, “An R package of Defect PredictionDatasets for Software Engineering Research,”https://github.com/klainfo/DefectData/tree/master/inst/extdata/terapromise, 2015.
   
2. M. D’Ambros, M. Lanza, and R. Robbes, “An extensive comparisonof bug prediction approaches,” In 2010 7th IEEE WorkingConference on Mining Software Repositories, 2010, pp. 31-41.
   
3. S. Yatish, J. Jiarpakdee, P. Thongtanunam, and C. Tantithamthavorn, “Mining software defects: Should we consider affected releases?,” In Proc. IEEE/ACM 41st Int. Conf. Software Engineering (ICSE), May 2019, pp. 654–665.

# Examples of SDP and CPDP
The Software Defect Prediction (SDP) model generally predicts future software defects from historical data using the Within Project Defect Prediction (WPDP) scenario. In the WPDP scenario, the SDP model is trained and tested on different ratios of a single dataset. The SDP model always works well when sufficient training modules/samples are available. However, in practice, most software defect datasets are small in size. Since the SDP model is generally trained using the WPDP scenario, it is very difficult to train any classifier/ machine learning algorithm using small-size datasets. So, Cross Project Defect Prediction (CPDP) is the best choice for training the SDP model. In the CPDP scenario, the SDP model is trained and tested using different datasets. In other words, we might get a training dataset with a large size for training any classifier in the CPDP scenario. 

# Details of Metrics
The details of metrics can be found from these studies:
1. M. Jureczko, “Significance of different software metrics in defect prediction,” Softw. Eng. Int. J., vol. 1, no. 1, pp. 86–95, 2011.
2. C. Tantithamthavorn, “An R package of Defect PredictionDatasets for Software Engineering Research,”https://github.com/klainfo/DefectData/tree/master/inst/extdata/terapromise, 2015.
3. M. D’Ambros, M. Lanza, and R. Robbes, “An extensive comparisonof bug prediction approaches,” In 2010 7th IEEE Working Conference on Mining Software Repositories, 2010, pp. 31-41.
4. S. Yatish, J. Jiarpakdee, P. Thongtanunam, and C. Tantithamthavorn, “Mining software defects: Should we consider affected releases?,” In Proc. IEEE/ACM 41st Int. Conf. Software Engineering (ICSE), May 2019, pp. 654–665.
