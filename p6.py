def update_instagram_ids(user_dict, full_name, new_id):
    if new_id in user_dict.values():
        print("Error: Enter a unique Instagram ID.")
        return False
    user_dict[full_name] = new_id
    print("Instagram ID updated successfully.")
    return True

user_dictionary = {
    'John Doe': 'john_doe123',
    'Jane Smith': 'jane_smith456',
    'Bob Johnson': 'bob_johnson789'
}

full_name_input = input("Enter your full name: ")
new_id_input = input("Enter your new Instagram ID: ")

update_successful = update_instagram_ids(user_dictionary, full_name_input, new_id_input)

if update_successful:
    print("Updated Dictionary:")
    for name, instagram_id in user_dictionary.items():
        print(f"{name}: {instagram_id}")
