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
from sqlmodel_model import ElectionDates
from sqlmodel import Session, select, or_
import db_connect as dbc
from sqlalchemy.exc import IntegrityError

engine = dbc.get_postgres_config()

FEC_API_KEY = "vtR7iSAdFdWJO8kvCNG13ihOP9vIyMnGpheD4LdX"


@dataclass
class ElectionDate:
    create_date: str
    election_date: str
    election_notes: Optional[str]
    election_party: Optional[str]
    election_state: Optional[str]
    election_type_full: Optional[str]
    election_type_id: Optional[str]
    election_year: int
    office_sought: Optional[str]
    primary_general_date: Optional[str]
    update_date: Optional[str]



def get_request(url, page, per_page, start_date):
    # url = "https://api.open.fec.gov/v1/candidates/"
    session = requests.Session() 
    r = session.get(url, params={'page': page, 'start_date': start_date, 'api_key': FEC_API_KEY, 'sort_null_only': False, 'per_page': per_page, 'sort_hide_null': False }).json()
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
    election_dates = []
    page = 1 
    # session = requests.Session() 
    url = "https://api.open.fec.gov/v1/election-dates/"
    data = get_request(url=url, page=page, per_page = 100, start_date='')
    pages = get_pagination(data=data).get("pages")
    results = get_results(data=data)
    # print(pages)
    # pprint.pprint(results)
    
    for y in results:
        # pprint.pprint(y)
        # input("stop")
        cal_dict = from_dict(data_class=ElectionDate, data = y)
        election_dates.append(cal_dict)     
    
    for page in range(2, pages + 1):
        data = get_request(url=url, page=page, per_page = 100, start_date='')
        results = get_results(data=data)
        for y in results:
            cal_dict = from_dict(data_class=ElectionDate, data = y)
            election_dates.append(cal_dict) 
            
    for date in election_dates:
            
            insrt = ElectionDates(
                        
                    create_date = date.create_date,
                    election_date = date.election_date,
                    election_notes = date.election_notes,
                    election_party = date.election_party,
                    election_state = date.election_state,
                    election_type_full = date.election_type_full,
                    election_type_id = date.election_type_id,
                    election_year = date.election_year,
                    office_sought = date.office_sought,
                    primary_general_date = date.primary_general_date,
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