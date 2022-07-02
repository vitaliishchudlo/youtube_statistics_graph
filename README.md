# Media Group Ukraine - test task
### This is a test task for Media Group Ukraine company, for the position of Data Engineer.
### The main purpose of the script was - getting statistics (count of views, likes, dislikes, comments), from the specified YouTube channel (default - FootballTVUA), from each video for the period from the first to the last day of the last month. Use this statistics to graph. To get statistics - use YouTube API.

## How to start script:

1. Clone the project from github and change directory into project.
```
  $ git clone https://github.com/vitaliishchudlo/mediagroupukraine_test_task.git
  $ cd mediagroupukraine_test_task/
```

2. Create & active virtual environment and install all the necessary packages.
```
  $ python3 -m venv venv
  $ . venv/bin/activate
  $ python3 -m pip install -r requirements.txt
```
3. **For the fix problem:**

_"UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure."_

**Enter:**
```
  $ sudo apt-get install python3-tk
```

4. Run the script
```
  $ python3 app.py
```
