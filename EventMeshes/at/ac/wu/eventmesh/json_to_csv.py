import sys
import json
import csv
from faker import Factory
from collections import defaultdict
import xml.etree.ElementTree as ET

##
# Convert to string keeping encoding in mind...
##
def to_string(s):
    try:
        return str(s)
    except:
        #Change the encoding type if needed
        return s.encode('utf-8')


##
# This function converts an item like 
# {
#   "item_1":"value_11",
#   "item_2":"value_12",
#   "item_3":"value_13",
#   "item_4":["sub_value_14", "sub_value_15"],
#   "item_5":{
#       "sub_item_1":"sub_item_value_11",
#       "sub_item_2":["sub_item_value_12", "sub_item_value_13"]
#   }
# }
# To
# {
#   "node_item_1":"value_11",
#   "node_item_2":"value_12",
#   "node_item_3":"value_13",
#   "node_item_4_0":"sub_value_14", 
#   "node_item_4_1":"sub_value_15",
#   "node_item_5_sub_item_1":"sub_item_value_11",
#   "node_item_5_sub_item_2_0":"sub_item_value_12",
#   "node_item_5_sub_item_2_0":"sub_item_value_13"
# }
##
def reduce_item(key, value):
    
    #Reduction Condition 1
    if type(value) is list:
        i=0
        for sub_item in value:
            reduce_item(key+'_'+to_string(i), sub_item)
            i=i+1

    #Reduction Condition 2
    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item(key+'_'+to_string(sub_key), value[sub_key])
    
    #Base Condition
    else:
        reduced_item[to_string(key)] = to_string(value)

def reduce_item_anonym(key, value):
    
    #Reduction Condition 1
    if type(value) is list:
        i=0
        for sub_item in value:
            reduce_item_anonym(key+'_'+to_string(i), sub_item)
            i=i+1

    #Reduction Condition 2
    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item_anonym(key+'_'+to_string(sub_key), value[sub_key])
    
    #Base Condition
    else:
        skip = False
        new_value=value
        isXMl = False
        if("payload" in to_string(key)):
            # print "found!", type(value), to_string(key), "\nValue:", value
            if "https://api.otelo.de/otelo/ordering/PUA" in value:
                value.replace("https://api.otelo.de/otelo/ordering/PUA", "")
                new_value=value.strip()
#             if 'SOAP-ENV' in value:
#                 isXMl = True
            
#             if(isXMl):
#                 try:
#                     root = ET.fromstring(new_value)
#                     for
#                 except:
#                     print "Exception. The key is ",key,"\nValue is ",value, "\nType Value is ", type(value)
            try:
                payload = json.loads(new_value)
            except ValueError:
                try:
                    payload = json.loads(to_string(new_value))
                except ValueError:
                    print "Exception. The key is ",key,"\nValue is ",value, "\nType Value is ", type(value)
                    skip = True
            #print payload['last_name'], type(payload), "Faked as:", fakeFirstName[payload['last_name']]
            if skip==False and 'first_name' in payload:
                payload['first_name'] = fakeFirstName[payload['first_name']]
                payload['last_name'] = fakeLastName[payload['last_name']]
                payload['street'] = fakeStreet[payload['street']]
                payload['city'] = fakeCity[payload['city']]
                if 'address_supplement' in payload:
                    payload['address_supplement'] = fakeCompany[payload['address_supplement']]
                payload['password'] = fakePassword[payload['password']]
                payload['password_confirm'] = payload['password']
                payload['email'] = fakeEmail[payload['email']]
                payload['email_confirm'] = payload['email']
                payload['origin_owner'] = " ".join([payload['first_name'], payload['last_name']])
            # faker = Factory.create()
            #del payload['password']
        reduced_item_anonym[to_string(key)] = to_string(new_value)

def convert(node, json_string, csv_file_path):
    #Reading arguments
#     fp = open(json_file_path, 'r')
#     json_value = fp.read()
#     raw_data = json.loads(json_value)
    global reduced_item

    raw_data=json_string
    try:
        data_to_be_processed = raw_data[node]
    except:
        data_to_be_processed = raw_data

    processed_data = []
    header = []
    for item in data_to_be_processed:
        reduced_item = {}
        reduce_item(node, item)

        header += reduced_item.keys()

        processed_data.append(reduced_item)

    header = list(set(header))
    header.sort()

    with open(csv_file_path, 'w+') as f:
        writer = csv.DictWriter(f, header, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in processed_data:
#             print row
#             print json.dumps(row)
            writer.writerow(row)

    print ("Just completed writing csv file with %d columns" % len(header))


def convertAndAnynomizePayload(node, json_string, csv_file_path):
    #Reading arguments
#     fp = open(json_file_path, 'r')
#     json_value = fp.read()
#     raw_data = json.loads(json_value)
    global reduced_item_anonym
    global fakeFirstName, fakeLastName, fakeBirthdate, fakeStreet, fakeZip, fakeCity, fakeEmail, fakePassword, fakePhone, fakeCompany

    faker  = Factory.create("de_DE")
    fakeFirstName = defaultdict(faker.first_name)
    fakeLastName = defaultdict(faker.last_name)
    fakePassword = defaultdict(faker.password)
    fakeEmail = defaultdict(faker.email)
    fakeStreet = defaultdict(faker.street_name)
    fakeCompany = defaultdict(faker.company)
    fakeCity = defaultdict(faker.city)

    raw_data=json_string
    try:
        data_to_be_processed = raw_data[node]
    except:
        data_to_be_processed = raw_data

    processed_data = []
    header = []
    for item in data_to_be_processed:
        reduced_item_anonym = {}
        reduce_item_anonym(node, item)

        header += reduced_item_anonym.keys()

        processed_data.append(reduced_item_anonym)

    header = list(set(header))
    header.sort()

    with open(csv_file_path, 'w+') as f:
        writer = csv.DictWriter(f, header, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in processed_data:
            writer.writerow(row)

    print ("Just completed writing csv file with %d columns" % len(header))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print ("\nUsage: python json_to_csv.py <node_name> <json_in_file_path> <csv_out_file_path>\n")
    else:
        #Reading arguments
        node = sys.argv[1]
        json_file_path = sys.argv[2]
        csv_file_path = sys.argv[3]
        
        convert(node, json_file_path, csv_file_path)

    