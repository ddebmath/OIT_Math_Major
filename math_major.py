import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title = "Math Major", layout = "wide")
st.title("Math Major Advising")

# Default df if no file is uploaded
default_data = {"comm" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "hum" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "ss" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "phy" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "math" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "le" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "ue" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "fes" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                "fe" : [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]}

# Upload file    
uploaded_file = st.sidebar.file_uploader("Choose a CSV file")
if uploaded_file != None:
    uploaded_df = pd.read_csv(uploaded_file)
else:
    uploaded_df = pd.DataFrame(default_data)

# Make all the None into empty string    
uploaded_df.fillna("", inplace=True)
#st.write(uploaded_df)
# Get all the data
com_tc = None if uploaded_df["comm"][0] == "" else uploaded_df["comm"][0]
hum_tc = None if uploaded_df["hum"][0] == "" else uploaded_df["hum"][0]
ss_tc = None if uploaded_df["ss"][0] == "" else uploaded_df["ss"][0]
phy_tc = None if uploaded_df["phy"][0] == "" else uploaded_df["phy"][0]
math_tc = None if uploaded_df["math"][0] == "" else uploaded_df["math"][0]
le_tc = None if uploaded_df["le"][0] == "" else uploaded_df["le"][0]
ue_tc = None if uploaded_df["ue"][0] == "" else uploaded_df["ue"][0]
fes_tc = None if uploaded_df["fes"][0] == "" else uploaded_df["fes"][0]
fe_tc = None if uploaded_df["fe"][0] == "" else uploaded_df["fe"][0]

math_options = ["Default", "Physics", "Computational Mathematics", "Statistics"]
option_selected = st.sidebar.selectbox("Choose your math option", math_options)
st.sidebar.write("You have chosen " + option_selected + " option")

# Load the course list csv file
df = pd.read_csv("course_list_utf.csv")
cp = df['Prefix'].unique()

