import os
import streamlit as st
import pandas as pd

# Student information
student_info = """
1,e20211125,AN HENGHENG,M
2,e20210200,BAN BUNRONG,M
3,e20210271,BO SANE,F
4,e20210320,BUN RATNATEPY,F
5,e20211081,CHAN SOPHARA,M
6,e20210871,CHEA PISETH,M
7,e20210742,CHHIN VISAL,M
8,e20211474,CHHON MENGHOUT,M
9,e20210537,CHHORN SOLITA,F
10,e20210294,CHHRAN MOSES,M
11,e20211464,CHOUV YOU Y,F
12,e20211542,CHUM RATANAKCHENTRIA,F
13,e20201096,DEN SOKUNPIDOR,M
14,e20210337,DOK DOMINIQUE,F
15,e20210085,EN SREY TOCH,F
16,e20210084,EN SREYTHOM,F
17,e20210914,ENG SIVE EU,F
18,e20211502,HAYSAVIN RONGRAVIDWIN,M
19,e20210329,HENG SEAKLONG,M
20,e20210931,HENG SOPHANHA,M
21,e20200291,HENGPA VISAL,M
22,e20210954,HUON SITHAI,M
23,e20210603,HUTH SAKDA,M
24,e20210519,ING VITOUROTANAK,M
25,e20210527,KANG PENGKHEANG,M
26,e20211040,KHEM LYHOURT,M
27,e20211015,KHOEM SIVIN,M
28,e20210176,KHON KHENGMENG,M
29,e20211527,KHUN SITHANUT,M
30,e20200497,KONG CHANRAKSA,F
31,e20210963,KONG SATTHA,M
32,e20211537,KONG SEREYRATHA,M
33,e20210574,KOSAL CHANSOTHAY,M
34,e20211754,KOUM SOKNAN,M
35,e20200014,LAB THAVRITH,M
36,e20200413,LENG MOUYHONG,M
37,e20210086,LONG RATANAKVICHEA,M
38,e20210684,LUN CHANPOLY,M
39,e20211077,LY SOKPHENG,M
40,e20210359,MA OUSA,M
41,e20210207,MAK NIMOL,F
42,e20211621,MAO SEDTHA,M
43,e20210249,MORK MONGKUL,M
44,e20210134,NGORN PANHA,M
45,e20210490,NOM MENGHOUY,F
46,e20210635,OEUN PAO,M
47,e20211548,PAV LIMSENG,M
48,e20210072,PEANG RATTANAK,M
49,e20201314,PEL BUNKHLOEM,M
50,e20211572,PEN VIRAK,M
51,e20211154,PHALLY MAKARA,M
52,e20210227,PHAO CHANTHIN,F
53,e20201734,PHENG SOTHEA,M
54,e20210674,PHETH SORIYUON,M
55,e20211543,PHO ROTHA,M
56,e20211748,PHOEUN RAJAME,M
57,e20210823,PHOEURN KIMHOR,M
58,e20211431,PHON PANHALEAK,F
59,e20211037,PHON SREYLEAP,F
60,e20210166,PHORN SREYPOV,F
61,e20210906,PICH DARAPHAL,M
62,e20210057,POV OUGI,M
63,e20200082,POV RATHNA,F
64,e20210513,PROM BUNRONG,M
65,e20210369,PRUONH KIMLIYA,F
66,e20210511,PUM CHAMNAN,M
67,e20210533,RA VEASNA,M
68,e20200719,RATH PHIREAK,M
69,e20211364,RITH SEAVLAV,F
70,e20210964,RO LANGHENG,F
71,e20211022,ROEUN SOVANDETH,M
72,e20210367,ROEURN RITH,M
73,e20210994,ROS SREYNEATH,F
74,e20210323,SAN KIMHEANG,M
75,e20210929,SEK SOMUNINEATH,F
76,e20210254,SEK SOPHEAK VOATEI,F
77,e20211096,SEM YUTHEARYLYHOUR,M
78,e20211734,SIV LYHENG,M
79,e20210280,SOK SREYPOV,F
80,e20210535,SOL VISAL,M
81,e20210832,SORN ALY,F
82,e20210292,SORN SREYNATT,F
83,e20211557,SROEM SOKUNTHY,F
84,e20210629,SRUN KIMLANG,F
85,e20211737,SUN SOKUNTHEARY,F
86,e20210226,SUON SENCHEY,M
87,e20210872,TAING THAITHEANG,M
88,e20200711,THONG CHHUNHER,M
89,e20200643,THONG OUSAPHEA,F
90,e20210220,THY CHANTHA,M
91,e20210845,TON CHAMNAN,F
92,e20210275,TY KANA,M
93,e20200496,UCH MENGLY,M
94,e20210586,VA SEYHA,M
95,e20211043,VANG ROZA,F
96,e20210836,VANNA JUUKA,F
97,e20210095,VENG MENGSOKLIN,F
98,e20210708,VEY SREYPICH,F
99,e20211405,VEY THIDA,F
100,e20210131,VIN SREYMOM,F
101,e20210599,VONG PISEY,F
102,e20211478,VORN SEAVMEY,F
103,e20210138,YIN SAMBAT,M
"""
# Parse the provided student information into a DataFrame
student_data = [line.split(",") for line in student_info.strip().split("\n")]
df_students = pd.DataFrame(student_data, columns=[
                           "Index", "ID", "Name", "Gender"])
