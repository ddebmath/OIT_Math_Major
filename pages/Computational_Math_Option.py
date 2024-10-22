import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title = "Math Major - Computational Mathematics Option", layout = "wide")
st.title("Computational Mathematics Option")
# Load the course list csv file
df = pd.read_csv("pages/course_list_utf.csv")
cp = df['Prefix'].unique()

# Upper div credits
ud_credits = 0

# Default df if no file is uploaded
default_data = {"comm" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "hum" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "ss" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "phy" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "math" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "or" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "senseq" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "oe" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "le" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "details" : ["Default", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]}

# Upload file    
uploaded_file = st.sidebar.file_uploader("Choose a CSV file from last advising")
if uploaded_file != None:
    uploaded_df = pd.read_csv(uploaded_file)
else:
    uploaded_df = pd.DataFrame(default_data)

# Make all the None into empty string    
uploaded_df.fillna("", inplace=True)
#st.write(uploaded_df)

if uploaded_df["details"][1] == "":
    student_name = st.text_input("Student Name (optional):")
else:
    student_name = st.text_input("Student Name (optional):", uploaded_df["details"][1])   

option_selected = "Computational Mathematics"

# col1, col2 = st.columns(2)
# with col1:
#     math_options = ["Default", "Physics", "Computational Mathematics", "Statistics"]
#     option_selected = st.selectbox("Choose your math option", math_options, index = math_options.index(uploaded_df["details"][0]))
#     st.write("## You have chosen " + option_selected + " option")
# with col2:
#     if uploaded_df["details"][1] == "":
#         student_name = st.text_input("Student Name (optional):")
#     else:
#         student_name = st.text_input("Student Name (optional):", uploaded_df["details"][1])    

# Get all the data
com_tc = None if uploaded_df["comm"][0] == "" else uploaded_df["comm"][0]
hum_tc = None if uploaded_df["hum"][0] == "" else uploaded_df["hum"][0]
ss_tc = None if uploaded_df["ss"][0] == "" else uploaded_df["ss"][0]
phy_tc = None if uploaded_df["phy"][0] == "" else uploaded_df["phy"][0]
math_tc = None if uploaded_df["math"][0] == "" else uploaded_df["math"][0]
le_tc = None if uploaded_df["or"][0] == "" else uploaded_df["or"][0]
senseq_tc = None if uploaded_df["senseq"][0] == "" else uploaded_df["senseq"][0]
oe_tc = None if uploaded_df["oe"][0] == "" else uploaded_df["oe"][0]
fe_tc = None if uploaded_df["le"][0] == "" else uploaded_df["le"][0]

# Check boxes
com111z_value = True if uploaded_df["comm"][1] == "True" else False
spe321_value = True if uploaded_df["comm"][2] == "True" else False
wri121z_value = True if uploaded_df["comm"][3] == "True" else False

phy221_value = True if uploaded_df["phy"][1] == "True" else False
phy222_value = True if uploaded_df["phy"][2] == "True" else False

stat201_value = True if uploaded_df["math"][1] == "True" else False
math251_value = True if uploaded_df["math"][2] == "True" else False
math252_value = True if uploaded_df["math"][3] == "True" else False
math253_value = True if uploaded_df["math"][4] == "True" else False
math254_value = True if uploaded_df["math"][5] == "True" else False
math310_value = True if uploaded_df["math"][6] == "True" else False
math321_value = True if uploaded_df["math"][7] == "True" else False
math322_value = True if uploaded_df["math"][8] == "True" else False
math341_value = True if uploaded_df["math"][9] == "True" else False
math346_value = True if uploaded_df["math"][10] == "True" else False
math354_value = True if uploaded_df["math"][11] == "True" else False
math421_value = True if uploaded_df["math"][12] == "True" else False
math451_value = True if uploaded_df["math"][13] == "True" else False
math465_value = True if uploaded_df["math"][14] == "True" else False

cst116_value = True if uploaded_df["or"][1] == "True" else False
cst126_value = True if uploaded_df["or"][2] == "True" else False
cst136_value = True if uploaded_df["or"][3] == "True" else False
math342_value = True if uploaded_df["or"][4] == "True" else False
phy223_value = True if uploaded_df["or"][5] == "True" else False
math361_value = True if uploaded_df["or"][6] == "True" else False

math452_value = True if uploaded_df["senseq"][1] == "True" else False
math453_value = True if uploaded_df["senseq"][2] == "True" else False

cst236_value = True if uploaded_df["oe"][1] == "True" else False
stat211_value = True if uploaded_df["oe"][2] == "True" else False
math362_value = True if uploaded_df["oe"][3] == "True" else False
stat441_value = True if uploaded_df["oe"][4] == "True" else False


