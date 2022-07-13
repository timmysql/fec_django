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
from sqlmodel_model import CalendarDates
from sqlmodel import Session, select, or_
import db_connect as dbc
from sqlalchemy.exc import IntegrityError

engine = dbc.get_postgres_config()

FEC_API_KEY = "vtR7iSAdFdWJO8kvCNG13ihOP9vIyMnGpheD4LdX"


@dataclass
class CalendarDate:
    all_day: bool
    calendar_category_id: int
    category: str
    description: Optional[str]
    end_date: Optional[str]
    event_id: int
    location: Optional[str]
    start_date: str
    state: Optional[str]
    summary: str
    url: Optional[str]    



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
    calendar_dates = []
    page = 1 
    # session = requests.Session() 
    url = "https://api.open.fec.gov/v1/calendar-dates/"
    data = get_request(url=url, page=page, per_page = 100, start_date='')
    pages = get_pagination(data=data).get("pages")
    results = get_results(data=data)
    # print(pages)
    # pprint.pprint(results)
    
    for y in results:
        # pprint.pprint(y)
        # input("stop")
        cal_dict = from_dict(data_class=CalendarDate, data = y)
        calendar_dates.append(cal_dict)     
    
    for page in range(2, pages + 1):
        data = get_request(url=url, page=page, per_page = 100, start_date='')
        results = get_results(data=data)
        for y in results:
            cal_dict = from_dict(data_class=CalendarDate, data = y)
            calendar_dates.append(cal_dict) 
            
    for date in calendar_dates:
            
            insrt = CalendarDates(
        
                all_day = date.all_day,
                calendar_category_id = date.calendar_category_id,
                category = date.category,
                description = date.description,
                end_date = date.end_date,
                event_id = date.event_id,
                location = date.location,
                start_date = date.start_date,
                state = date.state,
                summary = date.summary,
                url = date.url
            )
            try:
                with Session(engine) as session:
                    session.add(insrt)    
                    session.commit()
                    session.close() 
            except IntegrityError as ie:
                pass                     
        
    # print(pages)
    # pprint.pprint(results)
    # return load

# def main():
#     data = get_request_data()
#     candidates = []
#     for y in data:
#         cand_dict = from_dict(data_class=Candidate, data = y)
#         candidates.append(cand_dict)       
        
#     for candidate in candidates:
#         print(candidate.candidate_id)
#         insrt = Candidates(
    
#             active_through = candidate.active_through,
#             candidate_id = candidate.candidate_id,
#             candidate_inactive = candidate.candidate_inactive,
#             candidate_status = candidate.candidate_status,
#             cycles = candidate.cycles,
#             district = candidate.district,
#             district_number = candidate.district_number,
#             election_districts = candidate.election_districts,
#             election_years = candidate.election_years,
#             federal_funds_flag = candidate.federal_funds_flag,
#             first_file_date = candidate.first_file_date,
#             flags = candidate.flags,
#             has_raised_funds = candidate.has_raised_funds,
#             inactive_election_years = candidate.inactive_election_years,
#             incumbent_challenge = candidate.incumbent_challenge,
#             incumbent_challenge_full = candidate.incumbent_challenge_full,
#             last_f2_date = candidate.last_f2_date,
#             last_file_date = candidate.last_file_date,
#             load_date = candidate.load_date,
#             name = candidate.name,
#             office = candidate.office,
#             office_full = candidate.office_full,
#             party = candidate.party,
#             party_full = candidate.party_full,
#             state = candidate.state
#         )
#         try:
#             with Session(engine) as session:
#                 session.add(insrt)    
#                 session.commit()
#                 session.close() 
#         except IntegrityError as ie:
#             pass
    
    

if __name__ == "__main__":
    get_request_params()