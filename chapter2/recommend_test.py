import recommendations as recommend

print recommend.critics['Toby']

print recommend.sim_distance(recommend.critics, 'Lisa Rose' ,'Gene Seymour')

print recommend.sim_distance(recommend.critics, 'Lisa Rose' ,'Michael Phillips')

print recommend.sim_distance(recommend.critics, 'Lisa Rose' ,'Claudia Puig')

print recommend.sim_distance(recommend.critics, 'Lisa Rose' ,'Mick LaSalle')

print recommend.sim_distance(recommend.critics, 'Lisa Rose' ,'Jack Matthews')

print recommend.sim_distance(recommend.critics, 'Lisa Rose' ,'Toby')