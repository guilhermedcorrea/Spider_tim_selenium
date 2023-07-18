
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
import os
from pathlib import Path
from dotenv import load_dotenv
from urllib import parse
import urllib
from sqlalchemy import text



def engine_akiva():
    
    db102 = create_engine("mysql+pymysql://{usuario}:{senha}@{servidor}/{bd}"
                            .format(usuario="manager", senha="xcallmanbd",
                                    servidor="172.22.20.102", bd="xcall"))
    return db102