df_students.index = df_students.index + 1  # Adjust index to start from 1
# Initialize all students as absent
df_students["Attendance Status"] = "Absence"

# Cache the DataFrame to improve app performance
# Define a function to save the DataFrame to a CSV file


def save_df_to_csv(df, file_name):
    df.to_csv(file_name, index=False)

# Define a function to load the DataFrame from a CSV file


def load_df_from_csv(file_name):
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    else:
        # If the file doesn't exist, initialize the DataFrame with default data
        return pd.DataFrame(student_data, columns=["Index", "ID", "Name", "Gender"])
# Define a function to reset the attendance status


def reset_table(file_name):
    df = load_df_from_csv(file_name)
    df["Attendance Status"] = "Absence"
    save_df_to_csv(df, file_name)
# Main function for the Streamlit app


def main():
    # Set the file name where the DataFrame is saved
    file_name = 'student_attendance.csv'
    # Load student DataFrame from CSV file
    df_students = load_df_from_csv(file_name)
    df_students.index = df_students.index + 1
    # Set page configuration and title
    st.set_page_config(layout="wide")
    st.markdown("<h1 style='font-size:30px;'>Department of Applied Mathematics and Statistics</h1>",
                unsafe_allow_html=True)
    st.markdown("<h1 style='font-size:25px;'>Student Attendance System</h1>",
                unsafe_allow_html=True)

    # Sidebar for Reset Attendance and Select Your Name
    with st.sidebar:
        st.subheader("Reset Attendance")
        password = st.text_input(
            "Enter the password to reset attendance:", type="password")
        if st.button("Reset Attendance"):
            if password == "Dec061204P@ssword":
                reset_table(file_name)
                st.success("Attendance has been reset.")
            else:
                st.error("Incorrect password.")

        st.subheader("Select Your Name")
        name_query = st.text_input("Search your name here:")
        filtered_names = df_students[df_students["Name"].str.contains(
            name_query, case=False)]["Name"]
        selected_name = st.selectbox(
            "Or Select your name here:", options=filtered_names)
        if selected_name:
            student_id = df_students[df_students["Name"]
                                     == selected_name]["ID"].iloc[0]
            st.text_input("Student ID:", value=student_id, disabled=False)

        if st.button("Submit Attendance"):
            if selected_name:
                df_students.loc[df_students["Name"] ==
                                selected_name, "Attendance Status"] = "Present"
                save_df_to_csv(df_students, file_name)
                st.success(
                    f"Attendance submitted successfully for {selected_name}.")
                st.balloons()

    # Display student list
    st.subheader("Student List")
    st.table(df_students[["Name", "ID", "Attendance Status"]].style.applymap(
        lambda x: 'color: red' if x.strip() == 'Absence' else 'color: blue'))

    # Add credit information
    st.markdown("---")
    st.write("Project Holder by: OEUN PAO")
    st.write("Student of Department of Applied Mathematics and Statistics, ITC")


if __name__ == "__main__":
    main()
