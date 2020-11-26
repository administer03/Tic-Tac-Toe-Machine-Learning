import random
import csv
from tkinter import *
import tkinter.messagebox
import sys
import os

## error draw condition and X WIN last 
class Ai:
    def __init__(self):
        self.memory = []
        file = open("table_pattern.txt", "r")
        re = file.readlines()
        for i in re:
            x = i.strip('\n')
            b = x.split(',')
            self.memory.append(b)
    def choose_position_before(self,cur_position,state):#cur_position is list,state is int
        #print("before_cur_position")
        #print(state)
        if(len(cur_position) == 0):#first strat
            #print("case 1")
            #print(self.memory)
            if(self.memory == [['']]):#if not have memory
                return random.randint(1, 9)
            min_state = 6
            state_prob = []
            for i in self.memory:
                if(len(i)%2 == 1):
                    state_prob.append(i)
            for i in state_prob:#find method for fast win
                #print(i)
                if(min_state > int(i[-2])):
                    min_state = int(i[-2])
                    
            high_speed_met = []
            for i in self.memory:#select only fast method for win
                if(int(i[-2]) == min_state and len(i)%2 == 1):
                    high_speed_met.append(i)
                    
            high_speed_met_many_use = []
            many_use = 0
            for i in high_speed_met:#find many time to use
                if(many_use < int(i[-1])):
                    many_use = int(i[-1])

            for i in high_speed_met:
                if(int(i[-1]) == many_use):
                    high_speed_met_many_use.append(i)
            #print(high_speed_met_many_use)
            if(high_speed_met_many_use == []):
                not_in_table = {'1','2','3','4','5','6','7','8','9'}
                for i in cur_position:
                    not_in_table.remove(i)
                return int(random.choice(tuple(not_in_table)))
            
            result = random.choice(high_speed_met_many_use)
            return int(result[0])
            #choice = ['1','2','3','4','5','6','7','8','9']
            #return int(random.choice(choice))
        else:
            #print("case 2")
            state_prob = []
            if(self.memory == [['']]):#if not have memory
                not_in_table = {'1','2','3','4','5','6','7','8','9'}
                for i in cur_position:
                    not_in_table.remove(i)
                return int(random.choice(tuple(not_in_table)))
            #print(self.memory)
            for i in self.memory:#find prop answer and first start
                if(state <= int(i[-2]) and len(i)%2 == 1):
                    state_prob.append(i)
            #print(state_prob)
            state_k_prob = []
            for i in state_prob:#select only curposition match
                check_before_state = False
                count_cur_posi = len(cur_position)
                for j in range(len(cur_position)):#check state before
                    if(i[j] != cur_position[j]):
                        break
                    if(count_cur_posi == 1):
                        check_before_state = True
                    count_cur_posi -= 1
                if(check_before_state):  
                    state_k_prob.append(i)
            #print(state_k_prob)
            
            min_state = 6
            for i in state_k_prob:
                if(min_state > int(i[-2])):#find method for fast win
                    min_state = int(i[-2])
            high_speed_met = []
            for i in state_k_prob:
                if(int(i[-2]) == min_state):#select only fast method for win
                    high_speed_met.append(i)

            high_speed_met_many_use = []
            many_use = 0
            for i in high_speed_met:#find many time to use
                if(many_use < int(i[-1])):
                    many_use = int(i[-1])

            for i in high_speed_met:
                if(int(i[-1]) == many_use):
                    high_speed_met_many_use.append(i)
                    
            #print(high_speed_met_many_use)
            if(high_speed_met_many_use == []):#case not have match
                not_in_table = {'1','2','3','4','5','6','7','8','9'}
                for i in cur_position:
                    not_in_table.remove(i)
                return int(random.choice(tuple(not_in_table)))
            result = random.choice(high_speed_met_many_use)
            #print(result)
            while(True):
                if(result[(state-1)*2] in cur_position):
                    result = random.choice(high_speed_met_many_use)
                else:
                    return int(result[(state-1)*2])
        
    def choose_position_after(self,cur_position,state):
        #print("after_cur_position")
        #print(state)
        state_prob = []
        if(self.memory == [['']]):#if not have memory
            #print("case 1")
            not_in_table = {'1','2','3','4','5','6','7','8','9'}
            for i in cur_position:
                not_in_table.remove(i)
            return int(random.choice(tuple(not_in_table)))
        #print(self.memory)
        for i in self.memory:#find prop answer and first start
            if(state <= int(i[-2]) and len(i)%2 == 0):
                state_prob.append(i)
        #print(state_prob)
        if(state_prob != []):
            #print("case 1.1")
            state_k_prob = []
            for i in state_prob:#select only curposition match
                check_before_state = False
                count_cur_posi = len(cur_position)
                for j in range(len(cur_position)):#check state before
                    if(i[j] != cur_position[j]):
                        break
                    if(count_cur_posi == 1):
                        check_before_state = True
                    count_cur_posi -= 1
                if(check_before_state):  
                    state_k_prob.append(i)
            #print(state_k_prob)
                
            min_state = 6
            for i in state_k_prob:
                if(min_state > int(i[-2])):#find method for fast win
                    min_state = int(i[-2])
            high_speed_met = []
            for i in state_k_prob:
                if(int(i[-2]) == min_state):#select only fast method for win
                    high_speed_met.append(i)

            high_speed_met_many_use = []
            many_use = 0
            for i in high_speed_met:#find many time to use
                if(many_use < int(i[-1])):
                    many_use = int(i[-1])
            for i in high_speed_met:
                if(int(i[-1]) == many_use):
                    high_speed_met_many_use.append(i)
            #print(high_speed_met_many_use)
            if(high_speed_met_many_use == []):#case not have match
                not_in_table = {'1','2','3','4','5','6','7','8','9'}
                for i in cur_position:
                    not_in_table.remove(i)
                return int(random.choice(tuple(not_in_table)))
            result = random.choice(high_speed_met_many_use)
            while(True):
                #print(result[(state*2)-1])
                if(result[(state*2)-1] in cur_position):
                    result = random.choice(high_speed_met_many_use)
                else:
                    return int(result[(state*2)-1])
        else:
            #print("case 1.2")
            if(self.memory == [['']]):#if not have memory
                not_in_table = {'1','2','3','4','5','6','7','8','9'}
                for i in cur_position:
                    not_in_table.remove(i)
                return int(random.choice(tuple(not_in_table)))
            for i in self.memory:#find prop answer and first start
                if(state <= int(i[-2]) and len(i)%2 == 1):
                    state_prob.append(i)
            #print(state_prob)
            state_k_prob = []
            for i in state_prob:#select only curposition match
                check_before_state = False
                count_cur_posi = len(cur_position)
                for j in range(len(cur_position)):#check state before
                    if(i[j] != cur_position[j]):
                        break
                    if(count_cur_posi == 1):
                        check_before_state = True
                    count_cur_posi -= 1
                if(check_before_state):  
                    state_k_prob.append(i)
            #print(state_k_prob)
            min_state = 6
            for i in state_k_prob:
                if(min_state > int(i[-2])):#find method for fast win
                    min_state = int(i[-2])
            high_speed_met = []
            for i in state_k_prob:
                if(int(i[-2]) == min_state):#select only fast method for win
                    high_speed_met.append(i)

            high_speed_met_many_use = []
            many_use = 0
            for i in high_speed_met:#find many time to use
                if(many_use < int(i[-1])):
                    many_use = int(i[-1])

            for i in high_speed_met:
                if(int(i[-1]) == many_use):
                    high_speed_met_many_use.append(i)
                    
            #print(high_speed_met_many_use)
            if(high_speed_met_many_use == []):#case not have match
                not_in_table = {'1','2','3','4','5','6','7','8','9'}
                for i in cur_position:
                    not_in_table.remove(i)
                return int(random.choice(tuple(not_in_table)))
            result = random.choice(high_speed_met_many_use)
            #print(result)
            while(True):
                #print(result[(state*2)-1])
                if(result[(state*2)-1] in cur_position):
                    result = random.choice(high_speed_met_many_use)
                else:
                    return int(result[(state*2)-1])
                
    def choose_naive_bayes_before(self,cur_position,state):
        if(len(cur_position) == 0):#first strat
            #print("case 1")
            #print(self.memory)
            if(self.memory == [['']]):#if not have memory
                print("random answer")
                return random.randint(1, 9)
            prob_result = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            count_memory = len(self.memory)
            
            state_k_prob = []
            for i in self.memory:
                if(len(i)%2 == 1):
                    state_k_prob.append(i)
            
            if(state_k_prob == []):
                #print('case')
                state_l_prob = []
                for i in self.memory:
                    if(len(i)%2 == 0):
                        state_l_prob.append(i)
                if(state_l_prob == []):#not have every thing
                    print("random answer")
                    return random.randint(1, 9)
                print("avoidance lose: ",state_l_prob)
                for i in prob_result:#fin min use and lose
                    count_posi_lose = 0
                    for j in state_l_prob:
                        if(j[0] == i):
                            count_posi_lose += 1
                    prob_posi = count_posi_lose/count_memory
                    prob_result[i] += prob_posi
                min_prob = 1
                for i in prob_result:#find min prob
                    if(prob_result[i] < min_prob):
                        min_prob = prob_result[i]
                list_result = []
                for i in prob_result:
                    if(prob_result[i] == min_prob):
                        list_result.append(i)
                #print(list_result)
                result = random.choice(list_result)
                return int(result)

            for i in prob_result:#find high use and win
                count_posi_win = 0
                for j in state_k_prob:
                    if(j[0] == i and len(j)%2 == 1):
                        count_posi_win += 1
                prob_posi = count_posi_win/count_memory
                prob_result[i] += prob_posi
            #print(prob_result)
                
            print("In memory win: ",state_k_prob)
            max_prob = 0
            for i in prob_result:#find max prob
                if(prob_result[i] > max_prob):
                    max_prob = prob_result[i]
            #print(max_prob)
            list_result = []
            for i in prob_result:
                if(prob_result[i] == max_prob):
                    list_result.append(i)
            #print(list_result)
            result = random.choice(list_result)
            return int(result)     
            
        else:
            if(self.memory == [['']]):#if not have memory
                result = random.randint(1, 9)
                while(True):
                    if(str(result) in cur_position):
                        result = random.randint(1, 9)
                    else:
                        print("random answer")
                        return result
            prob_result = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            count_memory = len(self.memory)
            
            state_k_prob = []
            for i in self.memory:#select only curposition match
                check_before_state = False
                count_cur_posi = len(cur_position)
                for j in range(len(cur_position)):#check state before
                    if(i[j] != cur_position[j]):
                        break
                    if(count_cur_posi == 1):
                        check_before_state = True
                    count_cur_posi -= 1
                if(check_before_state):  
                    state_k_prob.append(i)
            #print(state_k_prob)
            if(state_k_prob == []):#not have this pattern in memory
                result = random.randint(1, 9)
                while(True):
                    if(str(result) in cur_position):
                        result = random.randint(1, 9)
                    else:
                        print("random answer")
                        return result
                    
            #print(state)
            before_win = []
            for i in prob_result:#find prob result
                count_posi_win = 0
                for j in state_k_prob:#naive bayes every position
                    if(j[state] == i and (len(j)%2 == 1 or (len(j) == 11 and j[-2] == '1'))):
                        count_posi_win += 1
                        before_win.append(j)
                prob_posi = count_posi_win/count_memory
                prob_result[i] += prob_posi
                
            #print(prob_result)
            #print(before_win)
            if(before_win == []):#if every prob_result = 0, we will find position for min lose rate
                before_lose = []
                for i in prob_result:
                    count_posi_lose = 0
                    for j in state_k_prob:
                        if(j[state] == i and len(j)%2 == 0):#select after win
                            count_posi_lose += 1
                            before_lose.append(j)
                    prob_posi = count_posi_lose/count_memory
                    prob_result[i] += prob_posi
                    
                if(before_lose == []):#not have every thing return random
                    result = random.randint(1, 9)
                    while(True):
                        if(str(result) in cur_position):
                            result = random.randint(1, 9)
                        else:
                            print("random answer")
                            return result

                print("avoidance lose: ",before_lose)       
                min_prob = 1
                for i in prob_result:#find min prob
                    if(prob_result[i] < min_prob):
                        min_prob = prob_result[i]
                list_result = []
                for i in prob_result:
                    if(prob_result[i] == min_prob):
                        list_result.append(i)
                result = random.choice(list_result)
                while(True):
                    if(result in cur_position):
                        prob_result.pop(result)
                        min_prob = 1
                        for i in prob_result:#find new min prob
                            if(prob_result[i] < min_prob):
                                min_prob = prob_result[i]
                        list_result = []
                        for i in prob_result:
                            if(prob_result[i] == min_prob):
                                list_result.append(i)
                        result = random.choice(list_result)
                    else:
                        return int(result)
                                    
            print("In memory win: ",before_win)           
            max_prob = 0
            for i in prob_result:#find max prob
                if(prob_result[i] > max_prob):
                    max_prob = prob_result[i]
            #print(max_prob)
            list_result = []
            for i in prob_result:
                if(prob_result[i] == max_prob):
                    list_result.append(i)
            #print(list_result)
            #print(prob_result)
            result = random.choice(list_result)
            while(True):
                if(result in cur_position):
                    prob_result.pop(result)
                    max_prob = 0
                    for i in prob_result:#find new max prob
                        if(prob_result[i] > max_prob):
                            max_prob = prob_result[i]
                    list_result = []
                    for i in prob_result:
                        if(prob_result[i] == max_prob):
                            list_result.append(i)
                    result = random.choice(list_result)
                else:
                    return int(result)
                
    def choose_naive_bayes_after(self,cur_position,state):
        if(self.memory == [['']]):#if not have memory
                result = random.randint(1, 9)
                while(True):
                    if(str(result) in cur_position):
                        result = random.randint(1, 9)
                    else:
                        print("random answer")
                        return result
        prob_result = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        count_memory = len(self.memory)
        state_k_prob = []
        for i in self.memory:#select only curposition match
            check_before_state = False
            count_cur_posi = len(cur_position)
            for j in range(len(cur_position)):#check state before
                if(i[j] != cur_position[j]):
                    break
                if(count_cur_posi == 1):
                    check_before_state = True
                count_cur_posi -= 1
            if(check_before_state):  
                state_k_prob.append(i)
        #print(state_k_prob)

        if(state_k_prob == []):#not have pattern in memory
            result = random.randint(1, 9)
            while(True):
                if(str(result) in cur_position):
                    result = random.randint(1, 9)
                else:
                    print("random answer")
                    return result
                    
        
        #print(state)
        after_win = []
        for i in prob_result:#find prob result
            count_posi_win = 0
            for j in state_k_prob:#naive bayes every position
                if(j[state] == i and (len(j)%2 == 0 or (len(j) == 11 and j[-2] == '1'))):
                    count_posi_win += 1
                    after_win.append(j)
            prop_posi = count_posi_win/count_memory
            prob_result[i] += prop_posi
        
        #print(prob_result)
        if(after_win == []):#if every prob_result = 0, we will find position for min lose rate
            after_lose = []
            for i in prob_result:
                count_posi_lose = 0
                for j in state_k_prob:
                    if(j[state] == i and len(j)%2 == 1):#select after win
                        count_posi_lose += 1
                        after_lose.append(j)
                prob_posi = count_posi_lose/count_memory
                prob_result[i] += prob_posi
               
            if(after_lose == []):#not have every thing return random
                result = random.randint(1, 9)
                while(True):
                    if(str(result) in cur_position):
                        result = random.randint(1, 9)
                    else:
                        print("random answer")
                        return result

            print("avoidance lose: ",after_lose)     
            min_prob = 1
            for i in prob_result:#find min prob
                if(prob_result[i] < min_prob):
                    min_prob = prob_result[i]
            list_result = []
            for i in prob_result:
                if(prob_result[i] == min_prob):
                    list_result.append(i)
            result = random.choice(list_result)
            while(True):
                if(result in cur_position):
                    prob_result.pop(result)
                    min_prob = 1
                    for i in prob_result:#find new min prob
                        if(prob_result[i] < min_prob):
                            min_prob = prob_result[i]
                    list_result = []
                    for i in prob_result:
                        if(prob_result[i] == min_prob):
                            list_result.append(i)
                    result = random.choice(list_result)
                else:
                    return int(result)

        print("In memory win: ",after_win)       
        max_prob = 0
        for i in prob_result:#find max prob
            if(prob_result[i] > max_prob):
                max_prob = prob_result[i]
        #print(max_prob)
        list_result = []
        for i in prob_result:
            if(prob_result[i] == max_prob):
                list_result.append(i)
        #print(list_result)
        #print(prob_result)
        result = random.choice(list_result)
        while(True):
            if(result in cur_position):
                prob_result.pop(result)
                max_prob = 0
                for i in prob_result:#find new max prob
                    if(prob_result[i] > max_prob):
                        max_prob = prob_result[i]
                list_result = []
                for i in prob_result:
                    if(prob_result[i] == max_prob):
                        list_result.append(i)
                result = random.choice(list_result)
            else:
                return int(result)
                           
           
