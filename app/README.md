The approach to getting to gauging correctness was straightforward, and implemented step-wise adding new columns in a Pandas DataFrame:
1. For each row, determine whether the actual ultimate outcome was a reach or not.
2. Then determine whether the reach column was predicting a reach or not (below or above 50)
3. If actual == prediction, then that specific row was "correct"
4. Accuracy was defined as correct outcomes / total outcomes.
5. I figured for further analysis, it might be helpful to build and keep more complete DF even if it lightly increases time space complexity.

Then to automate and communicate the results automatically:
1. I built a barebones Flask web app that can run as a microservice.
2. There are several API endpoints, notably one that lets POST or upload a new file to be analyzed and then a GET for the result of the given saved file in the (theoretical) server.

To run the solution:
1. pip install -r requirements.txt
2. run python3 app.py, FLASK dev server should run on localhost/3200.
2. Use the /upload (GET) endpoint to upload the CSV to be analyzed for correctness.
3. Use the /data (GET) endpoint to get your data result.
4. Use the /boxplot (GET) endpoint to see boxplot (this feature is buggy)



Further optimizations:
As a vanilla flask app, background processes are not built-in so there is a significant bottleneck in that as new data is added via the POST uploader endpoint, every metric is recalculated before the request returns. This is not ideal, as the updating data could be calculated outside any HTTP requests, and could be easily implemented with a library such as Celery depending on the web server choice.

To parallelize for more than one outcome I would create a database with all the different datasets to analyze each with a unique key. The API endpoints could be expanded so that we would call the /data endpoint with a key attribute (referring to the specific dataset we need to analyze) and then return the data for that specific dataset.

Deploying to a Docker container would also be a logical next step.

To visualize the data, more GET endpoints could be added which automatically call MatPlotLib on the data.

There is more to it but wanted to keep this short.  I found interesting how the predictions became increasingly more accurate as we got further into the pitch count of an event e.g. (3-2 balls, outs) will be more accurate than (0-0).
