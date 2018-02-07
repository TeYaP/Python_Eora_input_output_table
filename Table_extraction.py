import pandas as pd


basepath = "PATH_EXAMPLE/Eora_IO_tables/EORA_IO_table_CountryX"

country_code = "MAJ" # 3 letters in MAJ
year_min = "1900" # Year 4 digits
year_max = "1901" # Year 4 digits
price_type = "PurchasersPrice" # "BasicPrice" or "PurchasersPrice"
file_extention = ".txt" # txt tab separated only, if not change first for loop
table = "use_tables" # 

dict_table = dict()

for year in range(int(year_min),int(year_max)+1):
    filename = "IO_"+country_code+"_"+str(year)+"_"+price_type
    file = basepath + "/" + filename + file_extention
    data = pd.read_csv(file, 'r',
    	delimiter="\t", 
    	header = None)
    info = data.iloc[0][0].replace(' Purchasers Prices', ' Price: Purchasers').replace(':', ';').replace(' ','').split(';')
    if table == "use_table":
    	dict_table[year] = data.iloc[129:325,4:129] # select data matrix
    	colnames = data.iloc[0:4,4:129] # select column names
    	rownames = data.iloc[129:325,0:4] # select row names
    	dict_table[year] = colnames.append(dict_table[year]) # "murge" column names to data
    	dict_table[year] = pd.concat([rownames, dict_table[year]], axis=1) # "murge" row names to data
    	dict_table[year][0][0] = info[0]
    	dict_table[year][1][0] = info[1]
    	dict_table[year][0][1] = info[2]
    	dict_table[year][1][1] = info[3]
    	dict_table[year][0][2] = info[4]
    	dict_table[year][1][2] = info[5]
    	dict_table[year][0][3] = info[6]
    	dict_table[year][1][3] = info[7]
    	del colnames, rownames
    else:
    	if table == "make_table":
    		dict_table[year] = data.iloc[4:129,129:325] # select data matrix
    		colnames = data.iloc[0:4,129:325] # select column names
    		rownames = data.iloc[4:129,0:4] # select row names
    		dict_table[year] = colnames.append(dict_table[year]) # "murge" column names to data
    		dict_table[year] = pd.concat([rownames, dict_table[year]], axis=1) # "murge" row names to data
    		dict_table[year][0][0] = info[0]
    		dict_table[year][1][0] = info[1]
    		dict_table[year][0][1] = info[2]
    		dict_table[year][1][1] = info[3]
    		dict_table[year][0][2] = info[4]
    		dict_table[year][1][2] = info[5]
    		dict_table[year][0][3] = info[6]
    		dict_table[year][1][3] = info[7]
    		del colnames, rownames
    	else: 
    		print("ERROR...!!! \n table or year or non-well specified")

print(dict_table)
