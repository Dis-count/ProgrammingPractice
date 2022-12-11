# 考虑多段运输过程的海外仓选址优化问题：优化模型及其编程求解

import numpy as np
import matplotlib.pyplot as plt
from gurobipy import *
import math
import networkx as nx

np.random.seed(520)

class DataGet():
    def __init__(self):
        # 距离就代表费用 1 unit cost per km
        # i:国内商家  g:国内港口  l:国外港口  k:国外仓库  j：国外顾客
        # parameters
        self.num_i = 5
        self.num_g = 5
        self.num_l = 5
        self.num_k = 10 
        self.num_j = 30
        self.fixed_cost = np.random.randint(1e5, 1e7, self.num_k)  #仓库固定成本
        self.q_ij = np.random.randint(1000,10000,self.num_i*self.num_j).reshape(self.num_i,self.num_j) #ij需求
        self.alpha = 0.5  #规模折扣系数
        self.beta = 0.8 #规模折扣系数
        self.expect_num_k = 5  #期望的海外仓库个数
    
    def generate_loc(self,num,x_value_range,y_value=500):
        '''
        @Description: 生成坐标
        @parameters num : 点的个数 , int
                    x_value_range: 横坐标取值范围 , list
                    y_value : 纵坐标最大值 , int
        @return location ：坐标 
        '''
        x_loc = np.random.randint(x_value_range[0],x_value_range[1],num)
        y_loc = np.random.randint(0,y_value,num)  # range: [0,y_value]
        locaiton = np.vstack((x_loc,y_loc)).T
        return locaiton


    def get_euclidean_distance_matrix(self,locationA,locationB):
        """Creates callback to return distance between locations."""
        distances = {}
        for from_counter, from_node in enumerate(locationA):
            distances[from_counter] = {}
            for to_counter, to_node in enumerate(locationB):
                    # Euclidean distance
                    distances[from_counter][to_counter] = (                        
                    math.hypot((from_node[0] - to_node[0]),
                                (from_node[1] - to_node[1])))
        return distances

    def generate_node(self):
        # location generate 
        self.i_loc = self.generate_loc(num=self.num_i,x_value_range=[0,100])
        self.g_loc = self.generate_loc(num=self.num_g,x_value_range=[200,300])
        self.l_loc = self.generate_loc(num=self.num_l,x_value_range=[400,600])
        self.k_loc = self.generate_loc(num=self.num_k,x_value_range=[700,800])
        self.j_loc = self.generate_loc(num=self.num_j,x_value_range=[900,1000])
        # matrix distance generate 
        self.c_ig = self.get_euclidean_distance_matrix(self.i_loc,self.g_loc)
        self.c_gl = self.get_euclidean_distance_matrix(self.g_loc,self.l_loc)
        self.c_lk = self.get_euclidean_distance_matrix(self.l_loc,self.k_loc)
        self.c_kj = self.get_euclidean_distance_matrix(self.k_loc,self.j_loc)

    def solver_gp(self):
        model = Model('YUjINYan')
        #定义决策变量
        x_iglkj = {}
        z_k = {}
        z_kj ={}
        for i in range(self.num_i):
            for g in range(self.num_g):
                for l in range(self.num_l):
                    for k in range(self.num_k):
                        for j in range(self.num_j):
                            name = 'x_' + str(i)+str(g) +str(l) +str(k) +str(j) 
                            x_iglkj[i,g,l,k,j] = model.addVar(0,1, vtype= GRB.BINARY,name= name)
        for k in range(self.num_k):
            name = 'z_'+str(k)
            z_k[k] = model.addVar(0,1, vtype= GRB.BINARY,name= name)
        for k in range(self.num_k):
            for j in range(self.num_j):
                name = 'z_'+str(k)+str(j)
                z_kj[k,j] = model.addVar(0,1, vtype= GRB.BINARY,name= name)
        model.update()
        #定义目标函数
        obj1 = LinExpr(0)
        obj2 = LinExpr(0)
        for i in range(self.num_i):
            for g in range(self.num_g):
                for l in range(self.num_l):
                    for k in range(self.num_k):
                        for j in range(self.num_j):
                            obj1.addTerms(self.q_ij[i,j]*(self.c_ig[i][g]+self.alpha*self.c_gl[g][l]+ self.beta*self.c_lk[l][k]+self.c_kj[k][j]),x_iglkj[i,g,l,k,j])
        for k in range(self.num_k):
            obj2.addTerms(self.fixed_cost[k],z_k[k])
        model.setObjective(obj1+obj2, GRB.MINIMIZE)

        # s.t 1 每个货物只经过一次国内港口、国外港口、仓库
        lhs = LinExpr(0)
        for i in range(self.num_i):
            for j in range(self.num_j):
                for g in range(self.num_g):
                    for l in range(self.num_l):
                        for k in range(self.num_k):
                            lhs.addTerms(1, x_iglkj[i,g,l,k,j])
                model.addConstr(lhs == 1, name= 'visit harbour once'+str(i)+str(g)+str(l)+str(k)+str(j))
                lhs.clear()

        # s.t 2 如果客户j由k负责，则i到j一定经过k
        lhs = LinExpr(0)
        for i in range(self.num_i):
            for j in range(self.num_j):
                for k in range(self.num_k):  
                    for g in range(self.num_g):
                        for l in range(self.num_l):
                            lhs.addTerms(1, x_iglkj[i,g,l,k,j])
                    model.addConstr(lhs <= z_kj[k,j], name= 'k warehouse decision'+str(i)+str(g)+str(l)+str(k)+str(j))
                    lhs.clear()

        # s.t 3 每个客户只有一个仓库负责配送,一个j对应一个k
        lhs = LinExpr(0)
        for j in range(self.num_j):
            for k in range(self.num_k):
                lhs.addTerms(1, z_kj[k,j])
            model.addConstr(lhs == 1, name= 'one warehouse for one custumer'+str(k)+str(j))
            lhs.clear()

        # s.t 4 配送需要的仓库小于等于选定的仓库
        lhs = LinExpr(0)
        for k in range(self.num_k):
            for j in range(self.num_j):
                lhs.addTerms(1, z_kj[k,j])
                model.addConstr(lhs <= z_k[k], name= 'warehouse limitation'+str(k)+str(j))
                lhs.clear()

        # s.t 5 期望的海外仓库数量
        lhs = LinExpr(0)
        for k in range(self.num_k):
            lhs.addTerms(1, z_k[k])
        model.addConstr(lhs == self.expect_num_k, name= 'the number of warehouse'+str(k))
            
        model.setParam("OutputFlag", 1) #是否输出信息，1输出，0关闭
        model.optimize()

        return model


    def get_route(self,model):
        route,z_set = [],[]
        if model.Status==2:
            for item in model.getVars():  # self.model.getVars()[i]. 
                if item.x == 1 and item.varname[0]=='x':
                    route_=[]
                    for n,temp_name in enumerate(item.varname[2::]):
                        if n < 4:
                            route_.append(temp_name)
                        else:
                            route_.append(item.varname[6::])
                            break
                    route.append(route_)
                elif item.x == 1 and item.varname[0]=='z' and len(item.varname)<4:
                    z_set.append(item.varname)
        else:
            print('no solution!!!')
        return route,z_set


    def plot_route(self,route):
        Graph = nx.DiGraph()
        node_name = ['i_','g_','l_','k_','j_']
        node_num = [self.num_i,self.num_g,self.num_l,self.num_k,self.num_j]
        locs = [self.i_loc,self.g_loc,self.l_loc,self.k_loc,self.j_loc]
        color_dict = ['r','y','g','b','pink']
        pos_location={}
        nodes_color_dict=[]
        for n,name in enumerate(node_name):
            nodes_name_temp = [name+str(_) for _ in range(node_num[n])]
            Graph.add_nodes_from(nodes_name_temp)
            nodes_color_dict += [color_dict[n] for _ in range(node_num[n])]
            for i,loc in enumerate(locs[n]):
                pos_location[nodes_name_temp[i]] = loc 
            
        edges = []
        for r in route :
            edge = [] 
            for cnt,n_r in enumerate(r):
                r_temp = node_name[cnt] + n_r
                edge.append(r_temp)
                if len(edge) == 2 :
                    edges.append(tuple(edge))
                    edge.pop(0)
        Graph.add_edges_from(edges)
        nx.draw_networkx(Graph,pos_location,node_size=300,node_color=nodes_color_dict,labels=None)  
        plt.show()


if __name__=='__main__':
    data = DataGet()
    data.generate_node()
    solution = data.solver_gp()
    route,z_set = data.get_route(solution)
    data.plot_route(route)
    print('select warehouse : ',z_set)
