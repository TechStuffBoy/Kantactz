# Kantactz
This is a Django Project for Managing the contacts or addressbook for the users.

# Features
1. Users can signup themselves. 
2. Password reset functionality provided, so if for any reason, user has locked out himself, he can use this functionality to get un-block himself.
3. User can view only his contacts. If accessed others details, 403 page will be shown.
4. Added RestFul APIs to the project which supports CRUD operation, so contacts can be created using APIs from other frontends as well. Currently BasicAuthentication being Implemented.
5. Only authenticated and authorized users can work with APIs. 

# Developer Specific 
1. Error Pages will be shown for respective errors, like, 404, 500, 403 errors.
2. SQL queries are being spit out in the Django server logs (they are not being stored in a log file as of now)
3. Reset emails will be stored in a File System. For production, a valid SMTP should be used as well as settings to be updated as well.
4. If you are using POSTMAN or Curl, make sure to pass the Authentication information as well before sending any request.
