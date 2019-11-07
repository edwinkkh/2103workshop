from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('Administrator', 'password')
cluster.authenticate(authenticator)
bucket = cluster.open_bucket('ICT2103')

#user details
bucket.upsert('123456789', {"title":"Harry Potter","author":[{"NRIC":"S1234567F","name":"happy"}]});
bucket.upsert('123456787', {"title":"ABC","author":[{"NRIC":"S1234567F","name":"happy"}]});
bucket.upsert('123456788', {"title":"Encyclopedia", "author":[{"NRIC":"S1234567G","name":"sadman"}, {"NRIC": "S1234568B", "name": "happyending"}]});

# print("Retrieve one Record")
bookObj = bucket.get('123456788').value 
print ("book title  \t" + bookObj['title'])
for authors in bookObj['author']:
    print ("author  \t" + authors['name'])


#bucket.n1ql_query('CREATE PRIMARY INDEX ON ICT2103').execute()
from couchbase.n1ql import N1QLQuery
row_iter = bucket.n1ql_query(N1QLQuery('SELECT * from ICT2103'))
for row in row_iter:
    print (row) 
    print ('\n')
    #print ('book title \t' + row.title)