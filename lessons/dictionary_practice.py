ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
print("Made my dictionary.")
print(ice_cream)
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else: 
    print("No orders of mint.")
ice_cream.pop("mint")
print(ice_cream)
print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10
print(len(ice_cream))
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else: 
    print("No orders of mint.")

for key in ice_cream:
    print(f"There are {ice_cream[key]} orders of {key}.")
print(ice_cream['mint'])