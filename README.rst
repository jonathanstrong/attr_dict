*attr_dict*

There is a package, attrdict, that does horrible things to the objects you send it to. 

Specifically, all "sequences" are silently changed to tuples. If you send a list, it magically turns into a tuple. Except, not always, only if you access it as an attribute. If you access it by key, it's still a list. 

This package does not do those horrible things to the objects you send to it. It works as expected. 