# Comm section
def comm_section():
    global com_tc, com_credits, com111z, spe321, wri121z, com_choice1, com1_prefix, com1_cn, ud_credits

    st.write("### Communication (18 Credits)")
    if uploaded_file == None:
        com_tc = st.selectbox("Communication Transfer Credits", list(range(0, 76)))
    else:
        com_tc = st.selectbox("Communication Transfer Credits", list(range(0, 76)), index=int(uploaded_df["comm"][0]))
    
    com111z = st.checkbox("COM 111Z - Public Speaking", value = com111z_value) 
    spe321 = st.checkbox("SPE 321 - Small Group/Team Comm Credits", value = spe321_value)
    wri121z = st.checkbox("WRI 121Z - Composition I", value = wri121z_value) 

    st.write("Communication Elective 1")
    com_col1, com_col2 = st.columns(2)
    with com_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["comm"][4] == ""):
            com1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "com1_prefix")
        else:
            com1_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["comm"][4]))), placeholder = "Pick One", key = "com1_prefix1")
        df_com1 = df[df['Prefix'] == com1_prefix]
    with com_col2:  
        if uploaded_file != None and uploaded_df["comm"][5] != "":  
            com1_cn = st.selectbox("Number", list(df_com1["Code"]), key = "com1_cn", index = int(list(df_com1["Code"]).index(uploaded_df["comm"][5])))
        else:
            com1_cn = st.selectbox("Number", list(df_com1["Code"]), key = "com1_cn1")

    # Find comm choice value
    if uploaded_df["comm"][6] == "":
        com_choice1_index = None
    else:
        com_choice1_index = ["Choose No Class", "WRI 122Z - Composition II", "WRI 227Z - Technical Writing"].index(uploaded_df["comm"][6])


    com_choice1 = st.selectbox("Choose one class", ["Choose No Class", "WRI 122Z - Composition II", "WRI 227Z - Technical Writing"], index = com_choice1_index, placeholder = "Pick One")
    #com_choice2 = st.selectbox("Choose one class", ["Choose No Class", "WRI 327 - Advanced Tech Writing", "WRI 350 - Documentation Development"], index = None, placeholder = "Pick One")
    
    if com_choice1 == None or com_choice1 == "Choose No Class":
        com_choice1_credit = 0
    else:
        com_choice1_credit = 4

    # Find the credit hours for each elective 
    com1_credit = df_com1[df_com1["Code"] == com1_cn]["Credit Hours:"]
    # This is if nothing is chosen then the credits defaults to 0
    if com1_prefix == None or com1_cn == None:
        com1_credit = 0

    com_credits = com_tc + 4*com111z + 3*spe321 + 4*wri121z + int(com1_credit) + com_choice1_credit
    st.write("###### :green[Total Communication Credits:] " + str(f":green[{com_credits}]"))

    # Find number of upper division credits
    ud_credits += 3*spe321
    if com1_cn != None:
        if int(''.join(filter(str.isdigit, com1_cn))) >= 300:
            ud_credits += int(com1_credit)

# Humanities section
def hum_section():
    global hum_tc, hum_credits, hum1_prefix, hum1_cn, hum2_prefix, hum2_cn, hum3_prefix, hum3_cn, ud_credits
    st.write("### Humanities (9 Credits)")
    if uploaded_file == None:
        hum_tc = st.selectbox("Humanities Transfer Credits", list(range(0, 76)))
    else:
        hum_tc = st.selectbox("Humanities Transfer Credits", list(range(0, 76)), index=int(uploaded_df["hum"][0]))
    # Separate Prefix and Course Number for each Humanities elective

    # Class 1        
    st.write("Humanities Elective 1")
    hum_col1, hum_col2 = st.columns(2)
    with hum_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["hum"][1] == ""):
            hum1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "hum1_prefix")
        else:
            hum1_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["hum"][1]))), placeholder = "Pick One", key = "hum1_prefix1")
        df_hum1 = df[df['Prefix'] == hum1_prefix]
    with hum_col2:  
        if uploaded_file != None and uploaded_df["hum"][2] != "":
            hum1_cn = st.selectbox("Number", list(df_hum1["Code"]), key = "hum1_cn", index = int(list(df_hum1["Code"]).index(uploaded_df["hum"][2])))
        else:
            hum1_cn = st.selectbox("Number", list(df_hum1["Code"]), key = "hum1_cn1")
    
    # Class 2
    st.write("Humanities Elective 2")
    hum_col1, hum_col2 = st.columns(2)
    with hum_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["hum"][3] == ""):
            hum2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "hum2_prefix")
        else:
            hum2_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["hum"][3]))), placeholder = "Pick One", key = "hum2_prefix1")
        df_hum2 = df[df['Prefix'] == hum2_prefix]
    with hum_col2:  
        if uploaded_file != None and uploaded_df["hum"][4] != "":  
            hum2_cn = st.selectbox("Number", list(df_hum2["Code"]), key = "hum2_cn", index = int(list(df_hum2["Code"]).index(uploaded_df["hum"][4])))
        else:
            hum2_cn = st.selectbox("Number", list(df_hum2["Code"]), key = "hum2_cn1")
    
    # Class 3
    st.write("Humanities Elective 3")
    hum_col1, hum_col2 = st.columns(2)
    with hum_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["hum"][5] == ""):
            hum3_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "hum3_prefix")
        else:
            hum3_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["hum"][5]))), placeholder = "Pick One", key = "hum3_prefix1")
        df_hum3 = df[df['Prefix'] == hum3_prefix]
    with hum_col2:  
        if uploaded_file != None and uploaded_df["hum"][6] != "":  
            hum3_cn = st.selectbox("Number", list(df_hum3["Code"]), key = "hum3_cn", index = int(list(df_hum3["Code"]).index(uploaded_df["hum"][6])))
        else:
            hum3_cn = st.selectbox("Number", list(df_hum3["Code"]), key = "hum3_cn1")

    # Find the credit hours for each elective 
    hum1_credit = df_hum1[df_hum1["Code"] == hum1_cn]["Credit Hours:"]
    hum2_credit = df_hum2[df_hum2["Code"] == hum2_cn]["Credit Hours:"]
    hum3_credit = df_hum3[df_hum3["Code"] == hum3_cn]["Credit Hours:"]
    # This is if nothing is chosen then the credits defaults to 0
    if hum1_prefix == None or hum1_cn == None:
        hum1_credit = 0
    if hum2_prefix == None or hum2_cn == None:
        hum2_credit = 0
    if hum3_prefix == None or hum3_cn == None:
        hum3_credit = 0

    hum_credits = hum_tc + int(hum1_credit) + int(hum2_credit) + int(hum3_credit)
    st.write("###### :green[Total Humanities Credits:] " + str(f":green[{hum_credits}]"))

    # Find number of upper division credits
    #st.write(hum1_cn)
    if hum1_cn != None:
        if int(''.join(filter(str.isdigit, hum1_cn))) >= 300:
            ud_credits += int(hum1_credit)
    if hum2_cn != None:
        if int(''.join(filter(str.isdigit, hum2_cn))) >= 300:
            ud_credits += int(hum2_credit)
    if hum3_cn != None:
        if int(''.join(filter(str.isdigit, hum3_cn))) >= 300:
            ud_credits += int(hum3_credit)


