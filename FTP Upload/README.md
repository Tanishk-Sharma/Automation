# FTP Upload

FTP (File Transfer Protocol) is a protocol to share files. Think about a common place where you put files and someone else can pick them up from there.

## Why is it needed?

So, no business is truly independent. They all depend on each other in some way or another. A business on its own runs on its own private network AKA Intranet.
But what to do if we need to interact with an external entity, i.e. another business? 
That's where FTP comes into the picture. Lets say an external entity requires your data, in fact, they pay for it!
You can simply zip those files into a single zip file and place it on the FTP site.
From there, the external entity can pick it up.

There is also the concept of authorizing the external entitiy to access the FTP site. But that's out of the scope of this program.

# How does the program work?

The program takes some input to begin working: 
* The location of the zipfile to upload
* FTP credentials
... Yep, that's about it.

There is another code where I take name of individual files and put them into a single zip file!
See it <a href="https://github.com/Tanishk-Sharma/Automation/tree/master/Zip%20Creator#zip-creator">here</a>
