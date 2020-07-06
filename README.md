# Behamics tasks

## Installation
1.Restore the mongoDB database
```bash
$ mongorestore Behamics_Tasks/db/ --db Behamics_DB
```
2.Create the virtual environment

```bash
$ pip install virtualenv
$ virtualenv behamics_env
```
3.Install the requirements

```bash
$ pip install -r requirements.txt
```

## Usage
First we need to prepare the data for the bestseller collection.
The next command will use pandas to calculate the statistics, it will extract 20% of the most sold products per category then all the extracted data will be saved in collection bestseller.
```bash
$ cd src
$ python main.py
```
Next, we will start the flask server, where we can make an endpoint call to check if a product is a best seller.

```bash
$ python app.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)