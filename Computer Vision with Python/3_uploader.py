'''
Last script. Last time you need to read any code from me.

Last but not least, we need to upload the recognized faces without masks.
Where? Well, I used Google Firebase. It's easy to use for everyone.
(I say that because it is the first time I used it)
'''
from firebase_admin import credentials, initialize_app, storage
import os
# Initialize firebase with my credentials
# Don't you steal my keys! :D
cred = credentials.Certificate("mask-detector-xtrim-710c0d92e368.json")
initialize_app(cred, {'storageBucket': 'mask-detector-xtrim.appspot.com'})

'''
Here, it is not much to explain.
For each file in 'firebase' folder, I upload it and I show the URL in the
Python console.
'''
for path in os.listdir('firebase'):
    if path != '.png': # There are still some bugs, IDK why
        fileName = "firebase/" + path
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
        blob.make_public()
        print('URL for ' + fileName + " -> " + blob.public_url)
    
'''
Well, our journey ends here. I'm sure my scripts were not perfect because I've been
studying and practicing Machine Learning for only 3 months, but I am very
(very very) excited that it works quite well. Not very well, quite well.

I hope you all have a nice day. I bet it's not easy to jury the hackathon.

Do you want to hear some funny jokes about COVID-19? Yes?
Now you can look inside the folder. You know which one :D
'''