import streamlit as st
import pandas as pd
import numpy as np

def MVMean(x):
    st.text("Mean Imputer")
    from sklearn.impute import SimpleImputer
    imp = SimpleImputer(missing_values = np.nan, strategy = 'mean')
    imputer = imp.fit(x)
    x = imputer.transform(x)
    return x

def MVMedian(df):
    st.text("Median Imputer")
    from sklearn.impute import SimpleImputer
    imp = SimpleImputer(missing_values = np.nan, strategy = 'median')
    imputer = imp.fit(df)
    df = imputer.transform(df)
    return df

def MVMode(x):
    st.text("Mode Imputer")
    from sklearn.impute import SimpleImputer
    imp = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
    imputer = imp.fit(x)
    x = imputer.transform(x)
    return x

def MVKNN(df):
    st.text("KNN Imputer")
    from sklearn.impute import KNNImputer
    imputer = KNNImputer(n_neighbors = 2)
    df = imputer.fit_transform(df)
    return df

#Outlier
def outlier(df):
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    print(q1,q3)
    iqr = q3 - q1
    df = df[~((df < (q1 - 1.5*iqr)) | (df > (q3 + 1.5*iqr))).any(axis=1)]
    return df

#Standard Scaling
def stdscaler(df):
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    x_std = df
    x_std = sc_x.fit_transform(x_std)
    return x_std
    
#Min Max Scaler
def MinmaxScaler(df):
    from sklearn.preprocessing import MinMaxScaler
    mm_x = MinMaxScaler()
    x_mm = df
    x_mm = mm_x.fit_transform(x_mm)
    return x_mm
    
#Robust
def Robust(df):
    from sklearn.preprocessing import RobustScaler
    rb_x = RobustScaler()
    x_rb = df
    x_rb = rb_x.fit_transform(x_rb)
    return x_rb
    
#Max Absolute
def MaxAbsolute(df):
    from sklearn.preprocessing import MaxAbsScaler
    ma_x = MaxAbsScaler()
    x_ma = df
    x_ma = ma_x.fit_transform(x_ma)
    return x_ma

def Data():
    st.title("DATA PRE-PROCESSING")
    st.sidebar.subheader("Upload the file")
    ff = st.sidebar.radio("Choose the file format", ("Excel","CSV"))
    if ff == "Excel":
            fl_up = st.text_input("Enter your file name", "Type here ..")
            y = pd.read_excel(fl_up)
        
    elif ff == "CSV":
        try:
            fl_up = st.text_input("Enter your file name", "Type here ..")
            y = pd.read_csv(fl_up)
        except:
            st.info("Download the file")
    
    a = 1
    b = 101
    c = 201
    d = 301
    e = 401
    f = 501
    g = 601
    n = 0
    ch6 = st.radio("Do you want to slice the table:", ("Yes","No"),index = 1, key = e)
    if ch6 == "Yes":
        l = len(y.columns) - 1
        st.write(l)
        r1 = st.slider("Choose the range",0,l)
        r2 = st.slider("",0,l)
        y = y.iloc[:,r1:r2]
        st.write(y)
        col = y.columns
    while n<3:
        ch1 = st.radio("Choose an option", ("Missing value", "Outlier", "Feature scaling"),key = a)
        st.write("You selected", ch1)
        if ch1 == "Missing value":
            ch2 = st.selectbox("Select an option", ["Mean", "Median", "Mode", "KNN"],key = b)
            st.write("You selected", ch2)
            if ch2 == "Mean":
                y = MVMean(y)
                y = pd.DataFrame(y)
                st.write(y)
            elif ch2 == "Median":
                y = MVMedian(y)
                st.write(y)
            elif ch2 == "Mode":
                y = MVMode(y)
                st.write(y)
            elif ch2 == "KNN":
                y = MVKNN(y)
                st.write(y)
            n = n + 1
            y = pd.DataFrame(y)
            y.columns = [col]
            st.write(n)
        elif ch1 =="Outlier":
                y = outlier(y)
                st.write(y)
                n = n + 1
                st.write(n)
        else:
            ch3 = st.selectbox("Choose an option", ("Std scaler", "Minmax scaler", "Robust scaler", "Maxabs scaler"),key = c)
            st.write("You selected", ch3)
            if ch3 == "Std scaler":
                y = stdscaler(y)
                st.write(y)
            elif ch3 == "Minmax scaler":
                y = MinmaxScaler(y)
                st.write(y)
            elif ch3 == "Robust scaler":
                y = Robust(y)
                st.write(y)
            elif ch3 == "Maxabs scaler":
                y = MaxAbsolute(y)
                st.write(y)
            n = n + 1
            y = pd.DataFrame(y)
            y.columns = [col]
            st.write(n)

        ch4 = st.radio("Do you want to continue:", ("Yes","No"),index = 1, key = d)
        if ch4 == "Yes":
            if n < 3:
                a = a + 1
                b = b + 1
                c = c + 1
                d = d + 1
            else:
                st.success("Successful all 3 process completed")
                st.sidebar.subheader("Download the file")
                final = st.sidebar.radio("Dowload the output file", ("Excel","CSV"))
                #if final == "Excel":
                    #fl_dw = st.text_input("Enter your file name", "Type here ..")
                    #y.to_excel(fl_dw)
        
                #elif ff == "CSV":
                    #fl_dw = st.text_input("Enter your file name", "Type here ..")
                    #y.to_csv(fl_dw)
        elif (ch4 == "No" and n<3):
            st.warning("Warning, all 3 process not completed")
            ch5 = st.radio("Do you want to continue:", ("Yes","No"),index = 1, key = e)
            if ch5 == "Yes":
                a = a + 1
                b = b + 1
                c = c + 1
                d = d + 1
                e = e + 1
            else:
                break
    final = st.sidebar.radio("Dowload the output file", ("Excel","CSV"))
    if final == "Excel":
        try:
            st.write(y)
            fl_dw = st.text_input("Enter your file name", "Type here ..",key = f)
            y.to_excel(fl_dw)
        except Exception as e:
            st.info(e)
        
    elif ff == "CSV":
        try:
            fl_dw = st.text_input("Enter your file name", "Type here ..",key = g)
            y.to_csv(fl_dw)
        except:
            st.info("Download the file")
#y = pd.read_excel(r'C:\Users\DELL\Desktop\data\Missing value.xlsx')
#y = pd.read_excel(r'C:\Users\DELL\Desktop\data\DemographicData.csv')
#C:\Users\DELL\.spyder-py3
Data()