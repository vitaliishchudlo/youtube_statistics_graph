# **Introduction**
## YouTube Statistics Graph

The idea of this script was laid in a test task. The test task was given to me by the Ukrainian IT company - *Media Group Ukraine*, for the position of **Python Data Engineer**.

## Main aim

- The main purpose of the script was - getting statistics (count of views, likes, dislikes, comments);
- The YouTube channel is indicated by the user himself (Name, ID, link);
- Data is taken from each video on the channel from the first to the last day of the previous month;
- The YouTube API is used to retrieve data;
- The result is displayed on the graphs.

# **How to run the script:**
1. Clone the project from GitHub and change directory into project:
>
```
  $ git clone https://github.com/vitaliishchudlo/youtube_statistics_graph.git
  $ cd youtube_statistics_graph/
```

2. Create & active virtual environment and install all the necessary packages:
```
  $ python3 -m venv venv
  $ . venv/bin/activate
  $ python3 -m pip install -r requirements.txt
```
3. Run the script:
```
  $ python3 app.py
```
____

### **If the following error occurs:**

_"UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure."_

```
  $ sudo apt-get install python3-tk
```

