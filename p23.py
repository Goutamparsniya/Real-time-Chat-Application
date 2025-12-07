def get_laptop_specifications(laptop_dict, company_name):
    return laptop_dict.get(company_name, "Laptop company not found.")
laptop_specifications = {
    "Dell": "Dell laptops are known for their build quality and performance.",
    "HP": "HP laptops are popular for their reliability and sleek design.",
    "Lenovo": "Lenovo laptops are known for their innovation and durability.",
    "Apple": "Apple laptops, such as MacBook, are known for their premium design and performance."
}
while True:
    company_name = input("Enter the name of the laptop company (or 'exit' to stop): ")
    if company_name.lower() == 'exit':
        break
    specifications = get_laptop_specifications(laptop_specifications, company_name)
    print(specifications)
