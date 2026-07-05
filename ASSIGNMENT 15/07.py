def Length(data):
    if (len(data) > 5):
        return True
    else:
        return False
    
text = ["Ritesh","Aman","Niranjan","Trushita","Mahika","Shreyash","Amogh","Mansi"]

new_data = list(filter(Length,text))
print(new_data)