# Social Science section
def ss_section():
    global ss_tc, ss_credits, ss1_prefix, ss1_cn, ss2_prefix, ss2_cn, ss3_prefix, ss3_cn, ss4_prefix, ss4_cn, ud_credits
    st.write("### Social Science (12 Credits)")
    if uploaded_file == None:
        ss_tc = st.selectbox("Social Science Transfer Credits", list(range(0, 76)))
    else:
        ss_tc = st.selectbox("Social Science Transfer Credits", list(range(0, 76)), index=int(uploaded_df["ss"][0]))
    # Separate Prefix and Course Number for each Humanities elective
    
    # Course 1
    st.write("Social Science Elective 1")
    ss_col1, ss_col2 = st.columns(2)
    with ss_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["ss"][1] == ""):
            ss1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ss1_prefix")
        else:
            ss1_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["ss"][1]))), placeholder = "Pick One", key = "ss1_prefix1")
        df_ss1 = df[df['Prefix'] == ss1_prefix]
    with ss_col2:  
        if uploaded_file != None and uploaded_df["ss"][2] != "":
            ss1_cn = st.selectbox("Number", list(df_ss1["Code"]), key = "ss1_cn", index = int(list(df_ss1["Code"]).index(uploaded_df["ss"][2])))
        else:
            ss1_cn = st.selectbox("Number", list(df_ss1["Code"]), key = "ss1_cn1")

    # Course 2    
    st.write("Social Science Elective 2")
    ss_col1, ss_col2 = st.columns(2)
    with ss_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["ss"][3] == ""):
            ss2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ss2_prefix")
        else:
            ss2_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["ss"][3]))), placeholder = "Pick One", key = "ss2_prefix1")
        df_ss2 = df[df['Prefix'] == ss2_prefix]
    with ss_col2:  
        if uploaded_file != None and uploaded_df["ss"][4] != "":
            ss2_cn = st.selectbox("Number", list(df_ss2["Code"]), key = "ss2_cn", index = int(list(df_ss2["Code"]).index(uploaded_df["ss"][4])))
        else:
            ss2_cn = st.selectbox("Number", list(df_ss2["Code"]), key = "ss2_cn1")
    
    # Course 3
    st.write("Social Science Elective 3")
    ss_col1, ss_col2 = st.columns(2)
    with ss_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["ss"][5] == ""):
            ss3_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ss3_prefix")
        else:
            ss3_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["ss"][5]))), placeholder = "Pick One", key = "ss3_prefix1")
        df_ss3 = df[df['Prefix'] == ss3_prefix]
    with ss_col2:  
        if uploaded_file != None and uploaded_df["ss"][6] != "":
            ss3_cn = st.selectbox("Number", list(df_ss3["Code"]), key = "ss3_cn", index = int(list(df_ss3["Code"]).index(uploaded_df["ss"][6])))
        else:
            ss3_cn = st.selectbox("Number", list(df_ss3["Code"]), key = "ss3_cn1")
        
    
    st.write("Social Science Elective 4")
    ss_col1, ss_col2 = st.columns(2)
    with ss_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["ss"][7] == ""):
            ss4_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ss4_prefix")
        else:
            ss4_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["ss"][7]))), placeholder = "Pick One", key = "ss4_prefix1")
        df_ss4 = df[df['Prefix'] == ss4_prefix]
    with ss_col2:  
        if uploaded_file != None and uploaded_df["ss"][8] != "":
            ss4_cn = st.selectbox("Number", list(df_ss4["Code"]), key = "ss4_cn", index = int(list(df_ss4["Code"]).index(uploaded_df["ss"][8])))
        else:
            ss4_cn = st.selectbox("Number", list(df_ss4["Code"]), key = "ss4_cn1")

    # Find the credit hours for each elective 
    ss1_credit = df_ss1[df_ss1["Code"] == ss1_cn]["Credit Hours:"]
    ss2_credit = df_ss2[df_ss2["Code"] == ss2_cn]["Credit Hours:"]
    ss3_credit = df_ss3[df_ss3["Code"] == ss3_cn]["Credit Hours:"]
    ss4_credit = df_ss4[df_ss4["Code"] == ss4_cn]["Credit Hours:"]
    # This is if nothing is chosen then the credits defaults to 0
    if ss1_prefix == None or ss1_cn == None:
        ss1_credit = 0
    if ss2_prefix == None or ss2_cn == None:
        ss2_credit = 0
    if ss3_prefix == None or ss3_cn == None:
        ss3_credit = 0
    if ss4_prefix == None or ss4_cn == None:
        ss4_credit = 0

    ss_credits = ss_tc + int(ss1_credit) + int(ss2_credit) + int(ss3_credit) + int(ss4_credit)
    st.write("###### :green[Total Social Science Credits:] " + str(f":green[{ss_credits}]"))

    # Find number of upper division credits
    #st.write(hum1_cn)
    if ss1_cn != None:
        if int(''.join(filter(str.isdigit, ss1_cn))) >= 300:
            ud_credits += int(ss1_credit)
    if ss2_cn != None:
        if int(''.join(filter(str.isdigit, ss2_cn))) >= 300:
            ud_credits += int(ss2_credit)
    if ss3_cn != None:
        if int(''.join(filter(str.isdigit, ss3_cn))) >= 300:
            ud_credits += int(ss3_credit)
    if ss4_cn != None:
        if int(''.join(filter(str.isdigit, ss4_cn))) >= 300:
            ud_credits += int(ss4_credit)

