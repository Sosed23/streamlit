import streamlit as st
import requests

st.title("Shop Bot Banner Management")

# Выбор действия
action = st.sidebar.selectbox("Choose an action", ["Create", "Read One", "Read All", "Update", "Delete"])

if action == "Create":
    st.header("Create a Banner")
    name = st.text_input("Name")
    image = st.text_input("Image URL (optional)")
    description = st.text_area("Description (optional)")

    if st.button("Create Banner"):
        data = {
            "name": name,
            "image": image,
            "description": description
        }
        response = requests.post("http://82.146.40.228:385/banners/", json=data)
        if response.status_code == 200:
            st.success("Banner created successfully!")
        else:
            st.error(f"Failed to create banner. Status code: {response.status_code}")

elif action == "Read One":
    st.header("Read a Banner")
    banner_id = st.number_input("Banner ID", min_value=1)

    if st.button("Get Banner"):
        response = requests.get(f"http://82.146.40.228:385/banners/{banner_id}")
        if response.status_code == 200:
            banner = response.json()
            st.write("Name:", banner["name"])
            st.write("Image:", banner["image"])
            st.write("Description:", banner["description"])
        else:
            st.error(f"Banner not found. Status code: {response.status_code}")

elif action == "Read All":
    st.header("Read All Banners")

    if st.button("Get All Banners"):
        response = requests.get("http://82.146.40.228:385/banners_all/")
        if response.status_code == 200:
            banners = response.json()
            for banner in banners:
                st.write(f"**ID:** {banner['id']} - **Name:** {banner['name']}")
                st.write(f"**Image:** {banner['image']}")
                st.write(f"**Description:** {banner['description']}")
                st.write("---")
        else:
            st.error("Failed to fetch banners.")

elif action == "Update":
    st.header("Update a Banner")
    banner_id = st.number_input("Banner ID to update", min_value=1)
    name = st.text_input("Updated Name")
    image = st.text_input("Updated Image URL (optional)")
    description = st.text_area("Updated Description (optional)")

    if st.button("Update Banner"):
        data = {
            "name": name,
            "image": image,
            "description": description
        }
        response = requests.put(f"http://82.146.40.228:385/banners/{banner_id}", json=data)
        if response.status_code == 200:
            st.success("Banner updated successfully!")
        else:
            st.error(f"Failed to update banner. Status code: {response.status_code}")

elif action == "Delete":
    st.header("Delete a Banner")
    banner_id = st.number_input("Banner ID to delete", min_value=1)

    if st.button("Delete Banner"):
        response = requests.delete(f"http://82.146.40.228:385/banners/{banner_id}")
        if response.status_code == 200:
            st.success("Banner deleted successfully!")
        else:
            st.error(f"Failed to delete banner. Status code: {response.status_code}")
