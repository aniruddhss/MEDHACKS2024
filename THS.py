
def without_openai():
    import streamlit as st
    import pandas as pd

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if 'page' not in st.session_state:
        st.session_state['page'] = 'login'

    def show_login_page():
        st.title("THE HEALTH RESUME")
        st.subheader("LOG-IN")
        name = st.text_input("Enter Name")
        password = st.text_input("Enter Password", type="password")

        if st.button("Login"):
            if name and password:
                st.session_state['logged_in'] = True
                st.session_state['page'] = 'upload'  # Navigate to upload page
                st.success(f"Welcome, {name}!")
            else:
                st.error("Please enter both name and password.")
        st.button("Forgot password?")

    def show_upload_page():
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ["Upload Report", "View Dashboard"])

        if page == "Upload Report":
            st.title("Upload Report")
            st.write("Upload your medical report here.")
            uploaded_file = st.file_uploader("Choose a file")

            if uploaded_file:
                st.session_state['uploaded'] = True
                st.write("File uploaded successfully!")
                if st.button("Save and Analyse"):
                    st.session_state['page'] = 'dashboard'  # Navigate to dashboard

            if st.button("Proceed without Uploading"):
                st.session_state['page'] = 'dashboard'  # Navigate to dashboard

        if page == "View Dashboard":
            st.session_state['page'] = 'dashboard'  # Navigate to dashboard

    def show_dashboard_page():
        st.markdown(
            """
            <style>
            .main .block-container {
                padding-top: 1rem;
                padding-right: 1rem;
                padding-left: 1rem;
                padding-bottom: 1rem;
                max-width: 100%;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.title("Patient Dashboard")

        col1, col2, col3 = st.columns([1, 2, 1])

        # Column 1: Personal Information
        with col1:
            st.header("Personal Information")
            st.write("**Name:** Ankit Tiwari")
            st.write("**Age:** 45")
            st.write("**Gender:** Male")
            st.write("**Blood Type:** O+")

            st.header("Illnesses")
            st.write("- Hypertension")
            st.write("- Type 2 Diabetes")

            st.header("Current Medications")
            st.write("- Metformin 20 mg OD")
            st.write("- Lisinopril 5 MG BD")

            st.header("Allergies")
            st.write("- Penicillin")
            st.write("- Peanuts")

        with col2:
            st.header("Health Reports Over Time")

            # Sample data for the graphs (replace with real data)
            dates = pd.date_range("2023-01-01", periods=12, freq='M')
            blood_pressure = [120, 125, 130, 128, 135, 140, 138, 145, 142, 140, 138, 136]
            glucose_levels = [90, 92, 95, 100, 105, 110, 112, 115, 118, 120, 125, 130]
            cholesterol = [180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235]
            weight = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]

            df_blood_pressure = pd.DataFrame({'Date': dates, 'Blood Pressure': blood_pressure})
            df_glucose_levels = pd.DataFrame({'Date': dates, 'Glucose Levels': glucose_levels})
            df_cholesterol = pd.DataFrame({'Date': dates, 'Cholesterol': cholesterol})
            df_weight = pd.DataFrame({'Date': dates, 'Weight': weight})

            # Display graphs in a 2x2 grid
            col21, col22 = st.columns(2)

            with col21:
                st.subheader("Blood Pressure Over Time")
                st.area_chart(df_blood_pressure.set_index('Date'))

                st.subheader("Glucose Levels Over Time")
                st.bar_chart(df_glucose_levels.set_index('Date'))

            with col22:
                st.subheader("Cholesterol Over Time")
                st.line_chart(df_cholesterol.set_index('Date'))

                st.subheader("Weight Over Time")
                st.vega_lite_chart(df_weight, {
                    'mark': 'point',
                    'encoding': {
                        'x': {'field': 'Date', 'type': 'temporal'},
                        'y': {'field': 'Weight', 'type': 'quantitative'}
                    }
                })

        # Column 3: Key Findings from Latest Report
        with col3:
            st.header("Key Findings from Latest Report")
            st.write("**Date of Report:** August 8, 2024")
            st.write("**Blood Pressure:** 136/85 mmHg")
            st.write("**Glucose Levels:** 130 mg/dL")
            st.write("**Cholesterol:** 235 mg/dL")
            st.write("**Weight:** 81 kg")
            st.write(
                "**Summary:** The patient shows elevated glucose levels and cholesterol, with blood pressure stabilizing but still slightly above the normal range. Continue monitoring and adjust medications as needed.")

    # Main app logic
    if st.session_state['logged_in']:
        if st.session_state['page'] == 'upload':
            show_upload_page()
        elif st.session_state['page'] == 'dashboard':
            show_dashboard_page()
    else:
        show_login_page()


# ----------------------------------------------------------------------------
# def with_openai():
#     import streamlit as st
#     import openai
#     from PIL import Image
#     import io
#
#     # Initialize session states for login status and navigation
#     if 'logged_in' not in st.session_state:
#         st.session_state['logged_in'] = False
#
#     if 'page' not in st.session_state:
#         st.session_state['page'] = 'login'
#
#     if 'report_summary' not in st.session_state:
#         st.session_state['report_summary'] = None
#
#     # Set up OpenAI API key
#     openai.api_key = 'your-openai-api-key'  # Replace with your OpenAI API key
#
#     # Function to analyze report using OpenAI
#     def analyze_report(image_bytes):
#         prompt = ("Analyze the report and summarize it. "
#                   "State the key findings in the summary along with the values of the same.")
#
#         response = openai.Completion.create(
#             engine="text-davinci-003",  # You can change the engine to the latest version if available
#             prompt=prompt,
#             max_tokens=150  # Adjust as necessary
#         )
#
#         summary = response.choices[0].text.strip()
#         return summary
#
#     # Function to show the login page
#     def show_login_page():
#         st.title("THE HEALTH RESUME")
#         st.subheader("LOG-IN")
#         name = st.text_input("Enter Name")
#         password = st.text_input("Enter Password", type="password")
#
#         if st.button("Login"):
#             if name and password:
#                 st.session_state['logged_in'] = True
#                 st.session_state['page'] = 'upload'  # Navigate to upload page
#                 st.success(f"Welcome, {name}!")
#             else:
#                 st.error("Please enter both name and password.")
#         st.button("Forgot Password?")
#
#     # Function to show the upload page
#     def show_upload_page():
#         st.sidebar.title("Navigation")
#         page = st.sidebar.radio("Go to", ["Upload Report", "View Dashboard"])
#
#         if page == "Upload Report":
#             st.title("Upload Report")
#             st.write("Upload your medical report here.")
#             uploaded_file = st.file_uploader("Choose a file", type=['jpg', 'png', 'jpeg', 'pdf'])
#
#             if uploaded_file:
#                 image = Image.open(uploaded_file)
#                 st.image(image, caption="Uploaded Report", use_column_width=True)
#                 image_bytes = io.BytesIO()
#                 image.save(image_bytes, format=image.format)
#                 image_bytes = image_bytes.getvalue()
#
#                 if st.button("Save and Analyse"):
#                     summary = analyze_report(image_bytes)
#                     st.session_state['report_summary'] = summary
#                     st.session_state['page'] = 'dashboard'  # Navigate to dashboard
#
#             if st.button("Proceed without Uploading"):
#                 st.session_state['page'] = 'dashboard'  # Navigate to dashboard
#
#         if page == "View Dashboard":
#             st.session_state['page'] = 'dashboard'  # Navigate to dashboard
#
#     # Function to show the dashboard page
#     def show_dashboard_page():
#         st.markdown(
            #     """
            #     <style>
            #     .main .block-container {
            #         padding-top: 1rem;
            #         padding-right: 1rem;
            #         padding-left: 1rem;
            #         padding-bottom: 1rem;
            #         max-width: 100%;
            #     }
            #     </style>
            #     """,
            #     unsafe_allow_html=True
            # )
            # st.title("Patient Dashboard")
            
            # col1, col2, col3 = st.columns([1, 2, 1])
            
            # # Column 1: Personal Information
            # with col1:
            #     st.header("Personal Information")
            #     st.write("**Name:** Ankit Tiwari")
            #     st.write("**Age:** 45")
            #     st.write("**Gender:** Male")
            #     st.write("**Blood Type:** O+")
            
            #     st.header("Illnesses")
            #     st.write("- Hypertension")
            #     st.write("- Type 2 Diabetes")
            
            #     st.header("Current Medications")
            #     st.write("- Metformin 20 mg OD")
            #     st.write("- Lisinopril 5 MG BD")
            
            #     st.header("Allergies")
            #     st.write("- Penicillin")
            #     st.write("- Peanuts")
            
            # with col2:
            #     st.header("Health Reports Over Time")
            
            #     # Sample data for the graphs (replace with real data)
            #     dates = pd.date_range("2023-01-01", periods=12, freq='M')
            #     blood_pressure = [120, 125, 130, 128, 135, 140, 138, 145, 142, 140, 138, 136]
            #     glucose_levels = [90, 92, 95, 100, 105, 110, 112, 115, 118, 120, 125, 130]
            #     cholesterol = [180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235]
            #     weight = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]
            
            #     df_blood_pressure = pd.DataFrame({'Date': dates, 'Blood Pressure': blood_pressure})
            #     df_glucose_levels = pd.DataFrame({'Date': dates, 'Glucose Levels': glucose_levels})
            #     df_cholesterol = pd.DataFrame({'Date': dates, 'Cholesterol': cholesterol})
            #     df_weight = pd.DataFrame({'Date': dates, 'Weight': weight})
            
            #     # Display graphs in a 2x2 grid
            #     col21, col22 = st.columns(2)
            
            #     with col21:
            #         st.subheader("Blood Pressure Over Time")
            #         st.area_chart(df_blood_pressure.set_index('Date'))
            
            #         st.subheader("Glucose Levels Over Time")
            #         st.bar_chart(df_glucose_levels.set_index('Date'))
            
            #     with col22:
            #         st.subheader("Cholesterol Over Time")
            #         st.line_chart(df_cholesterol.set_index('Date'))
            
            #         st.subheader("Weight Over Time")
            #         st.vega_lite_chart(df_weight, {
            #             'mark': 'point',
            #             'encoding': {
            #                 'x': {'field': 'Date', 'type': 'temporal'},
            #                 'y': {'field': 'Weight', 'type': 'quantitative'}
            #             }
            #         })
            
            # # Column 3: Key Findings from Latest Report
            # with col3:
            #     st.header("Key Findings from Latest Report")
            #     st.write("**Date of Report:** August 8, 2024")
            #     st.write("**Blood Pressure:** 136/85 mmHg")
            #     st.write("**Glucose Levels:** 130 mg/dL")
            #     st.write("**Cholesterol:** 235 mg/dL")
            #     st.write("**Weight:** 81 kg")
            #     st.write(
            #         "**Summary:** The patient shows elevated glucose levels and cholesterol, with blood pressure stabilizing but still slightly above the normal range. Continue monitoring and adjust medications as needed.")


#
#         if st.session_state['report_summary']:
#             st.subheader("Report Summary")
#             st.write(st.session_state['report_summary'])
#
#     # Main app logic
#     if st.session_state['logged_in']:
#         if st.session_state['page'] == 'upload':
#             show_upload_page()
#         elif st.session_state['page'] == 'dashboard':
#             show_dashboard_page()
#     else:
#         show_login_page()
#
# # with_openai()
# ==============================
without_openai()
