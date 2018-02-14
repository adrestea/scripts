"""This program will do 'find and replace', and save an output to a different file"""
#You should have openoffice listening on specified port already.
#Load necessary items
import uno
local = uno.getComponentContext()
resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)

#Load file template
document = desktop.loadComponentFromURL("file:///home/lucas/TemplateLetter.odt" ,"_blank", 0, ())
cursor = document.Text.createTextCursor()


#----------Start doing stuff--------
import string

#Create Search Descriptor
print 'starting a search'
search = document.createSearchDescriptor()

def findandreplace(document=document,search=search,find=None,replace=None):
    """This function searches and replaces. Create search, call function findFirst, and finally replace what we found."""
    #What to search for
    search.SearchString = unicode(find)
    #search.SearchCaseSensitive = True
    #search.SearchWords = True
    found = document.findFirst( search )
    if found:
        print 'Found %s' % find
    while found:
        found.String = string.replace( found.String, unicode(find),unicode(replace))
        found = document.findNext( found.End, search)


#Create data structure of what will get replaced. I assume that "$FirstName", etc. are already in you odt file.
data={}
data['$FirstName']='Lucas'
data['$LastName']='Mylastname'
data['$Address']='123 Main St.'
data['$City']='Chicago'
data['$State']='IL'
data['$Zipcode']='60645'
data['$TodaysDate']='20080821'
data['$DOB']='My Date of Birth'

#Do a loop of the data and replace the content.
for find,replace in data.items():
    findandreplace(document,search,unicode(find),unicode(replace))
    print find,replace


#Save document
document.storeAsURL("file:///home/lucas/letter2.odt",())
#Close
document.dispose()
