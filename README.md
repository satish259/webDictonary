1) Use docker-compose for the different parts of the application (web server, DB) 
2) Create a Python web application using Tornado web server. 
3) The project should have a single page with a form where I can enter a URL to any website (e.g. Wikipedia or BBCNews) 
4) The application should fetch that URL and: 
  a. Build a dictionary that contains the frequency of use of each word on that page. 
5) Use this dictionary to display, on the client’s browser, a “word cloud” of the top 100 words, where the font size is largest for the words used most frequently, and gets progressively smaller for words used less often. 
6) Each time a URL is fetched, it should save the top 100 words to a MySQL DB, with the following three columns: 
  a. The primary key for the word is a salted hash of the word. 
  b. The word itself is saved in a column that has asymmetrical encryption, and you are saving the encrypted version of the word. 
  c. The total frequency count of the word. 
 
Each time a new URL is fetched, you should INSERT or UPDATE the word rows. 
7) An “admin” page, that will: 
  a.  List all words entered into the DB, ordered by frequency of usage, visible in decrypted form. 
8) Optional 
  a. Use wit.ai to perform sentiment analysis (positive, negative) on the text of the document. Feel free to train the system in the way you wish. 
   b. each time a URL is fetched, it should save the sentiment analysis to a MySQL DB, with the following columns: 
    i. The primary key as salted hash of the URL 
    ii. The primary key as the URL 
    iii. The result of sentiment analysis (positive, negative) 
   c. In the admin, list all the URLs with their negative/positive qualification 
 
• Good project layout/structure 
• Clear README 
• Clean, well-documented code Extra points for: 
• Displaying just nouns and verbs (no prepositions or articles) 
• In the README, describe the best way to safely store and manage the encryption keys 
• Elegant front-end layout 
• Unit tests
