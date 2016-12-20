# BiarriTask
RESTful API that serves the content of Shakespeare’s play Henry IV


app/import.py file populates the database from specified JSON source (this is already done for Henry IV)

Homepage allows testing of POST queries


GET and DELETE can be tested using the following URLs:

  r'^speakers/$'

  r'^speakers/?((?P\<key>[\w]+)=?(?P\<value>[\w\s]+))/$'
  
  r'^plays/$'
  
  r'^plays/?((?P\<key>[\w]+)=?(?P\<value>[\w\s]+))/$'
  
  r'^lines/$'
  
  r'^lines/(?P\<limit>[\d]+)/$'
  
  r'^lines/?((?P\<key>[\w]+)=?(?P\<value>[\w\s.]+))/$'
  
  
I.e. to retrive all lines go to /lines/
     to retrieve the first 10 lines go to /lines/10
     to retrieve all lines containing the words 'and so' go to /lines/text=and so


Acceptable keys are:
  
  Lines: number, text, speaker, play, speech

  Plays: name, author
  
  Speaker: name


Please note all values are case sensitive except Lines: text
