#Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

#%%writefile app.py

import pandas as pd
import pickle
import streamlit as st


#loading the trained model
pickle_in = open('dct_reg_model.pkl','rb')
predictor = pickle.load(pickle_in)


@st.cache
#defining the function that will make the prediction using the data which the user inputs
def prediction(Store,DayofWeek,Promo,SchoolHoliday,month,year,day,weekofyear,StateHoliday,stateHolidayType):

    index = 0
    
    Store = Store
    if DayofWeek == "Sunday":
        DayofWeek = 1
    elif DayofWeek == "Monday":
        DayofWeek = 2
    elif DayofWeek == "Tuesday":
        DayofWeek = 3
    elif DayofWeek == "Wednsday":
        DayofWeek = 4
    elif DayofWeek == "Thurday":
        DayofWeek = 5
    elif DayofWeek == "Friday":
        DayofWeek = 6
    else:
        DayofWeek = 7
        
    if Promo == "Yes":
        Promo = 1
    else:
        Promo = 0

    if SchoolHoliday == "Yes":
        SchoolHoliday = 1
    else:
        SchoolHoliday = 0
        
    
    month = month

    year = year

    day = day

    weekofyear = weekofyear

    if StateHoliday == "Yes":
        StateHoliday = 1
    else:
        StateHoliday = 0

    if stateHolidayType == "Public Holiday":
        StateHoliday_a = 1
        StateHoliday_b = 0
    elif stateHolidayType == "Easter Holiday":
        StateHoliday_a = 0
        StateHoliday_b = 1
    else:
        StateHoliday_a = 0
        StateHoliday_b = 0

    attr_list = [Store,DayofWeek,Promo,SchoolHoliday,month,year,day,weekofyear,StateHoliday,StateHoliday_a,StateHoliday_b]
    #t =  [0,45,5,1,1,7,2015,31,31,1,0,0]
    df = pd.DataFrame([attr_list])
    #make predictions
    ans = predictor.predict(df)

    return ans



# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Sales Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    
    Store = st.number_input("Store Id",min_value=1,max_value=9000,step=1)
    DayofWeek = st.selectbox('Day of week',("Sunday","Monday","Tuesday","Wednsday","Thurday","Friday","Saturday")) 
    Promo = st.selectbox('Promo',("Yes","No"))
    SchoolHoliday = st.selectbox('SchoolHoliday',("Yes","No"))
    month = st.number_input("Month",min_value=1,max_value=12,step=1)
    year = st.number_input("Year",min_value=2013,max_value=2050,step=1)
    day = st.number_input("Day of month(1-31)",min_value=1,max_value=31,step=1)
    weekofyear = st.number_input("Week of Year",min_value=1,max_value=300,step=1)
    StateHoliday = st.selectbox('StateHoliday',("Yes","No"))
    stateHolidayType = st.selectbox('Is is',("Public Holiday","Easter Holiday",))
    
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"):
        result = prediction(Store,DayofWeek,Promo,SchoolHoliday,month,year,day,weekofyear,StateHoliday,stateHolidayType)
        #result = prediction(Open,Store,Promo,DayofWeek,day,weekofyear,year,StateHoliday,stateHolidayType,SchoolHoliday) 
        #st.success('Your loan is {}'.format(result))
        #print(LoanAmount)
        st.write(result)
if __name__=='__main__': 
    main()

