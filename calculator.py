import streamlit as st
st.title('Calculator App')
num1=st.number_input("Enter First Number :")
num2=st.number_input("Enter Second Number : ")

operation=st.selectbox(
    "Choose the operation to perform",
    ("Add","Subtract","Multiply","Divide","Power","Modulus"),
)

# Operation logic

if operation=="Add":
    result= num1 + num2
elif operation=="Subtract":
    result= num1 - num2
elif operation=="Multiply":
    result= num1 * num2
elif operation=="Divide":
    if num2 != 0:
        result= num1/num2
    else:
        "Error ! divison by zer0"    
elif operation=="Power":
    result= num1**num2
elif operation== "Modulus":
    result =num1 % num2                    

#disply the result    
st.write("Result",result)