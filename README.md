# Details of Datasets
All datasets are open source datasets and are available at 

1.	C. Tantithamthavorn, “An R package of Defect PredictionDatasets for Software Engineering Research,”https://github.com/klainfo/DefectData/tree/master/inst/extdata/terapromise, 2015.
   
2. M. D’Ambros, M. Lanza, and R. Robbes, “An extensive comparisonof bug prediction approaches,” In 2010 7th IEEE WorkingConference on Mining Software Repositories, 2010, pp. 31-41.
   
3. S. Yatish, J. Jiarpakdee, P. Thongtanunam, and C. Tantithamthavorn, “Mining software defects: Should we consider affected releases?,” In Proc. IEEE/ACM 41st Int. Conf. Software Engineering (ICSE), May 2019, pp. 654–665.



# Details of Metrics
The detailed description of metrics can be found from these studies:
1. M. Jureczko, “Significance of different software metrics in defect prediction,” Softw. Eng. Int. J., vol. 1, no. 1, pp. 86–95, 2011.
2. C. Tantithamthavorn, “An R package of Defect PredictionDatasets for Software Engineering Research”, https://github.com/klainfo/DefectData/tree/master/inst/extdata/terapromise, 2015.
3. M. D’Ambros, M. Lanza, and R. Robbes, “An extensive comparisonof bug prediction approaches,” In 2010 7th IEEE Working Conference on Mining Software Repositories, 2010, pp. 31-41.
4. S. Yatish, J. Jiarpakdee, P. Thongtanunam, and C. Tantithamthavorn, “Mining software defects: Should we consider affected releases?,” In Proc. IEEE/ACM 41st Int. Conf. Software Engineering (ICSE), May 2019, pp. 654–665.
5. T. Menzies, "PROMISE Software Engineering Repository", http://promise.site.uottawa.ca/SERepository/datasets-page.html, 2004.

# Details of Object Oriented Metrics

WMC: Number of methods defined in a class

CBO: Count the number of classes coupled to class

RFC: Count the number of distinct methods invoke by a class in response to a received message

DIT: Depth of a class within the class hierarchy from the root of inheritance

NOC: Number of immediate descendants of a class

IC: Count the number of coupled ancestor classes of a class

CBM: Count the number of added or redefined methods those are coupled with the inherited methods

CA: Count the number of dependent classes for a given class

CE: Count the number of classes to which a class depends

MFA: Shows the fraction of the methods inherited by a class to the methods accessible by the functions defined in the class

LCOM Subtraction of method-pairs that do not share a field to the method-pairs that do

LCOM3: Counts the number of connected components in a method graph

CAM: Computes the cohesion among methods of a class based on the parameters list

MOA: Count the number of data members declared as class type

NPM: Number of public methods defines in a class

DAM: Computes the ratio of private attributes in a class

AMC: Measures the average method size for each class

LOC: Counts the total number of lines of code of a class

CC: Counts the number of logically independent paths in a method

# Details of Process Metrics

COMM: The number of Git commits

ADDED LINES: The normalized number of lines added to the module

DEL LINES: The normalized number of lines deleted from the module

ADEV: The number of active developers

DDEV: The number of distinct developers

# Details of Ownership Metrics

MINOR COMMIT: The number of unique developers who have contributed less than 5% of the total code changes (i.e., Git commits) on the module

MINOR LINE: The number of unique developers who have contributed less than 5% of the total lines of code on the module

MAJOR COMMIT: The number of unique developers who have contributed more than 5% of the total code changes (i.e., Git commits) on the module

MAJOR LINE: The number of unique developers who have contributed more than 5% of the total lines of code on the module

OWN COMMIT: The proportion of code changes (i.e., Git commits) made bythe developer who has the highest contribution of code changes on the module

OWN LINE: The proportion of lines of code written by the developer who has the highest contribution of lines of code on the module
