from sqlmodel_model import States
from sqlmodel import Session, select, or_
import db_connect as dbc


engine = dbc.get_postgres_config()  

# class InsertFileChanges:
#     def __init__(self, dc_files, facility_id):
#         self.dc_files = dc_files
#         self.facility_id = facility_id
    
#     def insert(self):
#         dc = self.dc_files
#         # print(dc.file_id)
#         ic = FileChanges(
#                 file_id = dc.file_id,
#                 file_name = dc.file_name,
#                 file_extension = dc.file_extension,
#                 file_size = dc.file_size,
#                 history_status = dc.history_status,
#                 folder_id = dc.folder_id,
#                 file_manager_id = dc.file_manager_id,
#                 entity_id = dc.entity_id,
#                 source_service_code = dc.source_service_code,
#                 create_ts = dc.create_ts,
#                 last_update_ts = dc.last_update_ts,
#                 file_status = dc.file_status,
#                 file_folder_path = dc.file_folder_path,
#                 callsign = dc.callsign,
#                 city = dc.city,
#                 state = dc.state,
#                 licensee = dc.licensee,
#                 legalname = dc.legalname,
#                 moved_ts = dc.moved_ts,
#                 moved_from = dc.moved_from
#             )          
#         session = Session(engine)
#         session.add(ic)    
#         session.commit()
#         session.close() 
    
class InsertStates:
    def __init__(self):
        pass
    
    def insert(self):
        ak = States(state_abbr="AK",	state_name="Alaska")
        al = States(state_abbr="AL",	state_name="Alabama")
        ar = States(state_abbr="AR",	state_name="Arkansas")
        sm = States(state_abbr="AS",	state_name="American Samoa")
        az = States(state_abbr="AZ",	state_name="Arizona")
        ca = States(state_abbr="CA",	state_name="California")
        co = States(state_abbr="CO",	state_name="Colorado")
        ct = States(state_abbr="CT",	state_name="Connecticut")
        dc = States(state_abbr="DC",	state_name="District of Columbia")
        de = States(state_abbr="DE",	state_name="Delaware")
        fl = States(state_abbr="FL",	state_name="Florida")
        ga = States(state_abbr="GA",	state_name="Georgia")
        gu = States(state_abbr="GU",	state_name="Guam")
        hi = States(state_abbr="HI",	state_name="Hawaii")
        ia = States(state_abbr="IA",	state_name="Iowa")
        id = States(state_abbr="ID",	state_name="Idaho")
        il = States(state_abbr="IL",	state_name="Illinois")
        ind = States(state_abbr="IN",	state_name="Indiana")
        ks = States(state_abbr="KS",	state_name="Kansas")
        ky = States(state_abbr="KY",	state_name="Kentucky")
        la = States(state_abbr="LA",	state_name="Louisiana")
        ma = States(state_abbr="MA",	state_name="Massachusetts")
        md = States(state_abbr="MD",	state_name="Maryland")
        me = States(state_abbr="ME",	state_name="Maine")
        mi = States(state_abbr="MI",	state_name="Michigan")
        mn = States(state_abbr="MN",	state_name="Minnesota")
        mo = States(state_abbr="MO",	state_name="Missouri")
        mp = States(state_abbr="MP",	state_name="Northern Mariana Islands")
        ms = States(state_abbr="MS",	state_name="Mississippi")
        mt = States(state_abbr="MT",	state_name="Montana")
        nc = States(state_abbr="NC",	state_name="North Carolina")
        nd = States(state_abbr="ND",	state_name="North Dakota")
        ne = States(state_abbr="NE",	state_name="Nebraska")
        nh = States(state_abbr="NH",	state_name="New Hampshire")
        nj = States(state_abbr="NJ",	state_name="New Jersey")
        nm = States(state_abbr="NM",	state_name="New Mexico")
        nv = States(state_abbr="NV",	state_name="Nevada")
        ny = States(state_abbr="NY",	state_name="New York")
        oh = States(state_abbr="OH",	state_name="Ohio")
        ok = States(state_abbr="OK",	state_name="Oklahoma")
        org =States(state_abbr="OR",	state_name="Oregon")
        pa = States(state_abbr="PA",	state_name="Pennsylvania")
        pr = States(state_abbr="PR",	state_name="Puerto Rico")
        ri = States(state_abbr="RI",	state_name="Rhode Island")
        sc = States(state_abbr="SC",	state_name="South Carolina")
        sd = States(state_abbr="SD",	state_name="South Dakota")
        tn = States(state_abbr="TN",	state_name="Tennessee")
        tx = States(state_abbr="TX",	state_name="Texas")
        ut = States(state_abbr="UT",	state_name="Utah")
        va = States(state_abbr="VA",	state_name="Virginia")
        vi = States(state_abbr="VI",	state_name="Virgin Islands")
        vt = States(state_abbr="VT",	state_name="Vermont")
        wa = States(state_abbr="WA",	state_name="Washington")
        wi = States(state_abbr="WI",	state_name="Wisconsin")
        wv = States(state_abbr="WV",	state_name="West Virginia")
        wy = States(state_abbr="WY",	state_name="Wyoming"        )
        session = Session(engine)
        session.add(ak)
        session.add(al)
        session.add(ar)
        session.add(sm)
        session.add(az)
        session.add(ca)
        session.add(co)
        session.add(ct)
        session.add(dc)
        session.add(de)
        session.add(fl)
        session.add(ga)
        session.add(gu)
        session.add(hi)
        session.add(ia)
        session.add(id)
        session.add(il)
        session.add(ind)
        session.add(ks)
        session.add(ky)
        session.add(la)
        session.add(ma)
        session.add(md)
        session.add(me)
        session.add(mi)
        session.add(mn)
        session.add(mo)
        session.add(mp)
        session.add(ms)
        session.add(mt)
        session.add(nc)
        session.add(nd)
        session.add(ne)
        session.add(nh)
        session.add(nj)
        session.add(nm)
        session.add(nv)
        session.add(ny)
        session.add(oh)
        session.add(ok)
        session.add(org)
        session.add(pa)
        session.add(pr)
        session.add(ri)
        session.add(sc)
        session.add(sd)
        session.add(tn)
        session.add(tx)
        session.add(ut)
        session.add(va)
        session.add(vi)
        session.add(vt)
        session.add(wa)
        session.add(wi)
        session.add(wv)
        session.add(wy)
    
        session.commit()
        session.close() 