#st.write(cp)
# General Education Classes
with st.expander("General Education Classes"):
    com_col, hum_col, ss_col, phy_col = st.columns(4)

    # Communication
    with com_col:
        st.write("### Communication (18 Credits)")
        com_tc = st.selectbox("Comm. Transfer Credits", list(range(0, 76)))
        com111z = st.checkbox("COM 111Z - Public Speaking") 
        spe321 = st.checkbox("SPE 321 - Small Group/Team Comm Credits")
        wri121z = st.checkbox("WRI 121Z - Composition I") 
        com_choice1 = st.selectbox("Choose one class", ("WRI 122Z - Composition II", "WRI 227Z - Technical Writing"), index = None, placeholder = "Pick One")
        com_choice2 = st.selectbox("Choose one class", ("WRI 327 - Advanced Tech Writing", "WRI 350 - Documentation Development"), index = None, placeholder = "Pick One")
        if com_choice1 == None:
            com_choice1_credit = 0
        else:
            com_choice1_credit = 4
        if com_choice2 == None:
            com_choice2_credit = 0
        else:
            com_choice2_credit = 3
        com_credits = com_tc + 4*com111z + 3*spe321 + 4*wri121z + com_choice1_credit + com_choice2_credit
        st.write("###### Total Communication Credits: " + str(com_credits))

    # Humanities
    with hum_col:
        st.write("### Humanities (9 Credits)")
        hum_tc = st.selectbox("Humanities Transfer Credits", list(range(0, 76)))
        # Separate Prefix and Course Number for each Humanities elective
        st.write("Humanities Elective 1")
        hum_col1, hum_col2 = st.columns(2)
        with hum_col1:
            hum_ele1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "hum_ele1_prefix")
            df_hum1 = df[df['Prefix'] == hum_ele1_prefix]
        with hum_col2:    
            hum_ele1_cn = st.selectbox("Number", list(df_hum1["Code"]), key = "hum_ele1_cn")
            
        st.write("Humanities Elective 2")
        hum_col1, hum_col2 = st.columns(2)
        with hum_col1:
            hum_ele2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "hum_ele2_prefix")
            df_hum2 = df[df['Prefix'] == hum_ele2_prefix]
        with hum_col2:    
            hum_ele2_cn = st.selectbox("Number", list(df_hum2["Code"]), key = "hum_ele2_cn")
        
        st.write("Humanities Elective 3")
        hum_col1, hum_col2 = st.columns(2)
        with hum_col1:
            hum_ele3_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "hum_ele3_prefix")
            df_hum3 = df[df['Prefix'] == hum_ele3_prefix]
        with hum_col2:    
            hum_ele3_cn = st.selectbox("Number", list(df_hum3["Code"]), key = "hum_ele3_cn")

        # Find the credit hours for each elective 
        hum1_credit = df_hum1[df_hum1["Code"] == hum_ele1_cn]["Credit Hours:"]
        hum2_credit = df_hum2[df_hum2["Code"] == hum_ele2_cn]["Credit Hours:"]
        hum3_credit = df_hum3[df_hum3["Code"] == hum_ele3_cn]["Credit Hours:"]
        # This is if nothing is chosen then the credits defaults to 0
        if hum_ele1_prefix == None or hum_ele1_cn == None:
            hum1_credit = 0
        if hum_ele2_prefix == None or hum_ele2_cn == None:
            hum2_credit = 0
        if hum_ele3_prefix == None or hum_ele3_cn == None:
            hum3_credit = 0

        hum_credits = hum_tc + int(hum1_credit) + int(hum2_credit) + int(hum3_credit)
        st.write("###### Total Humanities Credits: " + str(hum_credits))

    # Social Science
    with ss_col:
        st.write("### Social Science (12 Credits)")
        ss_tc = st.selectbox("Social Science Transfer Credits", list(range(0, 76)))
        # Separate Prefix and Course Number for each Humanities elective
        st.write("Social Science Elective 1")
        ss_col1, ss_col2 = st.columns(2)
        with ss_col1:
            ss_ele1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ss_ele1_prefix")
            df_ss1 = df[df['Prefix'] == ss_ele1_prefix]
        with ss_col2:    
            ss_ele1_cn = st.selectbox("Number", list(df_ss1["Code"]), key = "ss_ele1_cn")
            
        st.write("Social Science Elective 2")
        ss_col1, ss_col2 = st.columns(2)
        with ss_col1:
            ss_ele2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ss_ele2_prefix")
            df_ss2 = df[df['Prefix'] == ss_ele2_prefix]
        with ss_col2:    
            ss_ele2_cn = st.selectbox("Number", list(df_ss2["Code"]), key = "ss_ele2_cn")
        
        st.write("Social Science Elective 3")
        ss_col1, ss_col2 = st.columns(2)
        with ss_col1:
            ss_ele3_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ss_ele3_prefix")
            df_ss3 = df[df['Prefix'] == ss_ele3_prefix]
        with ss_col2:    
            ss_ele3_cn = st.selectbox("Number", list(df_ss3["Code"]), key = "ss_ele3_cn")
        
        st.write("Social Science Elective 4")
        ss_col1, ss_col2 = st.columns(2)
        with ss_col1:
            ss_ele4_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ss_ele4_prefix")
            df_ss4 = df[df['Prefix'] == ss_ele4_prefix]
        with ss_col2:    
            ss_ele4_cn = st.selectbox("Number", list(df_ss4["Code"]), key = "ss_ele4_cn")

        # Find the credit hours for each elective 
        ss1_credit = df_ss1[df_ss1["Code"] == ss_ele1_cn]["Credit Hours:"]
        ss2_credit = df_ss2[df_ss2["Code"] == ss_ele2_cn]["Credit Hours:"]
        ss3_credit = df_ss3[df_ss3["Code"] == ss_ele3_cn]["Credit Hours:"]
        ss4_credit = df_ss3[df_ss3["Code"] == ss_ele3_cn]["Credit Hours:"]
        # This is if nothing is chosen then the credits defaults to 0
        if ss_ele1_prefix == None or ss_ele1_cn == None:
            ss1_credit = 0
        if ss_ele2_prefix == None or ss_ele2_cn == None:
            ss2_credit = 0
        if ss_ele3_prefix == None or ss_ele3_cn == None:
            ss3_credit = 0
        if ss_ele4_prefix == None or ss_ele4_cn == None:
            ss4_credit = 0

        ss_credits = ss_tc + int(ss1_credit) + int(ss2_credit) + int(ss3_credit) + int(ss4_credit)
        st.write("###### Total Social Science Credits: " + str(ss_credits))

    # Physics
    with phy_col:
        st.write("### Physics (19 Credits)")
        phy_tc = st.selectbox("Physics Transfer Credits", list(range(0, 76)))
        phy221 = st.checkbox("PHY 221 - General Physics with Calculus I") 
        phy222 = st.checkbox("PHY 222 - General Physics with Calculus II")
        phy223 = st.checkbox("PHY 223 - General Physics with Calculus III") 

        # Math/Physics Elective
        st.write("Math/Physics Elective 1")
        phy_col1, phy_col2 = st.columns(2)
        with phy_col1:
            phy_ele1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "phy_ele1_prefix")
            df_phy1 = df[df['Prefix'] == phy_ele1_prefix]
        with phy_col2:    
            phy_ele1_cn = st.selectbox("Number", list(df_phy1["Code"]), key = "phy_ele1_cn")
            
        st.write("Math/Physics Elective 2")
        phy_col1, phy_col2 = st.columns(2)
        with phy_col1:
            phy_ele2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "phy_ele2_prefix")
            df_phy2 = df[df['Prefix'] == phy_ele2_prefix]
        with phy_col2:    
            phy_ele2_cn = st.selectbox("Number", list(df_phy2["Code"]), key = "phy_ele2_cn")
        
        # Find the credit hours for each elective 
        phy1_credit = df_phy1[df_phy1["Code"] == phy_ele1_cn]["Credit Hours:"]
        phy2_credit = df_phy2[df_phy2["Code"] == phy_ele2_cn]["Credit Hours:"]      

        # This is if nothing is chosen then the credits defaults to 0
        if phy_ele1_prefix == None or phy_ele1_cn == None:
            phy1_credit = 0
        if phy_ele2_prefix == None or phy_ele2_cn == None:
            phy2_credit = 0

        phy_credits = phy_tc + 4*phy221 + 4*phy222 + 4*phy223 + int(phy1_credit) + int(phy2_credit)
        st.write("###### Total Physics Credits: " + str(phy_credits))


