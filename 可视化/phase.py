import json

threshold = 20
nodes_count = 50

weigh = [[0 for i in range(nodes_count)] for j in range(nodes_count)]

def get_sim(user_list):
    for i in range(nodes_count):
        for j in range(nodes_count):
            weigh[i][j]=abs(user_list[i]['league']['vs']-user_list[j]['league']['vs'])

if __name__ == '__main__':
    path = "alluser_tetr"
    dict_raw = json.load(open(path,'r',encoding='utf-8'))
    user_list = dict_raw['data']['users']
    #32024 nodes
    get_sim(user_list)
    #output graph
    with open("tetr.txt","wt",encoding='utf-8') as f:
        for i in range(nodes_count):
            for j in range(nodes_count):
                if weigh[i][j]<threshold :
                    print(i,j,file=f)


