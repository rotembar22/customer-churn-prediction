
import streamlit as st
import pandas as pd




st.title('Customer Churn Prediction')
st.markdown("""### Made by: Rotem Bar""")

st.markdown("""




 Dataset Source :

* [GitHub Dataset URL](https://github.com/IBM/telco-customer-churn-on-icp4d/tree/master/data)

You can also : 
* Check the **GitHub Project Repository**   [![](https://img.shields.io/badge/Customer%20Churn%20Prediction-GitHub-100000?logo=github&logoColor=white)](https://github.com/ahmedshahriar/Customer-Churn-Prediction)

* View the Project in **Jupyter Notebook Html**   [![Open in HTML](https://img.shields.io/badge/Html-Open%20Notebook-blue?logo=HTML5)](https://nbviewer.org/github/ahmedshahriar/Customer-Churn-Prediction/blob/main/Telco-Customer-Churn-Prediction.html) 

""")



st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("## Prediction Result")


st.sidebar.markdown("## Predict Customer Churn")





def get_transformed_data(test_data=None):
    pass



def make_prediction(X_test):
    if (X_test.iloc[0].Age < 25):
        return True
    else:
        return False
    





st.sidebar.markdown('## User Input')





def user_input_features():

    # MonthlyCharges slider
    credit_score = st.sidebar.slider("Credit Score", 300, 850, int(300))
    age = st.sidebar.slider("Age", 18, 120, int(18))
    balance = st.sidebar.slider("Balance", 0, 100000, int(0))
    is_germany = st.sidebar.selectbox('Live in Germany', ('Yes', 'No'))
    gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    num_product = st.sidebar.slider("Number of Products", int(1), int(3), int(1), 1)
    is_member = st.sidebar.selectbox('Is Active Member', ('Yes', 'No'))



    def normalize_feature(x,t,z):
        return x
    
    # Churn filter
    data = {'CreditScore': normalize_feature(credit_score, 1, 1),
            'Geography': [1 if is_germany.lower() == 'yes' else 0],
            'Gender': [1 if gender.lower() == 'Male' else 0],
            'Age': normalize_feature(age, 1, 1),
            'Balance': normalize_feature(balance, 1, 1),
            'NumOfProducts': [num_product],
            'IsActiveMember': [1 if is_germany.lower() == 'yes' else 0]
            }


    features = pd.DataFrame(data)

    return features


input_df = user_input_features()






if st.sidebar.button('Predict'):
    test_pred = make_prediction(input_df)
    st.markdown(f"Prediction result : {'**Churned**' if test_pred==True else '**Not Churned**'}  ")
    st.write("User Input Features")
    st.dataframe(input_df)
