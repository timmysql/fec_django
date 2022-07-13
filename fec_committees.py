from sys import flags
# from types import NoneType
import requests
from rich import inspect
import pprint
import json
from dataclasses import dataclass, field, MISSING
# from typing import List
from typing import Optional, List, Union, Dict
from datetime import date, datetime
from dacite import from_dict
from sqlmodel_model import Committees
from sqlmodel import Session, select, or_
import db_connect as dbc
from sqlalchemy.exc import IntegrityError
from settings import FEC_API_KEY

engine = dbc.get_postgres_config()


@dataclass
class Committee:
    affiliated_committee_name: Optional[str] = field(default=None, init=False) 
    candidate_ids: List[str]
    committee_id: str
    committee_type: str
    committee_type_full: str
    cycles: List[int]
    designation: Optional[str]
    designation_full: Optional[str]
    filing_frequency: str
    first_f1_date: Optional[str]
    first_file_date: str
    last_f1_date: Optional[str]
    last_file_date: str
    name: str
    organization_type: Optional[str]
    organization_type_full: Optional[str]
    party: Optional[str] = field(default=None, init=False) 
    party_full: Optional[str] = field(default=None, init=False) 
    sponsor_candidate_ids: Optional[List[str]] = field(default=None, init=False) 
    # sponsor_candidate_list: Dict[str, Union[str, bool, int]]
    sponsor_candidate_list: List[Dict[str, str]] 
    # sponsor_candidate_list: Optional[List[int]] = field(default=None, init=False) 
    state: str
    treasurer_name: Optional[str]
    

def get_request(url, page, per_page, state):
    # url = "https://api.open.fec.gov/v1/candidates/"
    session = requests.Session() 
    r = session.get(url, params={'page': page, 'state': state, 'api_key': FEC_API_KEY, 'sort_null_only': False, 'per_page': per_page, 'sort_hide_null': False }).json()
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
    committees = []
    page = 1 
    session = requests.Session() 
    url = "https://api.open.fec.gov/v1/committees/"                            
    data = get_request(url=url, page=page, per_page = 20, state='NE')
    pages = get_pagination(data=data).get("pages")
    results = get_results(data=data)
    for y in results:
        comm_dict = from_dict(data_class=Committee, data = y)
        committees.append(comm_dict)     
    
    for page in range(2, pages + 1):
        data = get_request(url=url, page=page, per_page = 20, state='NE')
        results = get_results(data=data)
        # cand_dict = from_dict(data_class=Candidate, data = results)
        # candidates.append(cand_dict)
        for y in results:
            comm_dict = from_dict(data_class=Committee, data = y)
            committees.append(comm_dict) 
            
    for committee in committees:
            print(committee.affiliated_committee_name)
            print(committee.sponsor_candidate_list)
            insrt = Committees(
        
                    affiliated_committee_name = committee.affiliated_committee_name,
                    candidate_ids = committee.candidate_ids,
                    committee_id = committee.committee_id,
                    committee_type = committee.committee_type,
                    committee_type_full = committee.committee_type_full,
                    cycles = committee.cycles,
                    designation = committee.designation,
                    designation_full = committee.designation_full,
                    filing_frequency = committee.filing_frequency,
                    first_f1_date = committee.first_f1_date,
                    first_file_date = committee.first_file_date,
                    last_f1_date = committee.last_f1_date,
                    last_file_date = committee.last_file_date,
                    name = committee.name,
                    organization_type = committee.organization_type,
                    organization_type_full = committee.organization_type_full,
                    party = committee.party,
                    party_full = committee.party_full,
                    sponsor_candidate_ids = committee.sponsor_candidate_ids,
                    sponsor_candidate_list = committee.sponsor_candidate_list,
                    state = committee.state,
                    treasurer_name = committee.treasurer_name
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