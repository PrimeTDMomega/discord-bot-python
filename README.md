# Discord Development
So you've always wanted to impress your friends with a discord bot or just get that SWEET SWEET `Active Developer` badge on discord. Well I'm here to help, in this repository you will be able to build your own discord bot with step-by-step explainations and pre-made templates to get you started ! All in your favorite language [PYTHON](https://www.python.org) !

## Contents

 - [Chat Bot](https://github.com/PrimeTDMomega/discord-bot-python#chat-bot)
    - Requirements
       - [Prerequisets](https://github.com/PrimeTDMomega/discord-bot-python#requirements)
       - [Discord](https://github.com/PrimeTDMomega/discord-bot-python#discord)
    - [Step-by-Step](https://github.com/PrimeTDMomega/discord-bot-python#step-by-step-guide)
    - [Code Template](https://github.com/PrimeTDMomega/discord-bot-python#code-template)
- [Image Bot](https://github.com/PrimeTDMomega/discord-bot-python#image-bot)
   - [Requirements](https://github.com/PrimeTDMomega/discord-bot-python#requirements-1)
   - [Step-by-Step Guide](https://github.com/PrimeTDMomega/discord-bot-python#step-by-step-guide-1)
   - [Code Template](https://github.com/PrimeTDMomega/discord-bot-python#code-template)
- [Credits](https://github.com/PrimeTDMomega/discord-bot-python#credits)
- [LICENSE](https://github.com/PrimeTDMomega/discord-bot-python#license)

# Chat Bot
### Requirements
For a chat bot you will need a few things installed on your PC which are the following:
-   You will need to have Python installed on your system. You can download the latest version of Python from the official website ([https://www.python.org/downloads/](https://www.python.org/downloads/)) and follow the installation instructions.
    
-   You will also need to install the `discord.py` library, which provides a Python wrapper for the Discord API. You can install it using `pip install discord.py`.
    

### Discord
1.  Go to the Discord Developer Portal ([https://discord.com/developers/applications](https://discord.com/developers/applications)) and log in with your Discord account.
    
2.  Click the "New Application" button to create a new app.
    
3.  Give your app a name and click the "Create" button.
    
4.  On the next page, click the "Create a Bot" button to create a bot for your app.
    
5.  Click the "Copy" button next to the bot's token to copy it to your clipboard. This token is used to authenticate your bot with the Discord API.
    
6.  Go to the "OAuth2" tab and scroll down to the "Scopes" section.
    
7.  Check the "bot" scope and copy the URL provided. This URL is used to invite your bot to a server.

## Step-By-Step Guide
1.  Install the Discord API wrapper for Python: You can use the `discord.py` library to interact with the Discord API from your Python code. You can install it using `pip install discord.py`.
    
2.  Create a Discord bot and get its token: You will need to create a Discord bot and get its token to authenticate your Python script. You can follow the instructions in the Discord API documentation to create a bot and get its token.
    
3.  Connect the bot to your Discord server: You can use the `discord.Client` class to connect your bot to your Discord server. You will need to provide the bot's token as well as the server's ID to establish the connection.
    
4.  Respond to messages: You can use the `on_message` event to have your bot respond to messages sent in the server. You can also use the `commands` extension to create custom commands that your bot can recognize and execute.
    
5.  Implement additional features: Some ideas for additional features you could implement include:
    
    -   Moderation tools: You can create commands that allow your bot to kick or ban users, or to clear chat messages.
    -   Music playback: You can use the `discord.FFmpegPCMAudio` class to play audio files or streams in voice channels.
    -   Server management: You can create commands that allow your bot to create or delete channels, roles, or other server resources.

#### How to use the Bot
1.  Invite the bot to your server by visiting the URL you copied from the Discord Developer Portal.
    
2.  Select the server you want to add the bot to and click the "Authorize" button.
    
3.  Run the Python script on your machine. The bot should now be connected to your server and ready to respond to commands.

## Code Template 
Code template for you to get started can be found [here]()


# Image Bot
### Requirements
A few things again you will need for this bot. They are - 
1.  Install the necessary libraries:

-   `discord.py`: This library is used to interact with the Discord API. You can install it using `pip install discord.py`.
-   `requests`: This library is used to download images from the web. You can install it using `pip install requests`.
-   `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, and `google-api-python-client`: These libraries are used to authenticate with and make requests to the Google Images Search API. You can install them using `pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`.

2.  Create a Discord bot and get its token:

-   Go to the Discord Developer Portal ([https://discord.com/developers/applications](https://discord.com/developers/applications)).
-   Sign in with your Discord account.
-   Click the "New Application" button.
-   Give your application a name and click the "Create" button.
-   On the left side of the screen, click the "Bot" button.
-   Click the "Add Bot" button.
-   Copy the bot's token. You'll need this later to run the bot.

3.  Create a Google Cloud project and enable the Custom Search API:

-   Go to the Google Cloud Console ([https://console.cloud.google.com](https://console.cloud.google.com/)).
-   Sign in with your Google account.
-   Click the "Create Project" button.
-   Give your project a name and click the "Create" button.
-   On the left side of the screen, click the "APIs & Services" button.
-   Click the "Enable APIs and Services" button.
-   Search for "Custom Search API" and click on the result.
-   Click the "Enable" button.

4.  Create a Custom Search Engine:

-   On the left side of the screen, click the "APIs & Services" button.
-   Click the "Credentials" button.
-   Click the "Create Credentials" button and select "API Key".
-   Copy the API key. You'll need this later to run the bot.
-   On the left side of the screen, click the "Custom Search" button.
-   Click the "Create a Custom Search Engine" button.
-   Give your search engine a name and set the "Sites to search" to "Google Search".
-   Click the "Create" button.
-   Click on the name of your search engine.
-   Copy the search engine ID. You'll need this later to run the bot

## Step-by-Step Guide
1.  Builds a Custom Search service using the `googleapiclient` library and authenticates it using the `google-auth` and `google-auth-oauthlib` libraries.
2.  Makes a search request to the Google Images Search API using the `service.cse().list()` method. The `q` parameter specifies the search query ("capybara"), the `cx` parameter specifies the search engine ID, the `searchType` parameter specifies that the search should be limited to images, the `imgSize` parameter specifies that large images should be returned, the `num` parameter specifies the number of images to return (10), and the `key` parameter specifies the API key.
3.  Extracts the image URLs from the search results using a list comprehension.
4.  Selects a random image URL from the list of image URLs.
5.  Downloads the image using the `requests` library.
6.  Sends the image to the channel where the message was received using `message.channel.send()`.

You'll need to replace `YOUR_API_KEY` and `YOUR_SEARCH_ENGINE_ID` with your API key and search engine ID, respectively, which you can get from the Google Cloud Console. You'll also need to replace `YOUR_BOT_TOKEN_HERE` with your bot's token, which you can get from the Discord Developer Portal.

## Code Template
The code template can be found [here]()

# Credits
[PrimeTDMomega](https://github.com/PrimeTDMomega/) - Creating Bot
<br>
[Withered Knights](https://dsc.gg/witheredknights/) - Emotional Suppot lol
( Withered Knights is a group not a person )

# LICENSE
This project is licensed under the  [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

If you use  **ANY**  code from the source for an obfuscated / closed-src project :

-   You must disclose the source code of your modified work and the source code you took from this project. This means you are not allowed to use code from this project in a closed-source and/or obfuscated application.
-   You must state clearly and obviously to all end users that you are using code from this project.
-   Your application must also be licensed under the same license.

_If you have any other questions, check our  [FAQ]https://dsc.gg/witheredknights)  or ask in our  [Discord](https://dsc.gg/witheredknights)  server._

( Look I had to add this part don't take be that serious but yea )
