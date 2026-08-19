height:int=2
radius:int=2
slant_height=((height**2+radius**2)**0.5)
print(slant_height)
curved_area=(3.14*radius*slant_height)
print(curved_area,"meter square")
volume=(1/3*(3.14)*radius**2*height)
print(volume,"meter cube")
surface_area=(3.14*radius*(radius+slant_height))
print(surface_area,"meter square")
all_measures:str=("slant_height=",slant_height,"curved_area=",curved_area,"volume=",volume,"surface_area=",surface_area)
print("all_measures=",all_measures,)