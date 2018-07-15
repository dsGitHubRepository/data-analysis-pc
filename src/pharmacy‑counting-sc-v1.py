
# NODE => N_of_data_entry; 500000
NODE = int(round(500000/100))
N_unit_test = 100
N_start = int(round(0))   #  24525860/2, 24520000
N = N_start + N_unit_test

def index_list(list1,sorted_list):
    #print len(list1), len(sorted_list)
    index = []
    for i in range(len(sorted_list)) :
        ind = list1.index(sorted_list[i])
        index.append(ind)
    return index

def count_frequency( list1, item1 ) :
    s = 0
    for i in range(len(list1)) :
        if item1 == list1[i] :
            s += 1
    return s

def pharmacy_counting():  
    data_c_dn_fn_ln = []
    cost_data = []
    idx = []
    data_input = open('./input/itcont.txt','r')
    for i in range(NODE) :  # 24525860
        line = data_input.readline()
        lins_sp = line.split(',')
        cs1 = lins_sp[4]
        cs = cs1.split('.')
        if ( i != 0 and len(cs) != 1 ) :
            data_c_dn_fn_ln.append(line)  # only 24516693 are cleaned up cost 99%
            cost_data.append(lins_sp[4])
            idx.append(i)                
    data_input.close()
                
    print '\n'
    #print cost_data[0:2]
    print '\n'
    #print len(cost_data)
    print '\n'
    #print idx[0:50]

    # since the input data set is large with 24 million entries, so unit test
    # can be carried on by choosing a smaller unit say 5000 entries by picking
    # then from the start, end, in the middle or anywhere from the 24 million
    # entries

    # step 2:

    data_c_dn_fn_ln_unit = data_c_dn_fn_ln[N_start:N] # data_c_dn_fn_ln list for smaller unit
    cost_data_unit = cost_data[N_start:N]
    #print cost_data[0:5]

    # since ids are not used for this analysis, hence ids need to be removed
    # from data_c_dn_fn_ln data and named as data_c_dn_fn_ln_v1

    # step 3 :

    cost = []
    drug_name = []
    data_c_dn_fn_ln_unit_v1 = []
    for i in range(len(data_c_dn_fn_ln_unit)) :
        entry_split = data_c_dn_fn_ln_unit[i].split(',')
        cost.append(entry_split[4])
        drug_name.append(entry_split[3])
        data_c_dn_fn_ln_unit_v1.append( [[entry_split[1], entry_split[2]],entry_split[3] ])

    #print data_c_dn_fn_ln_unit_v1[0:5]

    # cost[] contains the cost list of all drugs for the unit. Now top_cost[]
    # need to be sorted for all the drugs in descending order along with their
    # indices so that corresponding drug_name can be identified, as well as
    # number of times a drug was prescribed for the same prescriber.

    drug_cost = []
    for i in range(len(cost)) :
        c1 = float(cost[i])
        drug_cost.append(c1)
    drug_cost = list(set(drug_cost)) # added later
    drug_cost.sort(reverse = True)
    #print  'sorted drug_cost :', drug_cost[0:20]

    #print cost_data_unit[0:20]
    #print len(cost_data_unit), len(drug_cost)

    # convert items of cost_data_unit into float
    cost_data_unit_f = []
    for i in range( len(cost_data_unit) ) :
        c2 = float(cost_data_unit[i])
        cost_data_unit_f.append(c2)

    #print cost_data_unit_f
    index = index_list(cost_data_unit_f,drug_cost)  # calling subroutine here
    #print index[0:10]

    # Now frequency of the top drugs that was prescribed multiple times
    # to same individual need to counted based on matching the
    # drug name and full name using data_c_dn_fn_ln_unit_v1 data

    # top_cost_drug.txt with drug_name,num_prescriber,total_cost
    top_drugs_prescriber = []
    for i in range(len(index)) :
        top_drugs_prescriber.append(data_c_dn_fn_ln_unit_v1[index[i]])
    #print top_drugs_prescriber[0:5]

    num_prescriber_rep = [] # No of times a person shares the drug
    for i in range(len(index)) :
        item = top_drugs_prescriber[i]
        freq = count_frequency( data_c_dn_fn_ln_unit_v1, item )  # calling subroutine here
        num_prescriber_rep.append(freq)

    # print '\n'
    # print 'index : ', len(index), index[0:5]
    print '\n'
    print 'top_drugs_&_prescribers : ', len(top_drugs_prescriber), top_drugs_prescriber[0:3]
    print'\n'
    print 'num_of_prescriber : ', len(num_prescriber_rep), ', max value :', max(num_prescriber_rep), num_prescriber_rep[0:5]
    print '\n'
    print 'drug_cost : ', len(drug_cost), drug_cost[0:3]
    print '\n'

    # top_cost_drug.txt need to be written as :
    # drug_name,num_prescriber,total_cost :
    # CHLORPROMAZINE,2,3000

    top_drug_name = []
    top_drug_cost = []
    for i in range( len(drug_cost) ) :
        top_drug_name.append(top_drugs_prescriber[i][1])
        c = int(round(drug_cost[i]))
        top_drug_cost.append(c)

    top_drug_name.insert(0, 'drug_name')
    num_prescriber_rep.insert(0, 'num_prescriber')
    top_drug_cost.insert(0, 'total_cost')
    #print top_drug_name, num_prescriber_rep, top_drug_cost

    # write output
    output = open('./output/top_cost_drug.txt','wb')
    for k in range( len(top_drug_name) ) :
        output.write( '%s%s%s%s%s\n' % (top_drug_name[k],',',num_prescriber_rep[k],',',str(top_drug_cost[k])) )
    output.close()
    
pharmacy_counting()