# Core Math Classes
with st.expander("Core Mathematics Classes"):
    st.write("### Mathematics (64 Credits)")
    if uploaded_file == None:
        math_tc = st.selectbox("Mathematics Transfer Credits", list(range(0, 76)))
    else:
        math_tc = st.selectbox("Mathematics Transfer Credits", list(range(0, 76)), index=int(uploaded_df["math"][0]))
    stat201 = st.checkbox("STAT 201 - Intro to Data Science") 
    math251 = st.checkbox("MATH 251 - Differential Calculus")
    math252 = st.checkbox("MATH 252 - Integral Calculus") 
    math253 = st.checkbox("MATH 253 - Sequences and Series")
    math254 = st.checkbox("MATH 254 - Vector Calculus I") 
    math310 = st.checkbox("MATH 310 - Mathematical Structures")
    math321 = st.checkbox("MATH 321 - Applied Differential Equations I") 
    math322 = st.checkbox("MATH 322 - Applied Differential Equations II") 
    math341 = st.checkbox("MATH 341 - Linear Algebra I")  
    math346 = st.checkbox("MATH 346 - Number Theory") 
    math354 = st.checkbox("MATH 354 - Vector Calculus II") 
    math421 = st.checkbox("MATH 421 - Applied Partial Differential Equations I")
    math451 = st.checkbox("MATH 451 - Applied Numerical Methods I")

    math_choice1 = st.selectbox("Choose one class", ("Choose No Class", "MATH 422 - Applied Partial Differential Equations II", "MATH 423 - Applied Partial Differential Equations III", "MATH 452 - Applied Numerical Methods II", "MATH 453 - Applied Numerical Methods III"), index = None, placeholder = "Pick One", key = "math_choice1")
    math_choice2 = st.selectbox("Choose one class", ("Choose No Class", "MATH 422 - Applied Partial Differential Equations II", "MATH 423 - Applied Partial Differential Equations III", "MATH 452 - Applied Numerical Methods II", "MATH 453 - Applied Numerical Methods III"), index = None, placeholder = "Pick One", key = "math_choice2")

    if math_choice1 == None or math_choice1 == "Choose No Class":
        math_choice1_credit = 0
    else:
        math_choice1_credit = 1
    if math_choice2 == None or math_choice2 == "Choose No Class":
        math_choice2_credit = 0
    else:
        math_choice2_credit = 1
    math_credits = math_tc + 4*(stat201 + math251 + math252 + math253 + math254 + math310 + math321 + math322 + math341 + math346 + math354 + math421 + math451 + math_choice1_credit + math_choice2_credit)
    st.write("###### Total Mathematics Credits: " + str(math_credits))

