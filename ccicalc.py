#!/usr/local/bin/python2.7
# encoding: utf-8
'''
ccicalc -- shortdesc

ccicalc is a function calculates the Charlson Comorbidity Scoring Index

It defines classes_and_methods

@author:     Mostafa Mohamed

@copyright:  2015 Mostafa Mohamed. All rights reserved.

@license:    MIT

@contact:    mostafa_17@hotmail.com
@deffield    March 21, 2015: Updated
'''


def ccicalc(age, *args):
    ''' This function calculates the Charlson Comorbidity Scoring Index
    
        The first argument is the patient age, the rest are the list of patient conditions
        The argument list in not case sensitive and duplicates are ignored
        The return is a string in the form of "Charlson Comorbidity Index (CCI) Score: 9 Age factored in: 10"
        '''
    #print "This function calculates the Charlson Comorbidity Scoring Index"
    one_point = ['MI', 'CHF', 'PVD', 'CVA', 'dementia', 'COPD', 'CTD', 'PUD', 'CLD_mild', 'DM_mild'] # One point condition factors
    two_point = ['hemiplegia', 'CKD', 'DM_severe', 'tumor', 'leukemia', 'lymphoma'] # Two points condition factors
    thr_point = ['CLD_severe'] # Three points condition factors
    six_point = ['mets', 'AIDS'] # Six points condition factors
    points = 0
    argr = ''
    args1 = ','.join(args).encode('ascii','ignore')
    args2 = ''
    if len(args1)>0: 
        args2 = args1.split(',')
        
    for arg in args2:  # change the input arguments to lower case
        argr = argr + arg.encode('ascii','ignore').lower().strip() + ','
        
    #print argr
    #return '&'.join(argr)
    for case in one_point:  # Calculate the one point factors
        if case.lower() in argr:
            points+= 1
        #print case, type(case), points, 'Points'        
    #return str(points)    
    for case in two_point:  # Calculate the two points factors
        if case.lower() in argr:
            points+= 2
    
    for case in thr_point:  # Calculate the three points factors
        if case.lower() in argr:
            points+= 3
    
    for case in six_point:  # Calculate the six points factors
        if case.lower() in argr:
            points+= 6
        
    #return str(points)
    # Calculate the age factor
    agef = int(age) - 40
    
    if agef < 0:
        agef = 0
    else:
        agef = agef // 10

    
    r = "Charlson Comorbidity Index (CCI) Score: %(1)i Age factored in: %(2)i. " % {'1':points, '2':agef+points}
    
    if points < 2:
         r+= "Data not available if CCI less than 2."
         
    #print r
    return r

#ccicalc(10, 'MI', 'PVD')

