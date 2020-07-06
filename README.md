# Behamics tasks

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Install [MongoDB](https://docs.mongodb.com/manual/administration/install-community/).
- Install python 3

## Installation
1.Restore the mongoDB database (Be sure the database has the name Behamics_DB)
```bash
$ mongorestore Behamics_Tasks/db/ --db Behamics_DB
```
*Note: the restore database command was tested only in ubuntu os*

2.Create the virtual environment

```bash
$ pip install virtualenv
$ virtualenv behamics_env
$ source behamics_env/bin/activate
```
3.Install the requirements

```bash
$ pip install -r requirements.txt
```

## Usage
We have two folders the first one is data_tools in here we make the data manipulation with pandas, the second one is server wear we have a flask restful server.

First, we need to prepare the data for the bestseller collection.
The next command will use pandas to calculate the statistics, it will extract 20% of the most sold products per category then all the extracted data will be saved in collection bestseller. 
```bash
$ python data_tools/main.py
```
Next, we will start the flask server, where we can make an endpoint call to check if a product is a best seller.

```bash
$ python server/app.py 
```

*Note: hit this endpoint to test http://localhost:<port>/checkifbestseller/<producId> for example http://localhost:5000/checkifbestseller/10857897491*

## License
[MIT](https://github.com/Arber555/behamics_tasks/blob/master/LICENSE)