# Physics section
def phy_section():
    global phy_tc, phy_credits, phy221, phy222
    st.write("### Physics (8 Credits)")
    if uploaded_file == None:
        phy_tc = st.selectbox("Physics Transfer Credits", list(range(0, 76)))
    else:
        phy_tc = st.selectbox("Physics Transfer Credits", list(range(0, 76)), index=int(uploaded_df["phy"][0]))
    phy221 = st.checkbox("PHY 221 - General Physics with Calculus I", value = phy221_value) 
    phy222 = st.checkbox("PHY 222 - General Physics with Calculus II", value = phy222_value)
     

    phy_credits = phy_tc + 4*phy221 + 4*phy222 
    st.write("###### :green[Total Physics Credits:] " + str(f":green[{phy_credits}]"))


# Core math section
def math_section():
    global math_tc, math_credits, stat201, math251, math252, math253, math254, math310, math321, math322, math341, math346, math354, math421, math451, math465, ud_credits
    st.write("### Mathematics (56 Credits)")
    if uploaded_file == None:
        math_tc = st.selectbox("Mathematics Transfer Credits", list(range(0, 76)))
    else:
        math_tc = st.selectbox("Mathematics Transfer Credits", list(range(0, 76)), index=int(uploaded_df["math"][0]))
    ld_math_col, ud_math_col = st.columns(2)
    with ld_math_col:
        st.write("#### Lower Division Math (20 credits)")
        stat201 = st.checkbox("STAT 201 - Intro to Data Science", value = stat201_value) 
        math251 = st.checkbox("MATH 251 - Differential Calculus", value = math251_value)
        math252 = st.checkbox("MATH 252 - Integral Calculus", value = math252_value) 
        math253 = st.checkbox("MATH 253 - Sequences and Series", value = math253_value)
        math254 = st.checkbox("MATH 254 - Vector Calculus I", value = math254_value) 
    with ud_math_col:
        st.write("#### Upper Division Math (36 credits)")
        math310 = st.checkbox("MATH 310 - Mathematical Structures", value = math310_value)
        math321 = st.checkbox("MATH 321 - Applied Differential Equations I", value = math321_value) 
        math322 = st.checkbox("MATH 322 - Applied Differential Equations II", value = math322_value) 
        math341 = st.checkbox("MATH 341 - Linear Algebra I", value = math341_value)  
        math346 = st.checkbox("MATH 346 - Number Theory", value = math346_value) 
        math354 = st.checkbox("MATH 354 - Vector Calculus II", value = math354_value) 
        math421 = st.checkbox("MATH 421 - Applied Partial Differential Equations I", value = math421_value)
        math451 = st.checkbox("MATH 451 - Numerical Methods I", value = math451_value)
        math465 = st.checkbox("MATH 465 - Mathematical Statistics", value = math465_value)

    
    math_credits = math_tc + 4*(stat201 + math251 + math252 + math253 + math254 + math310 + math321 + math322 + math341 + math346 + math354 + math421 + math451 + math465)
    st.write("###### :green[Total Core Mathematics Credits:] " + str(f":green[{math_credits}]"))

    # Upper div credits
    ud_credits += 4*(math310 + math321 + math322 + math341 + math346 + math354 + math421 + math451 + math465)


