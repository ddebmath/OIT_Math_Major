import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Math Major", layout = "wide")
# Load the course list csv file
df = pd.read_csv("pages/course_list_utf.csv")
df = df.reset_index(drop = True)
#cp = df['Prefix'].unique()

st.title("Math Major Advising")
st.write("### ⬅️ Choose your math major option from the left menu")
st.write("### 🚫 Note - Do not click on a different option while doing advising and before downloading your CSV file 🚫")
st.write("### 🚫 Note - Some classes offer variable credit, and it's a little tricky to put them in code. They will show up as 0 credits when if you choose them. Use the respective Transfer Credits to add the number of credits that you would like 🚫. These classes are listed below")

variable_credit_classes = {"Prefix" : ["BIO", "BIO", "MIS", "MIT", "PHM", "PWR", "PWR", "ABA", "PSY", "CST", "BIO", "CHE", "CE", "ENV", "BIO"],
                           "Course Number" : [597, 595, 107, 407, 420, 490, 499, 599, 447, 490, 495, 495, 595, 420, 302]}
# pre = df[df["Prefix"] == "BIO"]
# name = pre[pre["Code"] == "597"]["Name"]

# st.write(name)
# for i in range(len(variable_credit_classes["Prefix"])):
#     prefix = df[df["Prefix"] == variable_credit_classes["Prefix"][i]]
#     #st.write(prefix)
#     name = prefix[prefix["Code"] == str(variable_credit_classes["Course Number"][i])]["Name"]
#     st.write(name)
#     variable_credit_classes["Course Name"].append(name)
#    # st.write(variable_credit_classes["Course Name"][i])

df1 = pd.DataFrame(variable_credit_classes)
#df1.reset_index(drop=True, inplace=True)
st.write(df1)

# Bugs
issue_url = "https://github.com/ddebmath/OIT_Math_Major/issues"
st.write("For any bugs, please create an issue ticket at my [GitHub](%s)" % issue_url)