import urllib.parse
from sqlalchemy import URL, create_engine
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
#load_dotenv(ENV_FILE, override=True)


TABLE_NAME=os.getenv("TABLE_NAME")

def database_connection(db_name=os.getenv("DB_NAME")):
    USER=os.getenv("DB_USER")
    HOST=os.getenv("DB_HOST")
    PASSWORD=urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))
    NAME=db_name
    PORT=os.getenv("DB_PORT")

    
    DATABASE_URI = (
        f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{db_name}'
    )

    data={}
    data['engine'] = create_engine(DATABASE_URI, echo=False)
    data['database_uri'] = DATABASE_URI
    return data





CSV_DATA = 'data/raw/supply_chain_data.csv'

