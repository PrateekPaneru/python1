teamname=input("enter your team(shortform): ")

p="points"
r="ranking"
o="overall stats"
name=input(f'''what stat you want to know about
    type       
    {p} = points
    {r} = ranking
    {o} = overall stats\n''')


class IPL:
    teams=["RCB" ,"CSK" , "MI","LSG","KKR","SRH","RR","KX1P","GT","DC" , "rcb" ,"csk" , "mi","lsg","kkr","srh","rr","kxip","gt","dc"]
    class rr:
        points= "12"
        ranking="1"
        overall_stats= "won-7 , lost-1 , points-12 , rank-1"
    class srh:
        points= "10"
        ranking="2"
        overall_stats= "won-5 , lost-2 , points-10 , rank-2"
    class kkr:
        points= "8"
        ranking="3"
        overall_stats= "won-4 , lost-2 , points-8 , rank-3"
    class csk:
        points= "12"
        ranking="4"
        overall_stats= "won-4 , lost-3 , points-8 , rank-4"
    class lsg:
        points= "8"
        ranking="5"
        overall_stats= "won-4 , lost-3 , points-8 , rank-5"
    class mi:
        points= "6"
        ranking="6"
        overall_stats= "won-3 , lost-4 , points-6 , rank-6"
    class dc:
        points= "6"
        ranking="7"
        overall_stats= "won-3, lost-5 , points-6 , rank-7"
    class gt:
        points= "6"
        ranking="8"
        overall_stats= "won-3 , lost-4 , points-6 , rank-8"
    class kxip:
        points= "4"
        ranking="9"
        overall_stats= "won-2, lost-5 , points-4 , rank-9"
    class rcb:
        points= "2"
        ranking="10"
        overall_stats= "won-1 , lost-6 , points-2 , rank-10"

    if(teamname == "rr"):
        if(name=="points"):
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {rr.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {rr.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {rr.overall_stats}")
    if(teamname == "srh"):
        if(name=="points"):
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {srh.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {srh.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {srh.overall_stats}")            
    if(teamname == "kkr"):
        if(name=="points"):    
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {kkr.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {kkr.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {kkr.overall_stats}")            
    if(teamname == "csk"):
        if(name=="points"):    
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {csk.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {csk.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {csk.overall_stats}")  
    if(teamname == "lsg"):
        if(name=="points"):    
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {lsg.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {lsg.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {lsg.overall_stats}")            
    if(teamname == "mi"):
        if(name=="points"):
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {mi.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {mi.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {mi.overall_stats}")              
    if(teamname == "gt"):
        if(name=="points"):    
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {gt.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {gt.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {gt.overall_stats}")   
    if(teamname == "dc"):
        if(name=="points"):   
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {dc.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {dc.ranking}")
        elif(name== "overall stats"):
              print(f"your team {teamname} {o}: {dc.overall_stats}")   
    if(teamname == "kxip"):
        if(name=="points"):
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {kxip.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {kxip.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {kxip.overall_stats}")   
    if(teamname == "rcb"):
        if(name=="points"):
            print("PLEASE WAIT , YOUR POINTS ARE LOADING......")
            print(f"your team {teamname} {p}: {rcb.points}")
        elif(name=="ranking"):
            print("PLEASE WAIT , YOUR rankings ARE LOADING......")
            print(f"your team {teamname} {p}: {rcb.ranking}")
        elif(name=="overall stats"):
              print(f"your team {teamname} {o}: {rcb.overall_stats}")   
            
    if():   
        try:
            teamname!= teams
            name!= ["points" , "ranking" , "overall stats"]
        except Exception as e:
            print(e)
m=IPL()
