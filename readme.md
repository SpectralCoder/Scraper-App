#create virtual environment.
Ubuntu: python3 -m venv venv

#activate virtual environment.
Ubuntu: source venv/bin/activate

#Create .env file with 
DATABASE_URL= "your db url"
page_number= "number of pages that you want to scrape"

#install required packages (python version = Python 3.10.6)
pip install -r requirements.txt

#for scraping data, from your root folder, Run.
python3 scraper/scrape.py

#run FastAPI app
uvicorn main:app --reload 

#get swagger to check the rest apis
localhost:8000/docs

#check the the api from postman or thunderclient
http://localhost:8000/item/{pincode}

example: http://localhost:8000/item/560002




