import db_connect as dbc
import requests
import json
from dataclasses import dataclass, field, MISSING
# from typing import List
from typing import Optional, List, Union
from datetime import date, datetime
from dacite import from_dict
# from sqlmodel_model import Committees
from sqlmodel import Session, select, or_
import db_connect as dbc
from sqlalchemy.exc import IntegrityError
from rich import inspect

import pprint



engine = dbc.get_postgres_config()

FEC_API_KEY = "vtR7iSAdFdWJO8kvCNG13ihOP9vIyMnGpheD4LdX"


url = f"https://api.open.fec.gov/v1/committees/?state=NE&sort_nulls_last=false&sort=name&api_key={FEC_API_KEY}&sort_null_only=false&page=1&per_page=20&sort_hide_null=false"
url = f"https://api.open.fec.gov/v1/committees/"


@dataclass
class Committee:
    affiliated_committee_name: Optional[str] = field(default=None, init=False) 
    candidate_ids: List[str]
    committee_id: str
    committee_type: str
    committee_type_full: str
    cycles: List[int]
    designation: str
    designation_full: str
    filing_frequency: str
    first_f1_date: str
    first_file_date: str
    last_f1_date: str
    last_file_date: str
    name: str
    organization_type: Optional[str]
    organization_type_full: Optional[str]
    party: Optional[str] = field(default=None, init=False) 
    party_full: Optional[str] = field(default=None, init=False) 
    sponsor_candidate_ids: Optional[List[str]] = field(default=None, init=False) 
    sponsor_candidate_list: List[str]
    state: str
    treasurer_name: str



# def get_request_pages():
#     first_page = session.get(url).json()
#     yield first_page
#     num_pages = first_page['last_page']

#     for page in range(2, num_pages + 1):
#         next_page = session.get(url, params={'page': page}).json()
#         yield next_page

# for page in get_jobs():
    # TODO: process the page

def get_request(page, per_page, state):
    session = requests.Session() 
    r = session.get(url, params={'page': page, 'state': state, 'api_key': FEC_API_KEY, 'sort_null_only': False, 'per_page': per_page, 'sort_hide_null': False }).json()
    return r

def get_request_params():
    page = 1 
    session = requests.Session() 
    # r = session.get(url, params={'page': page, 'state': 'NE', 'api_key': FEC_API_KEY, 'sort_null_only': False, 'per_page': 20, 'sort_hide_null': False }).json()
    r = get_request(page=1, state='NE')
    pages = r["pagination"]["pages"]
    results = r["results"]
    # yield results
    for page in range(2, pages + 1):
        pr = get_request(page, state='NE')
        # pprint.pprint(pr)
        results = pr["results"]
        pprint.pprint(results)
        # yield results
        # input('stop')
    # pprint.pprint(r)


def get_request_data():      
    search_get = url
    r = requests.get(search_get)                
    data = r.json() 
    dump = json.dumps(data.get("results"))
    load = json.loads(dump)
    return load


def get_request_pages():      
    search_get = url
    r = requests.get(search_get)                
    data = r.json() 
    dump = json.dumps(data.get("pagination"))
    load = json.loads(dump)
    print(load["page"])
    print(load["pages"])
    # pprint.pprint(load)
    # return load
    
    
# def get_request_data(): 
#     session = requests.Session()   
#     search_get = url
#     r = requests.get(search_get)                
#     data = r.json() 
#     # pprint.pprint(data)
#     page = session.get(url).get("pagination").json()
#     yield page
#     pages = page['pages']
#     print(page)
#     print(pages)
#     dump = json.dumps(data.get("results"))
#     # load = json.loads(dump)
#     # return load    
    

def main():
    # get_request_data()
    data = get_request_data()
    # inspect(data)
            
    committees = []
    for y in data:
        # inspect(y)
        # pprint.pprint(y)
        # input("stop")
        comm_dict = from_dict(data_class=Committee, data = y)
        committees.append(comm_dict)       
        
    for committee in committees:
        print(committee.name)
    #     insrt = Candidates(
    
    #         active_through = candidate.active_through,
    #         candidate_id = candidate.candidate_id,
    #         candidate_inactive = candidate.candidate_inactive,
    #         candidate_status = candidate.candidate_status,
    #         cycles = candidate.cycles,
    #         district = candidate.district,
    #         district_number = candidate.district_number,
    #         election_districts = candidate.election_districts,
    #         election_years = candidate.election_years,
    #         federal_funds_flag = candidate.federal_funds_flag,
    #         first_file_date = candidate.first_file_date,
    #         flags = candidate.flags,
    #         has_raised_funds = candidate.has_raised_funds,
    #         inactive_election_years = candidate.inactive_election_years,
    #         incumbent_challenge = candidate.incumbent_challenge,
    #         incumbent_challenge_full = candidate.incumbent_challenge_full,
    #         last_f2_date = candidate.last_f2_date,
    #         last_file_date = candidate.last_file_date,
    #         load_date = candidate.load_date,
    #         name = candidate.name,
    #         office = candidate.office,
    #         office_full = candidate.office_full,
    #         party = candidate.party,
    #         party_full = candidate.party_full,
    #         state = candidate.state
    #     )
    #     try:
    #         with Session(engine) as session:
    #             session.add(insrt)    
    #             session.commit()
    #             session.close() 
    #     except IntegrityError as ie:
    #         pass
    


if __name__ == "__main__":
    # get_request_data()
    # get_request_pages()
    get_request_params()