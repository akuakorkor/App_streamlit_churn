import streamlit as st

# Main application
def main():
    st.title("Welcome to the Customer Churn Prediction App!")

    # Home page content
    st.subheader("Home")
    st.write("Welcome to the app!")
    st.write("""
        This app is designed to help businesses predict customer churn.
        By analyzing customer data, the app identifies patterns and provides insights 
        into the likelihood of a customer discontinuing their service or product usage.

        Using machine learning algorithms, the app can assist businesses in taking 
        proactive measures to retain customers, improve satisfaction, and reduce churn.

        Explore the features and see how customer behavior can be predicted for better decision-making.
    """)


if __name__ == '__main__':
    main()