# Required classes
def option_req_section():
    global or_tc, or_credits, cst116, cst126, cst136, math342, phy223, math361, ud_credits
    
    st.write("### Option Specific Classes (Required) (24 Credits)")
    if uploaded_file == None:
        or_tc = st.selectbox("Option Specific Classes (Required) Transfer Credits", list(range(0, 76)))
    else:
        or_tc = st.selectbox("Option Specific Classes (Required) Transfer Credits", list(range(0, 76)), index=int(uploaded_df["or"][0]))
    st.write("Specific Required Classes")
    # Req classes
    cst116 = st.checkbox("CST 116 - C++ Programming I", value = cst116_value)
    cst126 = st.checkbox("CST 126 - C++ Programming II", value = cst126_value)
    cst136 = st.checkbox("CST 136 - OOP with C++", value = cst136_value)
    math342 = st.checkbox("MATH 342 - Linear Algebra II", value = math342_value)
    phy223 = st.checkbox("PHY 223 - General Physics with Calculus III", value = phy223_value)
    math361 = st.checkbox("MATH 361 - Mathematical Statistics I", value = math361_value)
    
            
    or_credits = or_tc + 4*(cst116 + cst126 + cst136 + math342 + phy223 + math361)
    st.write("###### :green[Total Option Specific Classes (Required) Credits:] " + str(f":green[{or_credits}]"))

    # Upper div credits
    ud_credits += 4*(math342 + math361)

def senior_seq_section():
    # Senior Sequence
    global senseq_tc, senseq_credits, math452, math453, ud_credits
    st.write("### Senior Sequence/Project (8 Credits)")
    #st.write(uploaded_df)
    if uploaded_file == None:
        senseq_tc = st.selectbox("Senior Sequence/Project Transfer Credits", list(range(0, 76)))
    else:
        senseq_tc = st.selectbox("Senior Sequence/Project Transfer Credits", list(range(0, 76)), index=int(uploaded_df["senseq"][0]))

    # Find math choice value
    math452 = st.checkbox("MATH 452 - Numerical Methods II", value = math452_value)
    math453 = st.checkbox("MATH 453 - Numerical Methods III", value = math453_value) 


    senseq_credits = senseq_tc + 4*(math452 + math453)
    st.write("###### :green[Senior Sequence/Project Credits:] " + str(f":green[{senseq_credits}]"))

    # Upper div credits
    ud_credits += 4*(math452 + math453)


def option_elec_section():
    global oe_tc, oe_credits, cst236, stat211, math362, stat441, ud_credits
    st.write("### Option Specfic (Elective) (12 Credits)")
    if uploaded_file == None:
        oe_tc = st.selectbox("Option Specfic (Elective) Transfer Credits", list(range(0, 76)))
    else:
        oe_tc = st.selectbox("Option Specfic (Elective) Transfer Credits", list(range(0, 76)), index=int(uploaded_df["oe"][0]))
    st.write("Specific Elective Classes (At least one 300+ class)")

    # Elective classes
    cst236 = st.checkbox("CST 236 - Engineering for Quality Software (Strongly Recommended)", value = stat211_value)
    stat211 = st.checkbox("STAT 211 - Data Science Methods", value = stat211_value)
    math362 = st.checkbox("MATH 362 - Statistical Methods II", value = math362_value) 
    stat441 = st.checkbox("STAT 441 - Statistical Machine Learning I", value = stat441_value)


    oe_credits = oe_tc + 4*(cst236 + stat211 + math362 + stat441)
    st.write("###### :green[Total Focused Elective Sequence Credits:] " + str(f":green[{oe_credits}]"))

    # Upper div credits
    ud_credits += 4*(math362 + stat441)