# General Education Classes
with st.expander("Elective Classes"):
    lower_ele_col, upper_ele_col, foc_ele_seq_col, foc_ele_col = st.columns(4)

    # Lower div electives
    with lower_ele_col:
        st.write("### Lower Division Electives (35 Credits)")
        le_tc = st.selectbox("Lower Division Electives Transfer Credits", list(range(0, 76)))
        st.write("Specific Elective Classes")

        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le1_prefix")
            df_le1 = df[df['Prefix'] == le1_prefix]
        with le_col2:    
            le1_cn = st.selectbox("Number", list(df_le1["Code"]), key = "le1_cn") 
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le2_prefix")
            df_le2 = df[df['Prefix'] == le2_prefix]
        with le_col2:    
            le2_cn = st.selectbox("Number", list(df_le2["Code"]), key = "le2_cn")   
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le3_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le3_prefix")
            df_le3 = df[df['Prefix'] == le3_prefix]
        with le_col2:    
            le3_cn = st.selectbox("Number", list(df_le3["Code"]), key = "le3_cn")  
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le4_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le4_prefix")
            df_le4 = df[df['Prefix'] == le4_prefix]
        with le_col2:    
            le4_cn = st.selectbox("Number", list(df_le4["Code"]), key = "le4_cn") 
        
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le5_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le5_prefix")
            df_le5 = df[df['Prefix'] == le5_prefix]
        with le_col2:    
            le5_cn = st.selectbox("Number", list(df_le5["Code"]), key = "le5_cn") 
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le6_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le6_prefix")
            df_le6 = df[df['Prefix'] == le6_prefix]
        with le_col2:    
            le6_cn = st.selectbox("Number", list(df_le6["Code"]), key = "le6_cn")   
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le7_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le7_prefix")
            df_le7 = df[df['Prefix'] == le7_prefix]
        with le_col2:    
            le7_cn = st.selectbox("Number", list(df_le7["Code"]), key = "le7_cn")  
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le8_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le8_prefix")
            df_le8 = df[df['Prefix'] == le8_prefix]
        with le_col2:    
            le8_cn = st.selectbox("Number", list(df_le8["Code"]), key = "le8_cn") 
        
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le9_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le9_prefix")
            df_le9 = df[df['Prefix'] == le9_prefix]
        with le_col2:    
            le9_cn = st.selectbox("Number", list(df_le9["Code"]), key = "le9_cn")   
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le10_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le10_prefix")
            df_le10 = df[df['Prefix'] == le10_prefix]
        with le_col2:    
            le10_cn = st.selectbox("Number", list(df_le10["Code"]), key = "le10_cn")  
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le11_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le11_prefix")
            df_le11 = df[df['Prefix'] == le11_prefix]
        with le_col2:    
            le11_cn = st.selectbox("Number", list(df_le11["Code"]), key = "le11_cn") 
        le_col1, le_col2 = st.columns(2)
        with le_col1:
            le12_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "le12_prefix")
            df_le12 = df[df['Prefix'] == le12_prefix]
        with le_col2:    
            le12_cn = st.selectbox("Number", list(df_le12["Code"]), key = "le12_cn") 

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
        le10_credit = df_le10[df_le10["Code"] == le10_cn]["Credit Hours:"]
        le11_credit = df_le11[df_le11["Code"] == le11_cn]["Credit Hours:"]
        le12_credit = df_le12[df_le12["Code"] == le12_cn]["Credit Hours:"]

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
        if le10_prefix == None or le10_cn == None:
            le10_credit = 0
        if le11_prefix == None or le11_cn == None:
            le11_credit = 0
        if le12_prefix == None or le12_cn == None:
            le12_credit = 0
        
        le_credits = le_tc + int(le1_credit) + int(le2_credit) + int(le3_credit) + int(le4_credit) + int(le5_credit) + int(le6_credit) + int(le7_credit) + int(le8_credit) + int(le9_credit) + int(le10_credit) + int(le11_credit) + int(le12_credit)
        st.write("###### Total Lower Division Elective Credits: " + str(le_credits))
    
    # Lower div electives
    with upper_ele_col:
        st.write("### Upper Division Electives (7 Credits)")
        #st.write(uploaded_df)
        if uploaded_file == None:
            ue_tc = st.selectbox("Upper Division Electives Transfer Credits", list(range(0, 76)))
        else:
            ue_tc = st.selectbox("Upper Division Electives Transfer Credits", list(range(0, 76)), index=int(uploaded_df["ue"][0]))
        st.write("Specific Elective Classes")

        # Class 1
        ue_col1, ue_col2 = st.columns(2)
        with ue_col1:
            if uploaded_file == None or (uploaded_file != None and uploaded_df["ue"][1] == ""):
                ue1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ue1_prefix")
            else:
                ue1_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["ue"][1]))), placeholder = "Pick One", key = "ue1_prefix1")
            df_ue1 = df[df['Prefix'] == ue1_prefix]
        with ue_col2:  
            if uploaded_file != None and ue1_prefix == uploaded_df["ue"][1]:  
                ue1_cn = st.selectbox("Number", list(df_ue1["Code"]), key = "ue1_cn", index = int(list(df_ue1["Code"]).index(uploaded_df["ue"][2])))
            else:
                ue1_cn = st.selectbox("Number", list(df_ue1["Code"]), key = "ue1_cn1")
        
        # Class 2
        ue_col1, ue_col2 = st.columns(2)
        with ue_col1:
            if uploaded_file == None or (uploaded_file != None and uploaded_df["ue"][3] == ""):
                ue2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "ue2_prefix")
            else:
                ue2_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["ue"][3]))), placeholder = "Pick One", key = "ue2_prefix1")
            df_ue2 = df[df['Prefix'] == ue2_prefix]
            #st.write(df_ue2)
        with ue_col2: 
            if uploaded_file != None and ue2_prefix == uploaded_df["ue"][3]:
                ue2_cn = st.selectbox("Number", list(df_ue2["Code"]), key = "ue2_cn1", index = int(list(df_ue2["Code"]).index(uploaded_df["ue"][4]))) 
            else:
                ue2_cn = st.selectbox("Number", list(df_ue2["Code"]), key = "ue2_cn") 


        # Find the credit hours for each elective 
        ue1_credit = df_ue1[df_ue1["Code"] == ue1_cn]["Credit Hours:"] 
        ue2_credit = df_ue2[df_ue2["Code"] == ue2_cn]["Credit Hours:"]

        if ue1_prefix == None or ue1_cn == None:
            ue1_credit = 0
        if ue2_prefix == None or ue2_cn == None:
            ue2_credit = 0

        ue_credits = ue_tc + int(ue1_credit) + int(ue2_credit)
        st.write("###### Total Upper Division Elective Credits: " + str(ue_credits))
    


    # Focused elective sequence
    with foc_ele_seq_col:
        st.write("### Focused Elective Sequence (9 Credits)")
        fes_tc = st.selectbox("Focused Elective Sequence Transfer Credits", list(range(0, 76)))
        st.write("Specific Elective Classes")

        # Class 1
        fes_col1, fes_col2 = st.columns(2)
        with fes_col1:
            if uploaded_file == None or (uploaded_file != None and uploaded_df["fes"][1] == ""):
                fes1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "fes1_prefix")
            else:
                fes1_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["fes"][1]))), placeholder = "Pick One", key = "fes1_prefix1")
            df_fes1 = df[df['Prefix'] == fes1_prefix]
            #st.write(df_ue2)
        with fes_col2: 
            if uploaded_file != None and fes1_prefix == uploaded_df["fes"][1]:
                fes1_cn = st.selectbox("Number", list(df_fes1["Code"]), key = "fes1_cn1", index = int(list(df_fes1["Code"]).index(uploaded_df["fes"][2]))) 
            else:
                fes1_cn = st.selectbox("Number", list(df_fes1["Code"]), key = "fes1_cn") 

        # Class 2    
        fes_col1, fes_col2 = st.columns(2)
        with fes_col1:
            if uploaded_file == None or (uploaded_file != None and uploaded_df["fes"][3] == ""):
                fes2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "fes2_prefix")
            else:
                fes2_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["fes"][3]))), placeholder = "Pick One", key = "fes2_prefix1")
            df_fes2 = df[df['Prefix'] == fes2_prefix]
            #st.write(df_ue2)
        with fes_col2: 
            if uploaded_file != None and fes2_prefix == uploaded_df["fes"][3]:
                fes2_cn = st.selectbox("Number", list(df_fes2["Code"]), key = "fes2_cn1", index = int(list(df_fes2["Code"]).index(uploaded_df["fes"][4]))) 
            else:
                fes2_cn = st.selectbox("Number", list(df_fes2["Code"]), key = "fes2_cn") 
        
        # Class 3
        fes_col1, fes_col2 = st.columns(2)
        with fes_col1:
            if uploaded_file == None or (uploaded_file != None and uploaded_df["fes"][5] == ""):
                fes3_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "fes3_prefix")
            else:
                fes3_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["fes"][5]))), placeholder = "Pick One", key = "fes3_prefix1")
            df_fes3 = df[df['Prefix'] == fes3_prefix]
            #st.write(df_ue2)
        with fes_col2: 
            if uploaded_file != None and fes3_prefix == uploaded_df["fes"][5]:
                fes3_cn = st.selectbox("Number", list(df_fes3["Code"]), key = "fes3_cn1", index = int(list(df_fes3["Code"]).index(uploaded_df["fes"][6]))) 
            else:
                fes3_cn = st.selectbox("Number", list(df_fes3["Code"]), key = "fes3_cn") 

        # Find the credit hours for each elective 
        fes1_credit = df_fes1[df_fes1["Code"] == fes1_cn]["Credit Hours:"]
        fes2_credit = df_fes2[df_fes2["Code"] == fes2_cn]["Credit Hours:"]
        fes3_credit = df_fes3[df_fes3["Code"] == fes3_cn]["Credit Hours:"]

        # This is if nothing is chosen then the credits defaults to 0
        if fes1_prefix == None or fes1_cn == None:
            fes1_credit = 0
        if fes2_prefix == None or fes2_cn == None:
            fes2_credit = 0
        if fes3_prefix == None or fes3_cn == None:
            fes3_credit = 0

        fes_credits = fes_tc + int(fes1_credit) + int(fes2_credit) + int(fes3_credit)
        st.write("###### Total Focused Elective Sequence Credits: " + str(fes_credits))

    # Focused electives
    with foc_ele_col:
        st.write("### Focused Electives (7 Credits)")
        fe_tc = st.selectbox("Focused Electives Transfer Credits", list(range(0, 76)))
        st.write("Specific Elective Classes")

        # Class 1
        fe_col1, fe_col2 = st.columns(2)
        with fe_col1:
            if uploaded_file == None or (uploaded_file != None and uploaded_df["fe"][1] == ""):
                fe1_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "fe1_prefix")
            else:
                fe1_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["fe"][1]))), placeholder = "Pick One", key = "fe1_prefix1")
            df_fe1 = df[df['Prefix'] == fe1_prefix]
            #st.write(df_ue2)
        with fe_col2: 
            if uploaded_file != None and fe1_prefix == uploaded_df["fe"][1]:
                fe1_cn = st.selectbox("Number", list(df_fe1["Code"]), key = "fe1_cn1", index = int(list(df_fe1["Code"]).index(uploaded_df["fe"][2]))) 
            else:
                fe1_cn = st.selectbox("Number", list(df_fe1["Code"]), key = "fe1_cn") 

        # Class 2
        fe_col1, fe_col2 = st.columns(2)
        with fe_col1:
            if uploaded_file == None or (uploaded_file != None and uploaded_df["fe"][3] == ""):
                fe2_prefix = st.selectbox("Prefix", list(cp), index = None, placeholder = "Pick One", key = "fe2_prefix")
            else:
                fe2_prefix = st.selectbox("Prefix", list(cp), index = int(list(cp).index(str(uploaded_df["fe"][3]))), placeholder = "Pick One", key = "fe2_prefix1")
            df_fe2 = df[df['Prefix'] == fe2_prefix]
            #st.write(df_ue2)
        with fe_col2: 
            if uploaded_file != None and fe2_prefix == uploaded_df["fe"][3]:
                fe2_cn = st.selectbox("Number", list(df_fe2["Code"]), key = "fe2_cn1", index = int(list(df_fe2["Code"]).index(uploaded_df["fe"][4]))) 
            else:
                fe2_cn = st.selectbox("Number", list(df_fe2["Code"]), key = "fe2_cn") 
    
        # Find the credit hours for each elective 
        fe1_credit = df_fe1[df_fe1["Code"] == fe1_cn]["Credit Hours:"] 
        fe2_credit = df_fe2[df_fe2["Code"] == fe2_cn]["Credit Hours:"]
        

        # This is if nothing is chosen then the credits defaults to 0
        if fe1_prefix == None or fe1_cn == None:
            fe1_credit = 0
        if fe2_prefix == None or fe2_cn == None:
            fe2_credit = 0

        fe_credits = fe_tc + int(fe1_credit) + int(fe2_credit)
        st.write("###### Total Focused Electives Credits: " + str(fe_credits))

