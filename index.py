from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
import pprint

def insertRecords(bucket):
    print("inserting record into couchbase")
    bucket.upsert('123456789', {"title":"Harry Potter","author":[{"NRIC":"S1234567F","name":"happy"}]})
    bucket.upsert('123456787', {"title":"ABC","author":[{"NRIC":"S1234567F","name":"happy"}]})
    bucket.upsert('123456788', {"title":"Encyclopedia", "author":[{"NRIC":"S1234567G","name":"sadman"}, {"NRIC": "S1234568B", "name": "happyman"}]})
    bucket.upsert('123455', {"title":"to be deleted", "author":[{"NRIC":"S1234567G","name":"sadman"}, {"NRIC": "S1234568B", "name": "happyman"}]})
    print("inserted record into database\n")

def retrieveRecordList(bucket):
    print ("retrieving list of records\n")
    #bucket.n1ql_query('CREATE PRIMARY INDEX ON ICT2103').execute()
    from couchbase.n1ql import N1QLQuery
    row_iter = bucket.n1ql_query(N1QLQuery('SELECT * from ' + bucketname))
    for row in row_iter:
        pprint.pprint(row)
        print ("\n")
        
def retrieveRecordDetails(id, bucket):
    id = str(id)
    print("\nRetrieve " +  str(id) + " record from couchbase")
    bookObj = bucket.get(id).value 
    pprint.pprint(bookObj)

    return bookObj

def updateRecord(documentId, documentObj, bucket):
    print ("\nupdating records")
    documentId = str(documentId)
    bucket.replace(documentId, documentObj);
    print ("updated records")

def deleteRecord(documentId, bucket):
    print ("deleting record id of " + str(documentId))
    documentId = str(documentId)
    bucket.remove(documentId)
    print ("deleted record")

def deleteAttributes(documentId, documentObj, bucket):
    documentId = str(documentId)
    bucket.upsert(documentId, documentObj)

#couchbase settings
bucketname = 'ICT2103'
cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('Administrator', 'password')
cluster.authenticate(authenticator)
bucket = cluster.open_bucket(bucketname)
selectedRecord = 123456788

#insert records
insertRecords(bucket)
#retrieveRecordList(bucket)

#retrieve book details
bookObj = retrieveRecordDetails(selectedRecord, bucket)

#update properties
bookObj['title'] = "ABCD"
bookObj['tags'] = ['alphabet', 'ict2103']
updateRecord(selectedRecord, bookObj, bucket)

# display upated records
retrieveRecordDetails(selectedRecord, bucket)
deleteRecord(selectedRecord, bucket)
#retrieveRecordList(bucket)

# remove property
del bookObj['tags']
deleteAttributes(selectedRecord, bookObj, bucket)