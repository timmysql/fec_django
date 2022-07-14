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
from sqlmodel_model import Candidates
from sqlmodel import Session, select, or_
import db_connect as dbc
from sqlalchemy.exc import IntegrityError
from settings import FEC_API_KEY
from fec_requests import FecRequest


engine = dbc.get_postgres_config()



@dataclass
class Candidate:
    active_through: int
    candidate_id: str
    candidate_inactive: bool
    candidate_status: str
    cycles: List[int]
    district: str
    district_number: int
    election_districts: List[str]
    election_years: List[int]
    federal_funds_flag: bool
    first_file_date: Optional[str] = field(default=None, init=False) 
    flags: str
    has_raised_funds: bool
    inactive_election_years: Optional[List[int]] = field(default=None, init=False) 
    incumbent_challenge: Optional[str]
    incumbent_challenge_full: Optional[str]
    last_f2_date: Optional[str] = field(default=None, init=False) 
    last_file_date: Optional[str] = field(default=None, init=False) 
    load_date: Optional[str] = field(default=None, init=False) 
    name: str
    office:str
    office_full: str
    party: Optional[str]
    party_full: Optional[str]
    state: str  
    



# nebraska_candidates = f"https://api.open.fec.gov/v1/candidates/?state=NE&sort_nulls_last=false&sort=name&api_key={FEC_API_KEY}&sort_null_only=false&page=1&per_page=20&sort_hide_null=false"

# def get_request(url, params):
#     # url = "https://api.open.fec.gov/v1/candidates/"
#     session = requests.Session() 
#     r = session.get(url, params=params).json()
#     # r = session.get(url, params={'page': page, 'state': state, 'api_key': FEC_API_KEY, 'sort_null_only': False, 'per_page': per_page, 'sort_hide_null': False }).json()
#     return r

# def get_pagination(data):    
#     dump = json.dumps(data.get("pagination"))
#     pagination = json.loads(dump)      
#     return pagination
 
# def get_results(data):
#     dump = json.dumps(data.get("results"))
#     results = json.loads(dump)    
#     return results   

# def get_request_data():    
#     search_get = nebraska_candidates
#     r = requests.get(search_get)                
#     data = r.json() 
#     dump = json.dumps(data.get("results"))
#     load = json.loads(dump)
#     return load


def get_request_params():
    candidates = []
    page = 1 
    session = requests.Session() 
    # page=page 
    per_page = 20
    state='NE'
    params = {'page': page, 'state': state, 'api_key': FEC_API_KEY, 'sort_null_only': False, 'per_page': per_page, 'sort_hide_null': False }
    url = "https://api.open.fec.gov/v1/candidates/"                            
    data = get_request(url=url, params=params)
    pages = get_pagination(data=data).get("pages")
    results = get_results(data=data)
    for y in results:
        cand_dict = from_dict(data_class=Candidate, data = y)
        candidates.append(cand_dict)     
    
    for page in range(2, pages + 1):
        data = get_request(url=url, params=params)
        results = get_results(data=data)
        # cand_dict = from_dict(data_class=Candidate, data = results)
        # candidates.append(cand_dict)
        for y in results:
            cand_dict = from_dict(data_class=Candidate, data = y)
            candidates.append(cand_dict) 
            
    for candidate in candidates:
            print(candidate.candidate_id)
            insrt = Candidates(
        
                active_through = candidate.active_through,
                candidate_id = candidate.candidate_id,
                candidate_inactive = candidate.candidate_inactive,
                candidate_status = candidate.candidate_status,
                cycles = candidate.cycles,
                district = candidate.district,
                district_number = candidate.district_number,
                election_districts = candidate.election_districts,
                election_years = candidate.election_years,
                federal_funds_flag = candidate.federal_funds_flag,
                first_file_date = candidate.first_file_date,
                flags = candidate.flags,
                has_raised_funds = candidate.has_raised_funds,
                inactive_election_years = candidate.inactive_election_years,
                incumbent_challenge = candidate.incumbent_challenge,
                incumbent_challenge_full = candidate.incumbent_challenge_full,
                last_f2_date = candidate.last_f2_date,
                last_file_date = candidate.last_file_date,
                load_date = candidate.load_date,
                name = candidate.name,
                office = candidate.office,
                office_full = candidate.office_full,
                party = candidate.party,
                party_full = candidate.party_full,
                state = candidate.state
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

def main():
    data = get_request_data()
    candidates = []
    for y in data:
        cand_dict = from_dict(data_class=Candidate, data = y)
        candidates.append(cand_dict)       
        
    for candidate in candidates:
        print(candidate.candidate_id)
        insrt = Candidates(
    
            active_through = candidate.active_through,
            candidate_id = candidate.candidate_id,
            candidate_inactive = candidate.candidate_inactive,
            candidate_status = candidate.candidate_status,
            cycles = candidate.cycles,
            district = candidate.district,
            district_number = candidate.district_number,
            election_districts = candidate.election_districts,
            election_years = candidate.election_years,
            federal_funds_flag = candidate.federal_funds_flag,
            first_file_date = candidate.first_file_date,
            flags = candidate.flags,
            has_raised_funds = candidate.has_raised_funds,
            inactive_election_years = candidate.inactive_election_years,
            incumbent_challenge = candidate.incumbent_challenge,
            incumbent_challenge_full = candidate.incumbent_challenge_full,
            last_f2_date = candidate.last_f2_date,
            last_file_date = candidate.last_file_date,
            load_date = candidate.load_date,
            name = candidate.name,
            office = candidate.office,
            office_full = candidate.office_full,
            party = candidate.party,
            party_full = candidate.party_full,
            state = candidate.state
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
    # print(engine)