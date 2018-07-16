# Contents 
1. [Introduction](README.md#Intro)
2. [Additional Subroutines](README.md#sub)
3. [Solution Approach](README.md#solapp)
4. [Unit Test ](README.md#unit-test )
5. [Full Functionality Test ](README.md#FFT)

# Introduction 
Input data set contains information on prescription drug prescribed by healthcare providers. It contains id, prescriber last and first name, drug name and cost as comma separated items. ./output/itcont.txt is a smaller unit of original input sample data with 20,000 data entry. 

# Additional Subroutines
I used two additional subroutines:

index_list : For a given sub-set of data this subroutine returns the indices from the original data set. 

count_frequency : For a given number, it returns the number of times that number repeats in a given data set. 

# Solution Approach 
./src/pharmacy‑counting.py initially declares number of data entry (NODE) of the input sample data itcont.txt. The main subroutine used for analysis named pharmacy_counting collects all column such as id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost of the txt data in data_c_dn_fn_ln_unit[] and cost_data_unit[] collects only the drug cost. L26 cleans up the entry if the entry splits more than 5 items since the header contain 5 unit. 

In step 2, data_c_dn_fn_ln_unit_v1[] was obtained from data_c_dn_fn_ln_unit[] since only last name and first name will be used to identify number of times a drug was prescribed to same individual. Sorted cost named as drug_cost[] where list items are float, has been used to identify indices ( L73: index[] ) to pick corresponding drug list ( L83: top_drugs_prescriber[] ).

L88: num_prescriber_rep[] data contains number of times top drugs were prescribed to same individuals that uses subroutine count_frequency and uses data_c_dn_fn_ln_unit_v1[] ( unsorted list of drug and its precriber ) and top_drugs_prescriber[] ( sorted list of drug and its prescriber using indices of top drugs and its prescriber in descending order ) as input to the subroutine. 

L109: top_drug_cost[] converts the costs in rounded $ to write the output top_cost_drug.txt
 
# Unit Test 
./src/pharmacy‑counting.py defines some global variables for running the test since the original input file contains roughly 24 million data points. NODE (number of data entry) variable allows to choose a subset of the input data that would be used for analysis. NOD allows us to choose any percentile of the data say 50%, 10% or 1% of the input data for analysis. 

N_unit_test is another global variable that we can vary to sort out number of top cost drugs to generate the output, top_cost_drug.txt. N_unit_test pick a subset of the data for analysis and this subset can be chosen anywhere from the original set. It allows us to choose N number of line from any portion of the sample data; i.e.; either the original sample or any smaller subunit of the sample data can be choosen for analysis.

In step 2, L50 picks a smaller unit, N_unit_test; for sorting the drug cost in descending order.  

Since the input data set contains over 24 million records from which a list of all drugs be generated as per their cost in descending order along with the number of times the same drug was prescribed by unique individual identified with the same last and first name.   

# Full Functionality Test

./output/itcont.txt has 20,000 data entry. If I run ./src/pharmacy‑counting-full-functionality.py, it takes roughly a minute on my pc, where ./output/top_cost_drug.txt contains top cost drug HARVONI, cost $ 1942090. On the other hand the lowest cost drug ZOLPIDEM TARTRATE, cost $10.    



