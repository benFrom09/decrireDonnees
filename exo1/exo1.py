from csv import reader
opened_file = open("../code(1)/analyse/operations.csv",encoding="utf-8")
data = list(reader(opened_file))
#header of dataset
dataset_header = data[0]
# lets do a function to explore data
def explore_data(dataset,start,end):
    data_slice = dataset[start:end]
    for data in data_slice:
        print(data)
        print('\n')
    print("length: ",len(dataset))

#print header to see variable 
print("Header:",dataset_header)
#print 2 rows of dataset
print(explore_data(data,1,len(data)-1))
#
#We want to determine some categories and operationtype in your habits
# shopping place ...etc 
#let's write a function to find all occurence of most common words in transaction details

def find_most_common_word(dataset):
    #create a list to store all transactions by libele
    words = []
    #create a dictionary to store the result 
    most_common_word = {}
    for transaction in dataset[1:]:
        libelle = transaction[3]
        #add the splitted array in words array
        words += libelle.split(" ")
    for w in words:
        name = w
        if name not in most_common_word:
            most_common_word[name] = 1
        else:
            most_common_word[name] +=1
    return most_common_word


most_common_words = find_most_common_word(data[1:])

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

