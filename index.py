from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('Administrator', 'password')
cluster.authenticate(authenticator)
bucket = cluster.open_bucket('ICT2103')

#user details
#bucket.insert('123456789', {"title":"Harry Potter","author":[{"NRIC":"S1234567F","name":"happy"}]});
#bucket.insert('123456788', {"title":"Encyclopedia", "author":[{"NRIC":"S1234567G","name":"sadman"}, {"NRIC": "S1234568B", "name": "happyending"}]});

# print("Retrieve one Record")
# bookObj = bucket.get('123456788').value 
# print ("book title  \t" + bookObj['title'])
# for authors in bookObj['author']:
#     print ("author  \t" + authors['name'])


print("")