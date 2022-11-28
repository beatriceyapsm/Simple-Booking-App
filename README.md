# Simple Booking App
### Outcome: 
This project creates a new event in your google calendar with information in the file “events.py” when triggered by a new commit to this github repository.

### Use case: 
If you wanted to give people a chance to add events to your calendar but not grant them full access to your gmail account, this app could come in useful. You will only need to add them as collaborators in github. 

### In building this app, I went through these steps:
1.	Built an index.html page and embedded my google calendar so the person triggering a change can do a check if the event has been successfully created. 
2.	Launched the index.html to github pages.
3.	Looked up the google calendar api guide and followed the steps to set up the environment and for python quickstart. Reference: https://developers.google.com/calendar/api/guides/overview
4.	Wrote a python script “create.py” to create a test event referencing google calendar API documentation. Adapted the script to create events using the information from “events.py” file.
5.	Wrote a workflow to run python script “create.py” whenever there is a commit to the repository. While troubleshooting the build errors, I included a dependencies file “requirements.txt” and installed them in the workflow. Ensure that the dependencies file is kept to the minimum required, otherwise the workflow will take very long to run.
6.	Tested it by changing data in “events.py” file and realized that after a period of time, access tokens expire, resulting in an authorization error. This was fixed by generating a refresh token and ensuring that is updated in the “storage.json” file.

### To Use This Code:
Step 1: Clone this repository and make it private as you will store client secrets for the app to work. I recommend working on this project with visual studio code. Link your repo in github to your visual studio code.

Step 2: In index.html, edit the iframe src to embed your google calendar (you can find this in settings and sharing for your google calendar. Under settings for your repository, go to pages and deploy from main branch to github pages. Your calendar will be hosted on https://#yourgithubusername.github.io/#yourreponame.

Step 3: Set up your environment
Reference: https://developers.google.com/calendar/api/quickstart/js
•  Create a new google cloud project: <a href="https://console.cloud.google.com/">Link</a>
•  In the Google Cloud console, enable the Google Calendar API. <a href="https://console.cloud.google.com/flows/enableapi?apiid=calendar-json.googleapis.com">Link</a>
•  To authenticate as an end user and access user data in your app, you need to create one or more OAuth 2.0 Client IDs. Configure consent screen: <a href="https://console.cloud.google.com/apis/credentials/consent">Link</a> > Configure Consent Screen > External > Key in App Name & User Support Email & Developers Email > Save and continue > Save and continue on scopes > Add your email to “Test Users” > Back to Dashboard
•  Click Create Credentials > OAuth client ID. Click Application type > Web application. In the "Name" field, type a name for the credential. This name is only shown in the Google Cloud console. Add authorized URIs related to your app: Under Client-side apps, add: https://#yourgithubusername.github.io; Under server-side apps, add: http://localhost:8080/). Click Create. The OAuth client created screen appears, showing your new Client ID and Client secret. Download json and save as credentials.json in your repository.

Step 4: Run py quickstart.py in your terminal. (I usually do this in Visual Studio Code.) 
•  You will likely face a Access blocked page with Error 400. Click on error details and copy the redirect_uri (http://localhost:XXXXX/). 
•  Go to Credentials in Google Cloud Console <a href="https://console.cloud.google.com/apis/credentials/">Link</a> >
Click on the OAuth 2.0 Client ID created for this project. Under Authorized redirect URIs, add the localhost information you copied earlier. 
•  Go back to your terminal and click on the link provided to restart the authorization process. The page will now say "Google hasn't verified this app". Click continue until you reach a page that says "The authentication flow has completed". A token.json file will be created in your repository.

Step 5: Run py create.py in your terminal. The page will say "Google hasn't verified this app". Click continue until you reach a page that says "The authentication flow has completed". A storage.json file will be created in your repository. Also, check and confirma that an event would have been created in your repository for 15 Dec 2022.

Step 6: Push your updates to your github repo. Check that your workflow runs with no error under Actions in github.


### Workflow Diagram:


### Further Applications:
You can build a front-end interface to gather user inputs to create an event instead of triggering via a commit to github.
It would also be possible to adapt the code to build a booking system in which the slots available for booking are fixed to specific ones.
