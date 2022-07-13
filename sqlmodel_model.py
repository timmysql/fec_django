from sqlmodel import  SQLModel, Field, Column, VARCHAR, DateTime
from typing import Optional, List, Dict
from datetime import date, datetime, time, timedelta
from sqlalchemy import BigInteger, inspect, Integer, String
from rich import inspect
import db_connect as dbc
from sqlmodel import Session, select, or_, ARRAY

# class Test:
#     test1: str

class Candidates(SQLModel, table=True):
    __tablename__ = "candidates"  
    active_through: int
    candidate_id: str = Field(default=None, primary_key=True)
    candidate_inactive: bool
    candidate_status: str
    cycles: List[int] = Field(sa_column=Column(ARRAY(Integer)))
    district: str
    district_number: int
    election_districts: List[str] = Field(sa_column=Column(ARRAY(String)))    
    election_years: List[int] = Field(sa_column=Column(ARRAY(Integer)))
    federal_funds_flag: bool
    first_file_date: Optional[str] = Field(default=None) 
    flags: str
    has_raised_funds: bool
    inactive_election_years: List[int] = Field(sa_column=Column(ARRAY(Integer)))
    incumbent_challenge: Optional[str]
    incumbent_challenge_full: Optional[str]
    last_f2_date: Optional[str] = Field(default=None) 
    last_file_date: Optional[str] = Field(default=None) 
    load_date: Optional[str] = Field(default=None) 
    name: str
    office:str
    office_full: str
    party: str
    party_full: str
    state: str  
    
    class Config:
        arbitrary_types_allowed = True

class Committees(SQLModel, table=True):
    __tablename__ = "committees"  
    affiliated_committee_name: Optional[str] = Field(default=None) 
    candidate_ids: List[str]
    committee_id: str = Field(default=None, primary_key=True)
    committee_type: str
    committee_type_full: str
    cycles: List[int] = Field(sa_column=Column(ARRAY(String)))
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
    party: Optional[str] = Field(default=None) 
    party_full: Optional[str] = Field(default=None) 
    sponsor_candidate_ids: Optional[List[str]] = Field(sa_column=Column(ARRAY(String)))    
    sponsor_candidate_list: Optional[List[str]] = Field(sa_column=Column(ARRAY(String)))   
    # sponsor_candidate_list: List[Dict[str, str]] = Field(sa_column=Column(ARRAY(String)))  
    state: str
    treasurer_name: Optional[str]
    
    
    
class CalendarDates(SQLModel, table=True):
    __tablename__ = "dates_calendar"  
    all_day: bool
    calendar_category_id: int
    category: str
    description: Optional[str]
    end_date: Optional[str]
    event_id: int
    location: Optional[str]
    start_date: str = Field(default=None, primary_key=True)
    state: Optional[str]
    summary: str
    url: Optional[str]    
    
    
class ElectionDates(SQLModel, table=True):
    __tablename__ = "dates_election"  
    create_date: str
    election_date: str = Field(default=None, primary_key=True)
    election_notes: Optional[str]
    election_party: Optional[str]
    election_state: Optional[str]
    election_type_full: Optional[str]
    election_type_id: Optional[str]
    election_year: int
    office_sought: Optional[str]
    primary_general_date: Optional[str]
    update_date: Optional[str]  
    
    
class ReportingDates(SQLModel, table=True):
    __tablename__ = "dates_reporting" 
    create_date: str
    due_date: str = Field(default=None, primary_key=True)
    report_type: str
    report_type_full: Optional[str]
    report_year: int
    update_date: str         


class States(SQLModel, table=True):
    __tablename__ = "states"            
        
    state_abbr: Optional[str] = Field(default=None, primary_key=True) 
    state_name: str = None
    last_facilities_list_process_dt: datetime = None 
    last_facilities_detail_process_dt: datetime = None
    last_file_process_dt: datetime = None 
    last_file_changes_process_dt: datetime = None
    last_file_changes_post_process_dt: datetime = None
    last_pdf_process_dt: datetime = None
    last_image_process_dt: datetime = None
    last_post_process_dt: datetime = None
    

engine = dbc.get_postgres_config() 

SQLModel.metadata.create_all(engine)  