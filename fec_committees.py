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

engine = dbc.get_postgres_config()

FEC_API_KEY = "vtR7iSAdFdWJO8kvCNG13ihOP9vIyMnGpheD4LdX"


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
        # insrt = Candidates(
    
        #     active_through = candidate.active_through,
        #     candidate_id = candidate.candidate_id,
        #     candidate_inactive = candidate.candidate_inactive,
        #     candidate_status = candidate.candidate_status,
        #     cycles = candidate.cycles,
        #     district = candidate.district,
        #     district_number = candidate.district_number,
        #     election_districts = candidate.election_districts,
        #     election_years = candidate.election_years,
        #     federal_funds_flag = candidate.federal_funds_flag,
        #     first_file_date = candidate.first_file_date,
        #     flags = candidate.flags,
        #     has_raised_funds = candidate.has_raised_funds,
        #     inactive_election_years = candidate.inactive_election_years,
        #     incumbent_challenge = candidate.incumbent_challenge,
        #     incumbent_challenge_full = candidate.incumbent_challenge_full,
        #     last_f2_date = candidate.last_f2_date,
        #     last_file_date = candidate.last_file_date,
        #     load_date = candidate.load_date,
        #     name = candidate.name,
        #     office = candidate.office,
        #     office_full = candidate.office_full,
        #     party = candidate.party,
        #     party_full = candidate.party_full,
        #     state = candidate.state
        # )
        # try:
        #     with Session(engine) as session:
        #         session.add(insrt)    
        #         session.commit()
        #         session.close() 
        # except IntegrityError as ie:
        #     pass
    
    

if __name__ == "__main__":
    get_request_params()