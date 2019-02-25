# InstagramApp -  Followers-Following Balance
Not to feed the anxiety and negative aspects of Social Media, but this script does something close to that. 

{Thanks to 'LevPasha'(https://github.com/LevPasha/Instagram-API-python) who helped convert the API from PHP to Python.}

This script helps look at your followers and following list and compare them to see if your friends have unfollowed you or if someone you followed you'd think would follow you back hasn't followed you because...well thats for you to judge what kind of human being they are.

There are many other functions built in to this API, allowing you to like posts etc. but the goal here is user friendliness. Just type login details, select the feature you want and run it.

While apps for this do exist and the use of this might be a little more complicated, this safety of this lies in the fact that the entire code base is presented to you. Apps may save your information and other forms of virtual malpractice. So this gives you the security that your data isn't with someone else.
The cons - It won't work too well if the followers are greater than, lets say 10k-15k. Actually I can't confirm this as I don't have that many followers.

### Setup Instructions
The base requirements for these are a Python evironment(basically an interpreter. You can use the terminal,IDEs or notebooks after you have the interpreter) and that's it.

* Then after that, on <b>Linux</b> you can do the following-

      sudo apt-get install ffmpeg
      
* As for <b>Windows</b>, you will need to run the following in your interpreter. basically go to command prompt and type- 

      >python
      >import imageio
      >imageio.plugins.ffmpeg.download()
      
* As a safety measure, you can run the requirements.txt file in the file directory. Navigate to the folder with the first command and run the .txt file with the second command-

       cd Instagram-API-python
       pip install -r requirements.txt

* And finally just run the below command as well-

      pip install InstagramApi



And you're good to go!

### Running Instructions

In the script "FollowLists.py", enter in the double quotes, the username and password variables to your username and password, and compile and run the file(these should show up in your respective notebook or IDE) and the results will be infront of you.

* If you want the users that are in your followers but not in your following, change the variables to - 

       difference = list[set(followers_list) - set(following_list)]
       
* if you want the users that are in your following but not in your followers, change the variables to - 

       difference = list[set(following_list) - set(followers_list)]
       

### Upcoming Additions - 

* Most liked posts
* Least liked posts
* Most/Least liked comments
* Celebrities that may have liked your posts
* Story viewer lists, cause Instagram has now blocked them out.

Enjoy!
    