# Update credits on the sidebar
st.sidebar.write("#### Total Communication Credits: " + str(com_credits) + " (" + str(18-com_credits) + " needed)")
st.sidebar.write("#### Total Humanities Credits: " + str(hum_credits) + " (" + str(9-hum_credits) + " needed)")
st.sidebar.write("#### Total Social Science Credits: " + str(ss_credits) + " (" + str(12-ss_credits) + " needed)")
st.sidebar.write("#### Total Physics Credits: " + str(phy_credits) + " (" + str(19-phy_credits) + " needed)")
st.sidebar.write("#### Total Math Credits: " + str(math_credits) + " (" + str(64-math_credits) + " needed)")
st.sidebar.write("#### Total Lower Division Elective Credits: " + str(le_credits) + " (" + str(35-le_credits) + " needed)")
st.sidebar.write("#### Total Upper Division Elective Credits: " + str(ue_credits) + " (" + str(7-ue_credits) + " needed)")
st.sidebar.write("#### Total Focused Elective Sequence Credits: " + str(fes_credits) + " (" + str(9-fes_credits) + " needed)")
st.sidebar.write("#### Total Focused Electives Credits: " + str(fe_credits) + " (" + str(7-fe_credits) + " needed)")


with st.expander("Analysis and Download"):
    # Draw the bar graph showing the credits left
    st.write("#### Analyze Credits")
    credits_data = pd.DataFrame(
                    {
                        "Sections" : ["Comm", "Hum", "Soc Sci", "Phy", "Math", "Low Ele", "Upper Ele", "Foc Ele Seq", "Foc Ele"],
                        "Credits Acquired" : [com_credits, hum_credits, ss_credits, phy_credits, math_credits, le_credits, ue_credits, fes_credits, fe_credits],
                        "Credits Needed" : [18-com_credits, 9-hum_credits, 12-ss_credits, 19-phy_credits, 64-math_credits, 35-le_credits, 7-ue_credits, 9-fes_credits, 7-fe_credits]
                    
                    }
                    )  
    st.bar_chart(
        credits_data,
        x="Sections",
        y=["Credits Acquired", "Credits Needed"],
        color=["#35bd59", "#bd4c35"],  # Optional
    )    

    total_credits_acquired = com_credits + hum_credits + ss_credits + phy_credits + math_credits + le_credits + ue_credits + fes_credits + fe_credits
    total_credits_needed = 180 - total_credits_acquired
    st.write("#### Total Credits Acquired - " + str(total_credits_acquired))
    st.write("#### Total Credits Needed - " + str(total_credits_needed))
    st.sidebar.write("## CREDITS - " + str(total_credits_acquired) + "/" + str(180))

    # Creating a data frame to download
    created_data = {"comm" : [com_tc, com111z, spe321, wri121z, com_choice1, com_choice2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "hum" : [hum_tc, hum_ele1_prefix, hum_ele1_cn, hum_ele2_prefix, hum_ele2_cn, hum_ele2_prefix, hum_ele3_cn, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "ss" : [ss_tc, ss_ele1_prefix, ss_ele1_cn, ss_ele2_prefix, ss_ele2_cn, ss_ele3_prefix, ss_ele3_cn, ss_ele4_prefix, ss_ele4_cn, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "phy" : [phy_tc, phy221, phy222, phy223, phy_ele1_prefix, phy_ele1_cn, phy_ele2_prefix, phy_ele2_cn, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "math" : [math_tc, stat201, math251, math252, math253, math254, math310, math321, math322, math341, math346, math354, math421, math451, math_choice1, math_choice2, None, None, None, None, None, None, None, None, None],
                    "le" : [le_tc, le1_prefix, le1_cn, le2_prefix, le2_cn, le3_prefix, le3_cn, le4_prefix, le4_cn, le5_prefix, le5_cn, le6_prefix, le6_cn, le7_prefix, le7_cn, \
                            le8_prefix, le8_cn, le9_prefix, le9_cn, le10_prefix, le10_cn, le11_prefix, le11_cn, le12_prefix, le12_cn],
                    "ue" : [ue_tc, ue1_prefix, ue1_cn, ue2_prefix, ue2_cn, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "fes" : [fes_tc, fes1_prefix, fes1_cn, fes2_prefix, fes2_cn, fes3_prefix, fes3_cn, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                    "fe" : [fe_tc, fe1_prefix, fe1_cn, fe2_prefix, fe2_cn, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]}


    @st.cache_data
    def convert_df(df):
        conv_df = pd.DataFrame(df)
        return conv_df.to_csv(index=False).encode('utf-8')
    conv_csv = convert_df(created_data)

    # Download file
    st.download_button(
        "Download CSV File",
        conv_csv,
        "math_major_advising.csv",
        "text/csv",
        key='download-csv',
        help = 'Download a CSV file for future advising'
    )




   

# uploaded_file = st.sidebar.file_uploader("Choose a CSV file")
# if uploaded_file != None:
#     uploaded_df = pd.read_csv(uploaded_file)
#     st.dataframe(uploaded_df)
#     st.write(uploaded_df["hum"])
# if uploaded_file != None:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

#     uploaded_df = pd.read_csv(uploaded_file)
#     st.dataframe(uploaded_df)

# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

# option_selected = st.sidebar.selectbox("Choose your math option", math_options)
# prefix_selected = st.sidebar.selectbox("Prefix", list(cp))
# df_p = df[df['Prefix'] == prefix_selected]
# #for i in df['Prefix']:
# #st.write(df_p)
# new_df = df[df['Prefix'] == "CST"]
# course_names = new_df['Name'].to_list()

# #print(type(list(cp)))
# #course_prefix = cp.to_list()

# course_selected_prefix = df[df['Prefix'] == prefix_selected]
# course_name = st.sidebar.selectbox("Courses", list(course_selected_prefix['Name']))
# course_number = df_p.loc[df['Name'] == course_name, 'Code']
# st.sidebar.selectbox("Number", list(course_selected_prefix['Code']))
# st.sidebar.header("This is a test of the header")
# #st.write(course_name)
# #print(len(course_number.values))
# #if len(course_number.values) > 0:
#     #st.write("You selected: " + str(course_number.values[0]) + " - " + course_name)
# b1 = st.sidebar.button("This is a button, click it")
# if b1:
#     st.write("You are bad")