import streamlit as st
from collections import Counter
import math 

inpu = st.text_input("Enter a word to arrange its letters:")
word =str(inpu)
st.caption("The word you entered is  :{}".format(word))
def wordarrangement(word):
    dic  = sorted(Counter(word).items() , key =lambda item : item[1] , reverse=True)
    non_dis_dic={}
    non_dis_lst=[]
    for k , v in dic :
        if v >1:
            non_dis_dic[k]=v
            non_dis_lst.append(v)
    den=1
    for i in non_dis_lst:
        den=den*math.perm(i,i)

    num =math.perm(len(word),len(word))
    result = num/den
    st.text("Non_distinct items :                             :{}\nArrangement without counting non_distinct items  :{}\nNon_distinct items factorial:{}\nfinal answer :{}".format(non_dis_dic, num, den , result))
wordarrangement(word)