def insert_states():
    states = select_states()    
    if len(states) == 0:
        x = InsertStates()
        x.insert()
        print("states inserted")
    else:
        print("no need to insert states, they already exist")


def select_states():
    with Session(engine) as session:
        statement = select(States)
        results = session.exec(statement)
        result = results.fetchall()
    return result
        
if __name__ == "__main__": 
    insert_states()
    # states = select_states()
    # print(len(states))
    # for x in states:
    #     print(x)
    # print(len(states))       

# "AK"	"Alaska"
# "AL"	"Alabama"
# "AR"	"Arkansas"
# "AS"	"American Samoa"
# "AZ"	"Arizona"
# "CA"	"California"
# "CO"	"Colorado"
# "CT"	"Connecticut"
# "DC"	"District of Columbia"
# "DE"	"Delaware"
# "FL"	"Florida"
# "GA"	"Georgia"
# "GU"	"Guam"
# "HI"	"Hawaii"
# "IA"	"Iowa"
# "ID"	"Idaho"
# "IL"	"Illinois"
# "IN"	"Indiana"
# "KS"	"Kansas"
# "KY"	"Kentucky"
# "LA"	"Louisiana"
# "MA"	"Massachusetts"
# "MD"	"Maryland"
# "ME"	"Maine"
# "MI"	"Michigan"
# "MN"	"Minnesota"
# "MO"	"Missouri"
# "MP"	"Northern Mariana Islands"
# "MS"	"Mississippi"
# "MT"	"Montana"
# "NC"	"North Carolina"
# "ND"	"North Dakota"
# "NE"	"Nebraska"
# "NH"	"New Hampshire"
# "NJ"	"New Jersey"
# "NM"	"New Mexico"
# "NV"	"Nevada"
# "NY"	"New York"
# "OH"	"Ohio"
# "OK"	"Oklahoma"
# "OR"	"Oregon"
# "PA"	"Pennsylvania"
# "PR"	"Puerto Rico"
# "RI"	"Rhode Island"
# "SC"	"South Carolina"
# "SD"	"South Dakota"
# "TN"	"Tennessee"
# "TX"	"Texas"
# "UT"	"Utah"
# "VA"	"Virginia"
# "VI"	"Virgin Islands"
# "VT"	"Vermont"
# "WA"	"Washington"
# "WI"	"Wisconsin"
# "WV"	"West Virginia"
# "WY"	"Wyoming"