# CCIcalc
Charlson Comorbidity Index (CCI) Score Calculator
Estimating Prognosis for Dialysis Patients
Programmed by: Mostafa Mohamed on March 21, 2015
Live example is setup on Google could engine at: http://main-element-89114.appspot.com/?age=55&factors=MI,CVA,dementia,COPD 

The repository contains a function written in Python programming language in the file "ccicalc.py".
To call it you must pass in the patient ages as the first parameter then all patient conditions as a list of parameters as follows:
```Python
	ccicalc(age, *args)
```    
The conditions can be passed as a one string or list of strings as:
```Python
	e.g.: ccicalc(55, 'MI, CVA, dementia, COPD')

	or    ccicalc(55, 'MI', 'CVA', 'dementia', 'COPD')
``` 
The function will clean-up the parameters list to remove duplicates and unknown inputs.
The function returns the result in text form as follows:
```
	"Charlson Comorbidity Index (CCI) Score: 4 Age factored in: 5."
```
The list of input arguments for patient conditions is divided into 4 sets as listed below:

Parameter       | 	Description
--------------- | -------------------------------------------------------------------
_1- One Point_ 	|
MI		|		Myocardial infarction (history, not ECG changes only)
CHF		|		Congestive heart failure
PVD		|		Peripheral disease (includes aortic aneurysm >= 6 cm
CVA		|		Cerebrovascular disease: CVA with mild or no residua or TIA
Dementia	|	Dementia
COPD		|	Chronic pulmonary disease
CTD		|		Connective tissue disease
PUD		|		Peptic ulcer disease
CLD_mild	|	Mild liver disease (without portal hypertension, includes chronic hepatitis)
DM_mild		|	Diabetes without end-organ damage (excludes diet-controlled alone)
_2- Two Points_	|
Hemiplegia	|	Hemiplegia
CKD		|		Moderate or severe renal disease
DM_severe	|	Diabetes with end-organ damage (retinopathy, neuropathy, nephropathy, or brittle diabetes)
Tumor 		|	Tumor without metastasis (exclude if > 5 y from diagnosis)
Leukemia 	|	Leukemia(acute or chronic)
Lymphoma	|	Lymphoma
*3- Three Points*|
CLD_severe	|	Moderate or severe liver disease
_4- Six Points_	|
Mets		|	Metastatic solid tumor
AIDS		|	AIDS (not just HIV positive)
 
Note: the parameters are not case sensitive.
