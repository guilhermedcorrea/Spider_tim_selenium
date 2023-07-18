import sys
from sqlalchemy import text
from itertools import chain
import re
from typing import Generator, Any,Sequence
from config import engine_akiva
from .querys import qry_select


def query_database_akiva() -> Generator:
    engine = engine_akiva()
    with engine.begin () as conn:
        result = conn.execute(text(qry_select)).all()
        if next(filter(lambda k: k if len(k) >0 or re.search("[0-9]{8,}",str(k)) > 0 else None, result)):
            yield result


def get_user_infos() -> None:
    news = query_database_akiva()
    try:
        ref_user = [re.findall("[0-9]{9,16}",str(item)) for item in chain.from_iterable(news) if item != '']
        cont = len(ref_user)
        i = 0
        while i < cont:
            yield ref_user[i]
            
            i+=1

    except Exception as e:
        print(e)