# Focused elective seq
def free_ele_section():
    global le_tc, le_credits, le1_prefix, le1_cn, le2_prefix, le2_cn, le3_prefix, le3_cn, le4_prefix, le4_cn, le5_prefix, le5_cn, le6_prefix, le6_cn, le7_prefix, le7_cn, le8_prefix, le8_cn, le9_prefix, le9_cn, ud_credits
     # Lower div elective
    st.write("### Lower Division Electives (33 Credits)")
    if uploaded_file == None:
        le_tc = st.selectbox("Lower Division Electives Transfer Credits", list(range(0, 76)))
    else:
        le_tc = st.selectbox("Lower Division Electives Transfer Credits", list(range(0, 76)), index=int(uploaded_df["le"][0]))
    st.write("Specific Elective Classes")

    # Course 1
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][1] == ""):
            le1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le1_prefix")
        else:
            le1_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][1]))), placeholder = "Pick One", key = "le1_prefix1")
        df_le1 = df[df['Prefix'] == le1_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][2] != "":
            le1_cn = st.selectbox("Number", list(df_le1["Code"]), key = "le1_cn", index = int(list(df_le1["Code"]).index(uploaded_df["le"][2])))
        else:
            le1_cn = st.selectbox("Number", list(df_le1["Code"]), key = "le1_cn1") 

    # Course 2
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][3] == ""):
            le2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le2_prefix")
        else:
            le2_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][3]))), placeholder = "Pick One", key = "le2_prefix1")
        df_le2 = df[df['Prefix'] == le2_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][4] != "":
            le2_cn = st.selectbox("Number", list(df_le2["Code"]), key = "le2_cn", index = int(list(df_le2["Code"]).index(uploaded_df["le"][4])))
        else:
            le2_cn = st.selectbox("Number", list(df_le2["Code"]), key = "le2_cn1")  
        
    # Course 3
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][5] == ""):
            le3_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le3_prefix")
        else:
            le3_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][5]))), placeholder = "Pick One", key = "le3_prefix1")
        df_le3 = df[df['Prefix'] == le3_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][6] != "":
            le3_cn = st.selectbox("Number", list(df_le3["Code"]), key = "le3_cn", index = int(list(df_le3["Code"]).index(uploaded_df["le"][6])))
        else:
            le3_cn = st.selectbox("Number", list(df_le3["Code"]), key = "le3_cn1")   

    # Course 4    
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][7] == ""):
            le4_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le4_prefix")
        else:
            le4_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][7]))), placeholder = "Pick One", key = "le4_prefix1")
        df_le4 = df[df['Prefix'] == le4_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][8] != "":
            le4_cn = st.selectbox("Number", list(df_le4["Code"]), key = "le4_cn", index = int(list(df_le4["Code"]).index(uploaded_df["le"][8])))
        else:
            le4_cn = st.selectbox("Number", list(df_le4["Code"]), key = "le4_cn1")  
    
    # Course 5
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][9] == ""):
            le5_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le5_prefix")
        else:
            le5_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][9]))), placeholder = "Pick One", key = "le5_prefix1")
        df_le5 = df[df['Prefix'] == le5_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][10] != "":
            le5_cn = st.selectbox("Number", list(df_le5["Code"]), key = "le5_cn", index = int(list(df_le5["Code"]).index(uploaded_df["le"][10])))
        else:
            le5_cn = st.selectbox("Number", list(df_le5["Code"]), key = "le5_cn1")  

    # Course 6
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][11] == ""):
            le6_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le6_prefix")
        else:
            le6_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][11]))), placeholder = "Pick One", key = "le6_prefix1")
        df_le6 = df[df['Prefix'] == le6_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][12] != "":
            le6_cn = st.selectbox("Number", list(df_le6["Code"]), key = "le6_cn", index = int(list(df_le6["Code"]).index(uploaded_df["le"][12])))
        else:
            le6_cn = st.selectbox("Number", list(df_le6["Code"]), key = "le6_cn1") 

    # Course 7
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][13] == ""):
            le7_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le7_prefix")
        else:
            le7_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][13]))), placeholder = "Pick One", key = "le7_prefix1")
        df_le7 = df[df['Prefix'] == le7_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][14] != "":
            le7_cn = st.selectbox("Number", list(df_le7["Code"]), key = "le7_cn", index = int(list(df_le7["Code"]).index(uploaded_df["le"][14])))
        else:
            le7_cn = st.selectbox("Number", list(df_le7["Code"]), key = "le7_cn1")  
    
    # Course 8
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][15] == ""):
            le8_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le8_prefix")
        else:
            le8_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][15]))), placeholder = "Pick One", key = "le8_prefix1")
        df_le8 = df[df['Prefix'] == le8_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][16] != "":
            le8_cn = st.selectbox("Number", list(df_le8["Code"]), key = "le8_cn", index = int(list(df_le8["Code"]).index(uploaded_df["le"][16])))
        else:
            le8_cn = st.selectbox("Number", list(df_le8["Code"]), key = "le8_cn1")  
        
    # Course 9
    le_col1, le_col2 = st.columns(2)
    with le_col1:
        if uploaded_file == None or (uploaded_file != None and uploaded_df["le"][17] == ""):
            le9_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le9_prefix")
        else:
            le9_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["le"][17]))), placeholder = "Pick One", key = "le9_prefix1")
        df_le9 = df[df['Prefix'] == le9_prefix]
    with le_col2:  
        if uploaded_file != None and uploaded_df["le"][18] != "":
            le9_cn = st.selectbox("Number", list(df_le9["Code"]), key = "le9_cn", index = int(list(df_le9["Code"]).index(uploaded_df["le"][18])))
        else:
            le9_cn = st.selectbox("Number", list(df_le9["Code"]), key = "le9_cn1")

   
    # Find the credit hours for each elective 
    le1_credit = df_le1[df_le1["Code"] == le1_cn]["Credit Hours:"] 
    le2_credit = df_le2[df_le2["Code"] == le2_cn]["Credit Hours:"]
    le3_credit = df_le3[df_le3["Code"] == le3_cn]["Credit Hours:"]
    le4_credit = df_le4[df_le4["Code"] == le4_cn]["Credit Hours:"]
    le5_credit = df_le5[df_le5["Code"] == le5_cn]["Credit Hours:"]
    le6_credit = df_le6[df_le6["Code"] == le6_cn]["Credit Hours:"]
    le7_credit = df_le7[df_le7["Code"] == le7_cn]["Credit Hours:"]
    le8_credit = df_le8[df_le8["Code"] == le8_cn]["Credit Hours:"]
    le9_credit = df_le9[df_le9["Code"] == le9_cn]["Credit Hours:"]

    # This is if nothing is chosen then the credits defaults to 0
    if le1_prefix == None or le1_cn == None:
        le1_credit = 0
    if le2_prefix == None or le2_cn == None:
        le2_credit = 0
    if le3_prefix == None or le3_cn == None:
        le3_credit = 0
    if le4_prefix == None or le4_cn == None:
        le4_credit = 0
    if le5_prefix == None or le5_cn == None:
        le5_credit = 0
    if le6_prefix == None or le6_cn == None:
        le6_credit = 0
    if le7_prefix == None or le7_cn == None:
        le7_credit = 0
    if le8_prefix == None or le8_cn == None:
        le8_credit = 0
    if le9_prefix == None or le9_cn == None:
        le9_credit = 0

    le_credits = le_tc + int(le1_credit) + int(le2_credit) + int(le3_credit) + int(le4_credit) + int(le5_credit) + int(le6_credit) + int(le7_credit) + int(le8_credit) + int(le9_credit)
    st.write("###### :green[Free Elective Credits:] " + str(f":green[{le_credits}]"))

    # Find number of upper division credits
    #st.write(hum1_cn)
    if le1_cn != None:
        if int(''.join(filter(str.isdigit, le1_cn))) >= 300:
            ud_credits += int(le1_credit)
    if le2_cn != None:
        if int(''.join(filter(str.isdigit, le2_cn)))>= 300:
            ud_credits += int(le2_credit)
    if le3_cn != None:
        if int(''.join(filter(str.isdigit, le3_cn))) >= 300:
            ud_credits += int(le3_credit)
    if le4_cn != None:
        if int(''.join(filter(str.isdigit, le4_cn))) >= 300:
            ud_credits += int(le4_credit)
    if le5_cn != None:
        if int(''.join(filter(str.isdigit, le5_cn))) >= 300:
            ud_credits += int(le5_credit)
    if le6_cn != None:
        if int(''.join(filter(str.isdigit, le6_cn))) >= 300:
            ud_credits += int(le6_credit)
    if le7_cn != None:
        if int(''.join(filter(str.isdigit, le7_cn))) >= 300:
            ud_credits += int(le7_credit)
    if le8_cn != None:
        if int(''.join(filter(str.isdigit, le8_cn))) >= 300:
            ud_credits += int(le8_credit)
    if le9_cn != None:
        if int(''.join(filter(str.isdigit, le9_cn))) >= 300:
            ud_credits += int(le9_credit)


