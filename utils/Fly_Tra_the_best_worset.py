'''
Karobben
Chain behaviors detect
'''

import pandas as pd
import numpy as np
import math

class fly_align():

    def dist_f(self, F1, F2):
        F1 = list(F1)
        F2 = list(F2)
        Dist = math.sqrt((F1[0]-F2[0])**2 + (F1[1]- F2[1])**2)
        return Dist

    def TB_dic(self, TB, frame):
        TB[0] = pd.to_numeric(TB[0])
        TB[1] = pd.to_numeric(TB[1])
        TB[2] = pd.to_numeric(TB[2])
        TB[3] = pd.to_numeric(TB[3])
        TB[4] = pd.to_numeric(TB[4])
        fly_bodies = TB[TB[0]==0]
        fly_bodies = fly_bodies.sort_values(by=[1,2,3,4])
        fly_head   = TB[TB[0]==1]
        fly_chasing   = TB[TB[0]==3]
        fly_sing   = TB[TB[0]==4]
        fly_mating   = TB[TB[0]==5]
        FLY_matrix = {frame:{"fly_"+str(i):{"body":list(fly_bodies.iloc[i,1:])} for i in range(len(fly_bodies))}}
        return FLY_matrix

    def nearst_match(self, id_new, FLY_1, OLD_LIST, FLY_matrix, frame, Threads, MATCH=100000):
        try:
            for id_old in OLD_LIST:
                FLY_2 = FLY_matrix[frame-1][id_old]["body"]
                DIST = self.dist_f(FLY_1, FLY_2)
                if DIST == 0:
                    MATCH = DIST
                    print("Nearst match result:", id_new, id_old, DIST)
                    Fly_list.remove(id_old)
                    return {id_new:id_old}
                elif DIST < MATCH:
                    MATCH = DIST
                    match_id = id_old
            print("Nearst match result:", id_new, match_id, MATCH)
            return {id_new: match_id}
        except:
            print("din't match, value lost")
            return {}

    def align(self, FLY_matrix, FLY_matrix_tpm, frame, Threads= 100000):
        Lost_list = False
        MATCH_result = {}
        OLD_LIST = list(FLY_matrix[frame-1].keys())
        for id_new in list(FLY_matrix_tpm[frame].keys()):
            FLY_1 = FLY_matrix_tpm[frame][id_new]["body"]
            Dic_tmp = self.nearst_match(id_new, FLY_1, OLD_LIST, FLY_matrix, frame, Threads)
            MATCH_result.update(Dic_tmp)
            print("Dic_tmp", Dic_tmp.values() )
            try:
                OLD_LIST.remove(list(Dic_tmp.values())[0])
            except:
                OLD_LIST
        '''
        Check the duplication of the result
        '''
        print("let's check the duplicates",MATCH_result)
        if len(set(MATCH_result.keys())) == len(FLY_matrix[frame-1]):
            print("No duplicate, run next")
            return MATCH_result, Lost_list

        '''
        remove dupication
        '''
        ## When the result has duplicate and only one duplicate
        ## MATCH_result.keys = id_new
        ## MMATCH_result.values = id_old
        if (len(MATCH_result.values()) != len(set(MATCH_result.values()))) :
            print("\n\nwe here\n\n")
            AA = list(MATCH_result.values())
            ## Find the duplicate
            [AA.remove(i) for i in list(set(MATCH_result.values()))]
            print("The duplicate is:", AA)
            ## Find the index of the duplicate
            for duplicate_id in list(set(AA)):
                INDEX = [i for i, x in enumerate(MATCH_result.values()) if x == duplicate_id]
                print("Index of the duplicate:", INDEX, "for", duplicate_id)

                ## caculate the nearset duplicate
                Compare_dic = {}
                for i in INDEX:
                    new_id=list(MATCH_result.keys())[i]
                    AA = self.dist_f(FLY_matrix_tpm[frame][new_id]["body"], FLY_matrix[frame-1][MATCH_result[new_id]]["body"])
                    Compare_dic.update({i:AA})
                print(Compare_dic)

                most_ID = 1
                for i in range(len(Compare_dic.keys()) -1):
                    ID_1 = list(Compare_dic.keys())[i]
                    ID_2 = list(Compare_dic.keys())[i+1]
                    if Compare_dic[ID_1] < Compare_dic[ID_2] and Compare_dic[ID_1] < most_ID:
                        most_ID = ID_1
                    elif Compare_dic[ID_2] < Compare_dic[ID_1] and Compare_dic[ID_1] < most_ID:
                        most_ID = ID_2
                print("most_ID", most_ID)
                # keep the nearst point
                INDEX.remove(most_ID)
                #print(INDEX)

                for i in [list(MATCH_result.keys())[i] for i in INDEX]:
                    MATCH_result.pop(i)
                print("cleared result", MATCH_result)
                #print("No duplicate result", MATCH_result)
            if len(MATCH_result)==len(FLY_matrix[frame-1]):
                print("We good")
                return MATCH_result, Lost_list

            #print(len(FLY_matrix_tpm[frame].keys()), len(FLY_matrix[frame-1].keys()))
            if len(FLY_matrix_tpm[frame].keys()) < len(FLY_matrix[frame-1].keys()):
                print("target lost")
                print("why not", MATCH_result)
        '''
        Check the number of the target
        '''
        if len(FLY_matrix[frame-1]) == len(MATCH_result):
            print("we good, at here")
            return MATCH_result, Lost_list
        else:
            '''
            find the lost one
            '''
            Fly_list = list(FLY_matrix[frame-1].keys())

            for i in list(set(MATCH_result.values())):
                try:
                    Fly_list.remove(i)
                except:
                    Fly_list
            print("we lost:", Fly_list)
            '''
            try match the nearst for it/them
            '''
            if len(FLY_matrix[frame-1]) > len(FLY_matrix_tpm[frame]):
                Lost_list = {}
                for id_old in Fly_list:
                    FLY_old_lost = FLY_matrix[frame-1][id_old]["body"]
                    Dic_tmp = self.nearst_match(id_old, FLY_old_lost, OLD_LIST, FLY_matrix_tpm, frame+1, Threads)
                    #print(Dic_tmp)
                    Lost_list.update(Dic_tmp)
                Lost_list = {v: k for k, v in Lost_list.items()}
                print(Lost_list)
                if len(Lost_list) != 0:
                    MATCH_result.update(Lost_list)

            print("\n\nLost_list\n\n", Lost_list)
            print("\n\MATCH_result\n\n", MATCH_result)
            return MATCH_result, Lost_list

        #print(len(fly_bodies))


        #FLY_matrix
