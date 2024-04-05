# Coding Temple Mini-Project Contact Management

Project starts by importing contacts if the contacts.txt file exists else there are no preexisting contacts.

The user is allowed to add new contacts, edit or add to existing ones, delete contacts, and search contacts. 

The user can also export contacts to save a contacts.txt file for future uses. And this file is updated when the program is exited as long as it is exited using the proper quit command.

Also contacts are displayed and sorted by name and the lists are updated to be sorted whenever these are called. It might be more efficient to maintain the list as sorted whenever a value is added but this way was simpler for me and was how I decided to implement because people will not care if it is sorted until they try and view it. Also the sorting should not take long because I do not think someone will go over a thousand contacts.