# Default option
def comp_math_option():
    # General Education Classes
    with st.expander("General Education Classes"):
        com_col, hum_col, ss_col, phy_col = st.columns(4)

        # Communication
        with com_col:
            # Comm
            comm_section()
        with hum_col:
            # Humanities
            hum_section()   
        with ss_col:
            # Social Science
            ss_section() 
        with phy_col:
            # Physics
            phy_section()
    # Core Math Classes
    with st.expander("Core Mathematics Classes"):
        math_section()
    # General Education Classes
    with st.expander("Option Specific Classes"):
        option_req_col, sen_seq_col, foc_ele_seq_col, free_ele_col = st.columns(4)

        # Option Req
        with option_req_col:
            option_req_section()

        # Senior Seq
        with sen_seq_col:
            senior_seq_section()
        
        # Option Elec
        with foc_ele_seq_col:
            option_elec_section()

        # Free elec
        with free_ele_col:
            free_ele_section()

       
comp_math_option()

# Update credits on the sidebar
with st.sidebar.expander("Total General Education Credits: " + str(com_credits + hum_credits + ss_credits + phy_credits) + " (" + str(47 - (com_credits + hum_credits + ss_credits + phy_credits)) + " needed)"):
    st.write("#### Total Communication Credits: " + str(com_credits) + " (" + str(18-com_credits) + " needed)")
    st.write("#### Total Humanities Credits: " + str(hum_credits) + " (" + str(9-hum_credits) + " needed)")
    st.write("#### Total Social Science Credits: " + str(ss_credits) + " (" + str(12-ss_credits) + " needed)")
    st.write("#### Total Physics Credits: " + str(phy_credits) + " (" + str(8-phy_credits) + " needed)")
