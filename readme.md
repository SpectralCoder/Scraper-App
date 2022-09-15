### create virtual environment. <br>
Ubuntu: ````python3 -m venv venv````

### activate virtual environment.<br>
Ubuntu: ````source venv/bin/activate````

### Create .env file with <br>
````
DATABASE_URL= "your db url"
page_number= "number of pages that you want to scrape"
````

### install required packages (python version = Python 3.10.6)<br>
````pip install -r requirements.txt````

### for scraping data, from your root folder, Run.<br>
````python3 scraper/scrape.py````

### run FastAPI app<br>
````uvicorn main:app --reload```` 

### get swagger to check the rest apis<br>
````localhost:8000/docs````

### check the the api from postman or thunderclient<br>
````
http://localhost:8000/item/{pincode}
example: http://localhost:8000/item/560002
````




