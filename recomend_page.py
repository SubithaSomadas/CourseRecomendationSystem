import streamlit as st
import pickle
import pandas as pd
from PIL import Image


# Load necessary data
courses_list = pickle.load(open('courses.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = [courses_list.iloc[i[0]].course_name for i in distances[1:11]]
    return recommended_course_names

def main():    
    st.markdown("<h2 style='text-align: center; color: Orange;'>Course Recommendation System</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Web Page created by Subitha Somadas</h4>", unsafe_allow_html=True)

    selected_course = st.selectbox("Search the topic :", courses_list['course_name'])
    selected_number = st.number_input("Enter a number: ", min_value=1, max_value=10, step=1)

    if st.button('Recommended Courses'):
        st.subheader("Recommended Courses based on your interests are :")
        
        recommended_course_names = recommend(selected_course)
        for i in range(selected_number):
            st.text(recommended_course_names[i])    
        

if __name__ == "__main__":
    main()
