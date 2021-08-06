import json

with open("config.json") as handle:
    config = json.loads(handle.read())

#print(config)

file = '''*** Targets ***

probe = FPing

menu = Top
title = Network Latency Grapher
remark = Welcome to the SmokePing website of xxx Company. \
         Here you will learn all about the latency of our network.


'''

for target,targets in config['targets'].items():
    file += '''+ '''+target+'''
menu = '''+target+'''
title = '''+target+'''
    '''
    for destination,data in targets.items():
        file += '''
++ '''+destination+'''

menu = '''+data['title']+'''
title = '''+data['title']+'''
host = '''+data['target']+'''

'''

file += '''+ Remote
menu = Remote
title = Remote

'''

for remote,data in config['remotes'].items():
    file += '''++ '''+remote+'''
menu = '''+data['title']+'''
title = '''+data['title']+'''

'''
    for target,targets in config['targets'].items():
        file += '''+++ '''+target+'''
menu = '''+target+'''
title = '''+target+'''

'''
        for destination,details in targets.items():
            file += '''++++ '''+destination+'''

menu = '''+details['title']+'''
title = '''+details['title']+'''
probe = '''+data['probe']+'''
host = '''+details['target']+'''

'''

with open("Targets", 'w') as out:
    out.write(file)
