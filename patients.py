#!/usr/bin/env python
# coding: utf-8

# In[2]:


patients_db = []
next_id = 1


# In[4]:


def add_patient(data):
    global next_id
    patient = {
        "ID": next_id,
        "Name": data.get("name"), 
        "Age": data.get("age"), 
        "Diagnosis": data.get("diagnosis")
    }
    patients_db.append(patient)
    next_id += 1
    return patient


# In[6]:


def delete_patient(patient_id):
    global patients_db
    for p in patients_db:
        if p["ID"] == patient_id:
            patient_db = [q for q in patients_db if q["ID"] != patient_id]
            return {f"Patient{patient_id} has been sucessfully deleted!"}
        return {f"No patient record found!"}


# In[ ]:


get_ipython().system('jupyter nbconvert --to script first_code.ipynb')