st.sidebar.write("#### Total Math Credits: " + str(math_credits) + " (" + str(56-math_credits) + " needed)")
with st.sidebar.expander("#### Total Option Specific Credits: " + str(or_credits + senseq_credits + oe_credits + le_credits) + " (" + str(32-(or_credits + senseq_credits + oe_credits + le_credits)) + " needed)"):
    st.write("#### Total Option Specific Classes (Required) Credits: " + str(or_credits) + " (" + str(12-or_credits) + " needed)")
    st.write("#### Total Senior Sequence/Project Credits: " + str(senseq_credits) + " (" + str(8-senseq_credits) + " needed)")
    st.write("#### Total Option Specific Classes (Elective) Credits: " + str(oe_credits) + " (" + str(12-oe_credits) + " needed)")
st.sidebar.write("#### Total Free Electives Credits: " + str(le_credits) + " (" + str(33-le_credits) + " needed)")



with st.expander("Analysis and Download"):
    # Draw the bar graph showing the credits left
    st.write("#### Analyze Credits")
    credits_data = pd.DataFrame(
                    {
                        "Sections" : ["Comm", "Hum", "Soc Sci", "Phy", "Math", "Option Req.", "Senior Seq.", "Option Elec.", "Free Elec."],
                        "Credits Acquired" : [com_credits, hum_credits, ss_credits, phy_credits, math_credits, or_credits, senseq_credits, oe_credits, le_credits],
                        "Credits Needed" : [18-com_credits, 9-hum_credits, 12-ss_credits, 19-phy_credits, 64-math_credits, 15-or_credits, 8-senseq_credits, 12-oe_credits, 33-le_credits]
                    
                    }
                    )  
    st.bar_chart(
        credits_data,
        x="Sections",
        y=["Credits Acquired", "Credits Needed"],
        color=["#35bd59", "#bd4c35"],  # Optional
    )    

    total_credits_acquired = com_credits + hum_credits + ss_credits + phy_credits + math_credits + or_credits + senseq_credits + oe_credits + le_credits
    total_credits_needed = 180 - total_credits_acquired
    st.write("#### Total Credits Acquired - " + str(total_credits_acquired))
    st.write("#### Total Credits Needed - " + str(total_credits_needed))
    st.write("#### Total Upper Division (300+) Credits (from OIT) - " + str(ud_credits) + "/" + str(60))
    st.sidebar.write("## :green[CREDITS] - " + str(total_credits_acquired) + "/" + str(180))

    # Creating a data frame to download
    created_data = {"comm" : [com_tc, com111z, spe321, wri121z, com1_prefix, com1_cn, com_choice1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "hum" : [hum_tc, hum1_prefix, hum1_cn, hum2_prefix, hum2_cn, hum3_prefix, hum3_cn, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "ss" : [ss_tc, ss1_prefix, ss1_cn, ss2_prefix, ss2_cn, ss3_prefix, ss3_cn, ss4_prefix, ss4_cn, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "phy" : [phy_tc, phy221, phy222, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "math" : [math_tc, stat201, math251, math252, math253, math254, math310, math321, math322, math341, math346, math354, math421, math451, math465, None, None, None, None, None, None, None, None, None, None],
                    "or" : [or_tc, cst116, cst126, cst136, math342, phy223, math361, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "senseq" : [senseq_tc, math452, math453, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "oe" : [oe_tc, cst236, stat211, math362, stat441, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "le" : [le_tc, le1_prefix, le1_cn, le2_prefix, le2_cn, le3_prefix, le3_cn, le4_prefix, le4_cn, le5_prefix, le5_cn, le6_prefix, le6_cn, le7_prefix, le7_cn, \
                            le8_prefix, le8_cn, le9_prefix, le9_cn, None, None, None, None, None, None],
                    "details" : [option_selected, student_name, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]}


    @st.cache_data
    def convert_df(df):
        conv_df = pd.DataFrame(df)
        return conv_df.to_csv(index=False).encode('utf-8')
    conv_csv = convert_df(created_data)
    
    # Download file
    st.download_button(
        "Download CSV File for future advising",
        conv_csv,
        "math_major_advising_" + str(student_name) + "_" + str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')) +".csv",
        "text/csv",
        key='download-csv',
        help = 'Download a CSV file for future advising'
    )


# Bugs
issue_url = "https://github.com/ddebmath/OIT_Math_Major/issues"
st.write("For any bugs, please create an issue ticket at my [GitHub](%s)" % issue_url)

