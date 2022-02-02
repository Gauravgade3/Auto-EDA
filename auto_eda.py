import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)


with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


# Set title
st.title("Exploratory Data Analysis")

# Upload dataset
uploaded_file = st.file_uploader("Upload your csv file", type=["csv", "json"], accept_multiple_files=False)
if not uploaded_file:
  st.stop()
st.success('File Uploaded Successfully!!')
df=pd.read_csv(uploaded_file)

# Show shape
if st.checkbox("Show Shape"):
    st.write(df.shape)

# show dataframe
opt = st.radio("Show Dataframe",('First Ten Rows', 'Last Ten Rows', 'All Rows'))

if opt == 'First Ten Rows':
     st.write(df.head(10))
elif opt == 'Last Ten Rows':
     st.write(df.tail(10))
else:
    st.write(df)


# show summary
if st.checkbox("Show Descriptive Summary"):
    st.write(df.describe())

# show null values
if st.checkbox("Show Null Values"):
    st.write(df.isnull().sum())
###############################################################################

# show data types
col_list=(df.columns.tolist())
lis=[]
for i in (df.columns.tolist()):
    lis.append(df[i].dtype)
if st.checkbox("Show Data Type"):
    st.write(list(zip((col_list),(lis))))
##################################################################################

# Replace the null values
if st.checkbox("Replace Null Values"):
    col_list=(df.columns.to_list())
    for i in col_list:
        if (df[i].dtype)=='float64':
            df[i].fillna(df[i].mean(), inplace=True)

        elif (df[i].dtype)=='object':
            df[i].fillna("Not present", inplace=True)

        elif (df[i].dtype)=='datetime':
            df[i].fillna(df[i].mode(),inplace=True)

        elif (df[i].dtype) == ('int64'):
            df[i].fillna(df[i].mean(),inplace=True)
    st.write(df.isnull().sum())

###################################################################################

# plot the correlation
if st.checkbox("Correlation Plot"):
    corr = df.corr()
    st.write(corr.style.background_gradient(cmap='coolwarm').set_precision(2))

########################################################################################

# plottings
if st.checkbox("Plot"):
    colx, coly= st.columns(2)
    with colx:
        colx = st.selectbox("Select Feature (X-Axis)", (df.columns))
    with coly:
        coly = st.selectbox("Select Feature (Y-Axis)",(df.columns))

    col1, col2, col3 = st.columns(3)

    with col1:
        color1 = st.color_picker('Pick A Color','#00f900')

    with col2:
        st.write("Figure Size")
        number1 = st.number_input('X-Axis',min_value=8)
        number2 = st.number_input('Y-Axis',min_value=4)

    with col3:
        plt_= st.selectbox("Select Plot Type", ('Countplot (Only X-Axis Feature)','Scatter',"Distplot",'Kernel Density Estimation',"Joint Plot","Pair Plot"))

    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    font2 = {'family': 'serif', 'color': 'red', 'size': 20}
    fig = plt.figure(figsize=(number1, number2))


    if plt_=="Scatter":
        plt.scatter(df[colx], df[coly],s=100,c=color1,alpha=0.2)
        plt.title(colx + ' Vs ' + coly, fontdict=font1)
        plt.xlabel(colx, fontdict=font2)
        plt.ylabel(coly, fontdict=font2)
        plt.grid(color='blue', linestyle='--', linewidth=0.2)
        if st.button('Generate Plot'):
            with st.spinner('Wait for it...'):
                time.sleep(5)
                st.pyplot(fig)


    elif plt_=="Countplot (Only X-Axis Feature)":
        sns.countplot(df[colx], palette='bright')
        plt.title(colx + ' Vs ' + "count", fontdict=font1)
        plt.xlabel(colx, fontdict=font2)
        plt.ylabel('count', fontdict=font2)
        plt.grid(color='blue', linestyle='--', linewidth=0.2)
        if st.button('Generate Plot'):
            with st.spinner('Wait for it...'):
                time.sleep(5)
                st.pyplot(fig)



    elif plt_ == "Distplot":
        fi=sns.displot(df, x=colx, hue=coly)
        plt.title(colx + ' Vs ' + coly, fontdict=font1)
        plt.xlabel(colx, fontdict=font2)
        plt.ylabel(coly, fontdict=font2)
        plt.grid(color='blue', linestyle='--', linewidth=0.2)
        if st.button('Generate Plot'):
            with st.spinner('Wait for it...'):
                time.sleep(5)
                st.pyplot(fi)

    elif plt_ == "Kernel Density Estimation":
        fi=sns.displot(df, x=colx, hue=coly, kind="kde", multiple="stack")
        plt.title(colx + ' Vs ' + coly, fontdict=font1)
        plt.xlabel(colx, fontdict=font2)
        plt.ylabel(coly, fontdict=font2)
        plt.grid(color='blue', linestyle='--', linewidth=0.2)
        if st.button('Generate Plot'):
            with st.spinner('Wait for it...'):
                time.sleep(5)
                st.pyplot(fi)

    elif plt_ == "Joint Plot":
        fi=sns.jointplot(data=df, x=colx, y=coly)
        plt.title(colx + ' Vs ' + coly, fontdict=font1)
        plt.xlabel(colx, fontdict=font2)
        plt.ylabel(coly, fontdict=font2)
        plt.grid(color='blue', linestyle='--', linewidth=0.2)
        if st.button('Generate Plot'):
            with st.spinner('Wait for it...'):
                time.sleep(5)
                st.pyplot(fi)


    elif plt_ == "Pair Plot":
        fi=sns.pairplot(df)
        plt.title(colx + ' Vs ' + coly, fontdict=font1)
        plt.xlabel(colx, fontdict=font2)
        plt.ylabel(coly, fontdict=font2)
        plt.grid(color='blue', linestyle='--', linewidth=0.2)
        if st.button('Generate Plot'):
            with st.spinner('Wait for it...'):
                time.sleep(5)
                st.pyplot(fi)


















