import pandas as pd 

data1 = pd.read_csv('../code(1)/analyse/operations.csv',parse_dates=[1,2])


# lets do a function to explore data
def explore_data(dataset,start,end):
    data_slice = dataset[start:end]
    for data in data_slice:
        print(data)
        print('\n')
    print("length: ",len(dataset))

#print 2 rows of dataset
print(explore_data(data1,1,len(data1)-1))
#
#We want to determine some categories and operationtype in your habits
# shopping place ...etc 
#let's write a function to find all occurence of most common words in transaction details

def find_most_common_word(dataset):
    #create a list to store all transactions by libele
    words = []
    #create a dictionary to store the result 
    most_common_word = {}
    for transaction in dataset:
        #add the splitted array in words array
        words += transaction.split(" ")
    for w in words:
        name = w
        if name not in most_common_word:
            most_common_word[name] = 1
        else:
            most_common_word[name] +=1
    return most_common_word


most_common_words = find_most_common_word(data1["libelle"])

print(most_common_words)

CATEGORIES = {
    'LOYER': 'LOYER',
    'FORFAIT COMPTE SUPERBANK': 'COTISATION BANCAIRE',
    'LES ANCIENS ROBINSON': 'COURSES',
    "L'EPICERIE DENBAS": 'COURSES',
    'TELEPHONE': 'FACTURE TELEPHONE',
    'LA CCNCF': 'TRANSPORT',
    'CHEZ LUC': 'RESTAURANT',
    'RAPT': 'TRANSPORT',
    'TOUPTIPRI': 'COURSES',
    'LA LOUVE': 'COURSES',
    'VELOC': 'TRANSPORT'
}
TYPES = {
    'CARTE': 'CARTE',
    'VIR': 'VIREMENT',
    'VIREMENT': 'VIREMENT',
    'RETRAIT': 'RETRAIT',
    'PRLV': 'PRELEVEMENT',
    'DON': 'DON',
}

##let's organise the dataset



