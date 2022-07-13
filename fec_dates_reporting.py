from sys import flags
# from types import NoneType
import requests
from rich import inspect
import pprint
import json
from dataclasses import dataclass, field, MISSING
# from typing import List
from typing import Optional, List, Union
from datetime import date, datetime
from dacite import from_dict
from sqlmodel_model import ReportingDates
from sqlmodel import Session, select, or_
import db_connect as dbc
from sqlalchemy.exc import IntegrityError
from settings import FEC_API_KEY
engine = dbc.get_postgres_config()


@dataclass
class ReportingDate:
    create_date: str
    due_date: str
    report_type: str
    report_type_full: Optional[str]
    report_year: int
    update_date: str



def get_request(url, page, per_page, due_date):
    # url = "https://api.open.fec.gov/v1/candidates/"
    session = requests.Session() 
    r = session.get(url, params={'page': page, 'due_date': due_date, 'api_key': FEC_API_KEY, 'sort_null_only': False, 'per_page': per_page, 'sort_hide_null': False }).json()
    return r

def get_pagination(data):    
    dump = json.dumps(data.get("pagination"))
    pagination = json.loads(dump)      
    return pagination
 
def get_results(data):
    dump = json.dumps(data.get("results"))
    results = json.loads(dump)    
    return results   




def get_request_params():
    reporting_dates = []
    page = 1 
    # session = requests.Session() 
    url = "https://api.open.fec.gov/v1/reporting-dates/"
    data = get_request(url=url, page=page, per_page = 100, due_date='')
    pages = get_pagination(data=data).get("pages")
    results = get_results(data=data)
    # print(pages)
    # pprint.pprint(results)
    
    for y in results:
        # pprint.pprint(y)
        # input("stop")
        cal_dict = from_dict(data_class=ReportingDate, data = y)
        reporting_dates.append(cal_dict)     
    
    for page in range(2, pages + 1):
        data = get_request(url=url, page=page, per_page = 100, due_date='')
        results = get_results(data=data)
        for y in results:
            cal_dict = from_dict(data_class=ReportingDate, data = y)
            reporting_dates.append(cal_dict) 
            
    for date in reporting_dates:
            
            insrt = ReportingDates(
                        
                    create_date = date.create_date,
                    due_date = date.due_date,
                    report_type = date.report_type,
                    report_type_full = date.report_type_full,
                    report_year = date.report_year,
                    update_date = date.update_date
            )
            try:
                with Session(engine) as session:
                    session.add(insrt)    
                    session.commit()
                    session.close() 
            except IntegrityError as ie:
                pass                     
        

    

if __name__ == "__main__":
    get_request_params()