tk = Tk()
tk.title("XO GAME")

pa = StringVar()
playerb = StringVar()
# p1 = StringVar()
# p2 = StringVar()
bclick = True
flag = 0
state_p = 1
state_ai = 1
table = [["","",""],["","",""],["","",""]]
posi_memory = []
ai_1 = Ai()

def restart_program(): # เมื่อเกมจบหรือเสมอให้เริ่มตัวโปรแกรมใหม่
    python = sys.executable
    os.execl(python, python, * sys.argv)


def disableButton(): #// hide ปุ่มเฉยๆ
    button1.configure(state=DISABLED) 
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def btnClick(buttons, i, j,mode):
    global bclick, flag, player2_name, player1_name, playerb, pa, state_ai ,state_p
    if(mode == 1):
        playerb = "Player O Wins!"                  # เมื่อ playerb ชนะ
        pa = "Player X Wins!"                       # เมื่อ pa ชนะ
        if buttons["text"] == " " and bclick == True:   # เมื่อคลิกครั้งแรก
            buttons["text"] = "X"                       # ใส่ค่า X
            buttons["fg"] = "#ff0000"                   # ใส่สีแดงให้ตัวหนังสือ X
            bclick = False
            table[i][j] = "X"
            if(i == 0 and j == 0):
                posi_memory.append("1")
            elif(i == 0 and j == 1):
                posi_memory.append("2")
            elif(i == 0 and j == 2):
                posi_memory.append("3")
            elif(i == 1 and j == 0):
                posi_memory.append("4")
            elif(i == 1 and j == 1):
                posi_memory.append("5")
            elif(i == 1 and j == 2):
                posi_memory.append("6")
            elif(i == 2 and j == 0):
                posi_memory.append("7")
            elif(i == 2 and j == 1):
                posi_memory.append("8")
            elif(i == 2 and j == 2):
                posi_memory.append("9")
            #print("xxxxxxx")
            #print(posi_memory)
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++
        elif buttons["text"] == " " and bclick == False:# เมื่อคลิกครั้งที่สอง
            buttons["text"] = "O"                       # ใส่ค่า O
            buttons["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
            bclick = True
            table[i][j] = "O"
            if(i == 0 and j == 0):
                posi_memory.append("1")
            elif(i == 0 and j == 1):
                posi_memory.append("2")
            elif(i == 0 and j == 2):
                posi_memory.append("3")
            elif(i == 1 and j == 0):
                posi_memory.append("4")
            elif(i == 1 and j == 1):
                posi_memory.append("5")
            elif(i == 1 and j == 2):
                posi_memory.append("6")
            elif(i == 2 and j == 0):
                posi_memory.append("7")
            elif(i == 2 and j == 1):
                posi_memory.append("8")
            elif(i == 2 and j == 2):
                posi_memory.append("9")
            #print("OOOOOOO")
            #print(posi_memory)
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++
        else:
            tkinter.messagebox.showinfo("XO", "Button already Clicked!")
        
        
    elif(mode == 2):
        playerb = "Player O Wins!"                  # เมื่อ playerb ชนะ
        pa = "Player X Wins!"                       # เมื่อ pa ชนะ
        if buttons["text"] == " " and bclick == True:   # เมื่อคลิกครั้งแรก
            buttons["text"] = "X"                       # ใส่ค่า X
            buttons["fg"] = "#ff0000"                   # ใส่สีแดงให้ตัวหนังสือ X
            bclick = False
            table[i][j] = "X"
            if(i == 0 and j == 0):
                posi_memory.append("1")
            elif(i == 0 and j == 1):
                posi_memory.append("2")
            elif(i == 0 and j == 2):
                posi_memory.append("3")
            elif(i == 1 and j == 0):
                posi_memory.append("4")
            elif(i == 1 and j == 1):
                posi_memory.append("5")
            elif(i == 1 and j == 2):
                posi_memory.append("6")
            elif(i == 2 and j == 0):
                posi_memory.append("7")
            elif(i == 2 and j == 1):
                posi_memory.append("8")
            elif(i == 2 and j == 2):
                posi_memory.append("9")
            #print("xxxxxxx")
            #print(posi_memory)
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++

            position = ai_1.choose_position_after(posi_memory,state_ai)
            posi_memory.append(str(position))
            bclick = True
            
            if(position == 1):
                button1["text"] = "O"                       # ใส่ค่า O
                button1["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[0][0] = "O"
            elif(position == 2):
                button2["text"] = "O"                       # ใส่ค่า O
                button2["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[0][1] = "O"
            elif(position == 3):
                button3["text"] = "O"                       # ใส่ค่า O
                button3["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[0][2] = "O"
            elif(position == 4):
                button4["text"] = "O"                       # ใส่ค่า O
                button4["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[1][0] = "O"
            elif(position == 5):
                button5["text"] = "O"                       # ใส่ค่า O
                button5["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[1][1] = "O"
            elif(position == 6):
                button6["text"] = "O"                       # ใส่ค่า O
                button6["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[1][2] = "O"
            elif(position == 7):
                button7["text"] = "O"                       # ใส่ค่า O
                button7["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[2][0] = "O"
            elif(position == 8):
                button8["text"] = "O"                       # ใส่ค่า O
                button8["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[2][1] = "O"
            elif(position == 9):
                button9["text"] = "O"                       # ใส่ค่า O
                button9["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[2][2] = "O"
            #print("OOOOOOO")
            #print(posi_memory)
            state_ai += 1
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++
        
        else:
            tkinter.messagebox.showinfo("XO", "Button already Clicked!")
    elif(mode == 3):
        playerb = "Player O Wins!"                  # เมื่อ playerb ชนะ
        pa = "Player X Wins!"                       # เมื่อ pa ชนะ
        if buttons["text"] == " " and bclick == False:# เมื่อคลิกครั้งที่สอง
            buttons["text"] = "O"                       # ใส่ค่า O
            buttons["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
            bclick = True
            table[i][j] = "O"
            if(i == 0 and j == 0):
                posi_memory.append("1")
            elif(i == 0 and j == 1):
                posi_memory.append("2")
            elif(i == 0 and j == 2):
                posi_memory.append("3")
            elif(i == 1 and j == 0):
                posi_memory.append("4")
            elif(i == 1 and j == 1):
                posi_memory.append("5")
            elif(i == 1 and j == 2):
                posi_memory.append("6")
            elif(i == 2 and j == 0):
                posi_memory.append("7")
            elif(i == 2 and j == 1):
                posi_memory.append("8")
            elif(i == 2 and j == 2):
                posi_memory.append("9")
            #print("OOOOOOO")
            #print(posi_memory)
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++

            position = ai_1.choose_position_before(posi_memory,state_ai)
            posi_memory.append(str(position))
            bclick = False
            if(position == 1):
                button1["text"] = "X"                       # ใส่ค่า X
                button1["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[0][0] = "X"
            elif(position == 2):
                button2["text"] = "X"                       # ใส่ค่า X
                button2["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[0][1] = "X"
            elif(position == 3):
                button3["text"] = "X"                       # ใส่ค่า X
                button3["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[0][2] = "X"
            elif(position == 4):
                button4["text"] = "X"                       # ใส่ค่า X
                button4["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[1][0] = "X"
            elif(position == 5):
                button5["text"] = "X"                       # ใส่ค่า X
                button5["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[1][1] = "X"
            elif(position == 6):
                button6["text"] = "X"                       # ใส่ค่า X
                button6["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[1][2] = "X"
            elif(position == 7):
                button7["text"] = "X"                       # ใส่ค่า X
                button7["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[2][0] = "X"
            elif(position == 8):
                button8["text"] = "X"                       # ใส่ค่า X
                button8["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[2][1] = "X"
            elif(position == 9):
                button9["text"] = "X"                       # ใส่ค่า X
                button9["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[2][2] = "X"
            #print("XXXXXXX")
            #print(posi_memory)
            state_ai += 1
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++
        else:
            tkinter.messagebox.showinfo("XO", "Button already Clicked!")

    elif(mode == 4):
        playerb = "Player O Wins!"                  # เมื่อ playerb ชนะ
        pa = "Player X Wins!"                       # เมื่อ pa ชนะ
        if buttons["text"] == " " and bclick == False:# เมื่อคลิกครั้งที่สอง
            buttons["text"] = "O"                       # ใส่ค่า O
            buttons["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
            bclick = True
            table[i][j] = "O"
            if(i == 0 and j == 0):
                posi_memory.append("1")
            elif(i == 0 and j == 1):
                posi_memory.append("2")
            elif(i == 0 and j == 2):
                posi_memory.append("3")
            elif(i == 1 and j == 0):
                posi_memory.append("4")
            elif(i == 1 and j == 1):
                posi_memory.append("5")
            elif(i == 1 and j == 2):
                posi_memory.append("6")
            elif(i == 2 and j == 0):
                posi_memory.append("7")
            elif(i == 2 and j == 1):
                posi_memory.append("8")
            elif(i == 2 and j == 2):
                posi_memory.append("9")
            #print("OOOOOOO")
            #print(posi_memory)
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++

            position = ai_1.choose_naive_bayes_before(posi_memory,flag)
            posi_memory.append(str(position))
            bclick = False
            if(position == 1):
                button1["text"] = "X"                       # ใส่ค่า X
                button1["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[0][0] = "X"
            elif(position == 2):
                button2["text"] = "X"                       # ใส่ค่า X
                button2["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[0][1] = "X"
            elif(position == 3):
                button3["text"] = "X"                       # ใส่ค่า X
                button3["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[0][2] = "X"
            elif(position == 4):
                button4["text"] = "X"                       # ใส่ค่า X
                button4["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[1][0] = "X"
            elif(position == 5):
                button5["text"] = "X"                       # ใส่ค่า X
                button5["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[1][1] = "X"
            elif(position == 6):
                button6["text"] = "X"                       # ใส่ค่า X
                button6["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[1][2] = "X"
            elif(position == 7):
                button7["text"] = "X"                       # ใส่ค่า X
                button7["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[2][0] = "X"
            elif(position == 8):
                button8["text"] = "X"                       # ใส่ค่า X
                button8["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[2][1] = "X"
            elif(position == 9):
                button9["text"] = "X"                       # ใส่ค่า X
                button9["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ X
                table[2][2] = "X"
            #print("XXXXXXX")
            #print(posi_memory)
            state_ai += 1
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++
        else:
            tkinter.messagebox.showinfo("XO", "Button already Clicked!")

    elif(mode == 5):
        playerb = "Player O Wins!"                  # เมื่อ playerb ชนะ
        pa = "Player X Wins!"                       # เมื่อ pa ชนะ
        if buttons["text"] == " " and bclick == True:   # เมื่อคลิกครั้งแรก
            buttons["text"] = "X"                       # ใส่ค่า X
            buttons["fg"] = "#ff0000"                   # ใส่สีแดงให้ตัวหนังสือ X
            bclick = False
            table[i][j] = "X"
            if(i == 0 and j == 0):
                posi_memory.append("1")
            elif(i == 0 and j == 1):
                posi_memory.append("2")
            elif(i == 0 and j == 2):
                posi_memory.append("3")
            elif(i == 1 and j == 0):
                posi_memory.append("4")
            elif(i == 1 and j == 1):
                posi_memory.append("5")
            elif(i == 1 and j == 2):
                posi_memory.append("6")
            elif(i == 2 and j == 0):
                posi_memory.append("7")
            elif(i == 2 and j == 1):
                posi_memory.append("8")
            elif(i == 2 and j == 2):
                posi_memory.append("9")
            #print("xxxxxxx")
            #print(posi_memory)
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++

            position = ai_1.choose_naive_bayes_after(posi_memory,flag)
            posi_memory.append(str(position))
            bclick = True
            
            if(position == 1):
                button1["text"] = "O"                       # ใส่ค่า O
                button1["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[0][0] = "O"
            elif(position == 2):
                button2["text"] = "O"                       # ใส่ค่า O
                button2["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[0][1] = "O"
            elif(position == 3):
                button3["text"] = "O"                       # ใส่ค่า O
                button3["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[0][2] = "O"
            elif(position == 4):
                button4["text"] = "O"                       # ใส่ค่า O
                button4["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[1][0] = "O"
            elif(position == 5):
                button5["text"] = "O"                       # ใส่ค่า O
                button5["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[1][1] = "O"
            elif(position == 6):
                button6["text"] = "O"                       # ใส่ค่า O
                button6["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[1][2] = "O"
            elif(position == 7):
                button7["text"] = "O"                       # ใส่ค่า O
                button7["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[2][0] = "O"
            elif(position == 8):
                button8["text"] = "O"                       # ใส่ค่า O
                button8["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[2][1] = "O"
            elif(position == 9):
                button9["text"] = "O"                       # ใส่ค่า O
                button9["fg"] = "#0000ff"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
                table[2][2] = "O"
            #print("OOOOOOO")
            #print(posi_memory)
            state_ai += 1
            checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
            flag += 1                                   # ถ้ายัง flag ++
        
        else:
            tkinter.messagebox.showinfo("XO", "Button already Clicked!")
        
        
            
        

                

def checkForWin(): 
    # กรณีทั้งหมดของ X ที่ชนะ
    #print(table)
    #print(posi_memory)
    #print(flag)
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' ):
        data_list = []
        file = open("table_pattern.txt", "r")
        re = file.readlines()
        for i in re:
            x = i.strip('\n')
            b = x.split(',')
            data_list.append(b)
        #print(data_list)
        check_dup = False
        for i in range(len(data_list)):#find position if have dup for increase use_time
            if(len(data_list[i])-2 == len(posi_memory)):
                for j in range(len(posi_memory)):
                    if(data_list[i][j] != posi_memory[j]):
                        break
                    if(j == len(posi_memory)-1 and data_list[i][j] == posi_memory[j]):
                        posi_in_data_list = i
                        check_dup = True
        #print()
        if(check_dup):#It have dup increase use_time
            print("dupdup X win yes")
            dup =  data_list.pop(posi_in_data_list)
            use = dup[-1]
            use = str(int(use)+1)
            dup[-1] = use
            data_list.insert(0,dup)
            #print(data_list)
            new_data_list = []
            for i in data_list:
                str_data = ','.join(i)
                new_data_list.append(str_data)
            #print(new_data_list)
            with open('table_pattern.txt', 'w') as f:
                for item in new_data_list:
                    f.write("%s\n" % item)
        else:#It not have dup increase pattern in table
            print("dupdup X win no")
            with open('table_pattern.txt', 'a') as f:
                if(len(posi_memory)%2 == 1):
                    count = (len(posi_memory)//2)+1
                    #posi_memory.append(str(count))
                    posi_memory.append('0')
                    posi_memory.append('1')
                else:
                    count = (len(posi_memory)//2)
                    #posi_memory.append(str(count))
                    posi_memory.append('0')
                    posi_memory.append('1')
                str_data = ','.join(posi_memory)
                f.write("%s\n" % str_data)

        disableButton()
        tkinter.messagebox.showinfo("", pa)
        restart_program()

    # กรณีเสมอ
    elif(flag == 8):
        data_list = []
        file = open("table_pattern.txt", "r")
        re = file.readlines()
        for i in re:
            x = i.strip('\n')
            b = x.split(',')
            data_list.append(b)
        #print(data_list)
        check_dup = False
        for i in range(len(data_list)):#find position if have dup for increase use_time
            if(len(data_list[i])-2 == len(posi_memory)):
                for j in range(len(posi_memory)):
                    if(data_list[i][j] != posi_memory[j]):
                        break
                    if(j == len(posi_memory)-1 and data_list[i][j] == posi_memory[j]):
                        posi_in_data_list = i
                        check_dup = True
        #print()
        if(check_dup):#It have dup increase use_time
            print('dupdup yes')
            dup =  data_list.pop(posi_in_data_list)
            use = dup[-1]
            use = str(int(use)+1)
            dup[-1] = use
            data_list.insert(0,dup)
            #print(data_list)
            new_data_list = []
            for i in data_list:
                str_data = ','.join(i)
                new_data_list.append(str_data)
            #print(new_data_list)
            with open('table_pattern.txt', 'w') as f:
                for item in new_data_list:
                    f.write("%s\n" % item)
        else:#It not have dup increase pattern in table
            print('dupdup no')
            with open('table_pattern.txt', 'a') as f:
                if(len(posi_memory)%2 == 1):
                    count = (len(posi_memory)//2)+1
                    #posi_memory.append(str(count))
                    posi_memory.append('1')
                    posi_memory.append('1')
                else:
                    count = (len(posi_memory)//2)
                    #posi_memory.append(str(count))
                    posi_memory.append('1')
                    posi_memory.append('1')
                str_data = ','.join(posi_memory)
                f.write("%s\n" % str_data)
                
        tkinter.messagebox.showinfo("Draw!", "Restart Game")
        restart_program()

    # กรณีทั้งหมดของ X ที่ชนะ
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
        button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
        button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' ):
        data_list = []
        file = open("table_pattern.txt", "r")
        re = file.readlines()
        for i in re:
            x = i.strip('\n')
            b = x.split(',')
            data_list.append(b)
        #print(data_list)
        check_dup = False
        for i in range(len(data_list)):#find position if have dup for increase use_time
            if(len(data_list[i])-2 == len(posi_memory)):
                for j in range(len(posi_memory)):
                    if(data_list[i][j] != posi_memory[j]):
                        break
                    if(j == len(posi_memory)-1 and data_list[i][j] == posi_memory[j]):
                        posi_in_data_list = i
                        check_dup = True
        #print()
        if(check_dup):#It have dup increase use_time
            print("dupdup o win yes")
            dup =  data_list.pop(posi_in_data_list)
            use = dup[-1]
            use = str(int(use)+1)
            dup[-1] = use
            data_list.insert(0,dup)
            #print(data_list)
            new_data_list = []
            for i in data_list:
                str_data = ','.join(i)
                new_data_list.append(str_data)
            #print(new_data_list)
            with open('table_pattern.txt', 'w') as f:
                for item in new_data_list:
                    f.write("%s\n" % item)
        else:#It not have dup increase pattern in table
            print("dupdup o win no")
            with open('table_pattern.txt', 'a') as f:
                if(len(posi_memory)%2 == 1):
                    count = (len(posi_memory)//2)+1
                    #posi_memory.append(str(count))
                    posi_memory.append('0')
                    posi_memory.append('1')
                else:
                    count = (len(posi_memory)//2)
                    #posi_memory.append(str(count))
                    posi_memory.append('0')
                    posi_memory.append('1')
                str_data = ','.join(posi_memory)
                f.write("%s\n" % str_data)
                
        disableButton()
        tkinter.messagebox.showinfo("", playerb)
        restart_program()
    

# สร้างปุ่มบน tk 9 ปุ่ม

            
buttons = StringVar()
mode = 4 #Set mode mode 1 is people vs people
         #mode 2 is people vs AI
         #mode 3 is AI vs people
         #mode 4 is naivebayes AI vs people
         #mode 5 is naivebayes people vs AI

        
button1 = Button(tk, text=" ", font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button1,0,0,mode))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button2,0,1,mode))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button3,0,2,mode))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button4,1,0,mode))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button5,1,1,mode))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button6,1,2,mode))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button7,2,0,mode))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button8,2,1,mode))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='#C9D7E3',
                 fg='#000000', height=4, width=8, command=lambda: btnClick(button9,2,2,mode))
button9.grid(row=5, column=2)

if(mode == 3):
    position = ai_1.choose_position_before(posi_memory,state_ai)
    posi_memory.append(str(position))
    bclick = False
    if(position == 1):
        button1["text"] = "X"                       # ใส่ค่า O
        button1["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[0][0] = "X"
    elif(position == 2):
        button2["text"] = "X"                       # ใส่ค่า O
        button2["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[0][1] = "X"
    elif(position == 3):
        button3["text"] = "X"                       # ใส่ค่า O
        button3["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[0][2] = "X"
    elif(position == 4):
        button4["text"] = "X"                       # ใส่ค่า O
        button4["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[1][0] = "X"
    elif(position == 5):
        button5["text"] = "X"                       # ใส่ค่า O
        button5["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[1][1] = "X"
    elif(position == 6):
        button6["text"] = "X"                       # ใส่ค่า O
        button6["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[1][2] = "X"
    elif(position == 7):
        button7["text"] = "X"                       # ใส่ค่า O
        button7["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[2][0] = "X"
    elif(position == 8):
        button8["text"] = "X"                       # ใส่ค่า O
        button8["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[2][1] = "X"
    elif(position == 9):
        button9["text"] = "X"                       # ใส่ค่า O
        button9["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[2][2] = "X"
    print("XXXXXXX")
    #print(posi_memory)
    state_ai += 1
    checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
    flag += 1                                   # ถ้ายัง flag ++

if(mode == 4):
    position = ai_1.choose_naive_bayes_before(posi_memory,flag)
    posi_memory.append(str(position))
    bclick = False
    if(position == 1):
        button1["text"] = "X"                       # ใส่ค่า O
        button1["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[0][0] = "X"
    elif(position == 2):
        button2["text"] = "X"                       # ใส่ค่า O
        button2["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[0][1] = "X"
    elif(position == 3):
        button3["text"] = "X"                       # ใส่ค่า O
        button3["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[0][2] = "X"
    elif(position == 4):
        button4["text"] = "X"                       # ใส่ค่า O
        button4["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[1][0] = "X"
    elif(position == 5):
        button5["text"] = "X"                       # ใส่ค่า O
        button5["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[1][1] = "X"
    elif(position == 6):
        button6["text"] = "X"                       # ใส่ค่า O
        button6["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[1][2] = "X"
    elif(position == 7):
        button7["text"] = "X"                       # ใส่ค่า O
        button7["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[2][0] = "X"
    elif(position == 8):
        button8["text"] = "X"                       # ใส่ค่า O
        button8["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[2][1] = "X"
    elif(position == 9):
        button9["text"] = "X"                       # ใส่ค่า O
        button9["fg"] = "#ff0000"                   # ใส่สีน้ำเงินให้ตัวหนังสือ O
        table[2][2] = "X"
    print("XXXXXXX")
    state_ai += 1
    checkForWin()                               # ตรวจสอบว่ามีฝ่ายไหนชนะรึยัง
    flag += 1                                   # ถ้ายัง flag ++
    
print("....................")

#tk.mainloop()
