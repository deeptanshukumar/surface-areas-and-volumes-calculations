import math

type_of_equation = input('''which equation:
working on cubes or cuboid? -> 'cubd' 
working on cylinders? -> 'cylinder'
working on cones? -> 'cone'
working on spheres? -> 'sphr'
documentations -> 'doc'
> ''')
while True:
    if type_of_equation.lower() == 'cubd':
        volume_or_tsa_or_lsa = input("""volume ->('volume') 
total surface area ->('tsa') 
lateral surface area ->('lsa')
>""")
        if volume_or_tsa_or_lsa.lower() == 'tsa':
            try:
                length = float(input('length: '))
                breadth = float(input('breadth: '))
                height = float(input('height: '))
                total_surface_area = 2 * \
                    ((length*breadth)+(length*height)+(breadth*height))
                print(total_surface_area)
                break
            except ValueError:
                print('please enter numbers only!!')
        elif volume_or_tsa_or_lsa.lower() == 'lsa':
            inclusion = input("including base or top? 'yes' or 'no': ")
            if inclusion.lower() == 'yes':
                try:
                    length = float(input('length: '))
                    breadth = float(input('breadth: '))
                    height = float(input('height: '))
                    included_base_or_top_lateral_surface_area = 2 * \
                        (length+breadth)*height + length*breadth
                    print(included_base_or_top_lateral_surface_area)
                    break
                except ValueError:
                    print('please enter numbers only!!')
            elif inclusion.lower() == 'no':
                try:
                    length = float(input('length: '))
                    breadth = float(input('breadth: '))
                    height = float(input('height: '))
                    lateral_surface_area = 2*(length+breadth)*height
                    print(lateral_surface_area)
                    break
                except ValueError:
                    print('please enter numbers only!!')
                    volume_or_tsa_or_lsa = input("""volume ->('volume') 
total surface area ->('tsa') 
lateral surface area ->('lsa')
>""")
            else:
                print('please enter "yes" or "no" only! ')
                inclusion = input("including base or top? 'yes' or 'no': ")
        elif volume_or_tsa_or_lsa.lower() == 'volume':
            try:
                length = float(input('length: '))
                breadth = float(input('breadth: '))
                height = float(input('height: '))
                volume = length*breadth*height
                print(volume)
                break
            except ValueError:
                print('please enter numbers only!!')
        else:
            print("please enter 'volume' or 'tsa' or 'lsa' only")

    elif type_of_equation.lower() == 'cylinder':
        type_of_working = input('''lateral surface area -> 'lsa' 
total surface area -> 'tsa'
volume -> 'volume'
working with total volume of a hollow pipe? -> pipe
> ''')
        if type_of_working.lower() == 'lsa':
            inclusion = input("including base or top? 'yes' or 'no': ")
            if inclusion.lower() == 'yes':
                try:
                    radius = float(input('radius: '))
                    height = float(input('height: '))
                    lsa = 2*(22/7)*radius*height + math.pi*(radius**2)
                    print(lsa)
                    break
                except ValueError:
                    print('please enter numbers only!!')
            elif inclusion.lower() == 'no':
                try:
                    radius = float(input('radius: '))
                    height = float(input('height: '))
                    lsa = 2*(22/7)*radius*height
                    print(lsa)
                    break
                except ValueError:
                    print('please enter numbers only!!')
            else:
                print('please enter "yes" or "no" only! ')
                inclusion = input("including base or top? 'yes' or 'no': ")
        elif type_of_working.lower() == 'tsa':
            try:
                radius = float(input('radius: '))
                height = float(input('height: '))
                tsa = 2*(22/7)*radius*(radius+height)
                print(tsa)
                break
            except ValueError:
                print('please enter numbers only!!')
        elif type_of_working.lower() == 'volume':
            try:
                radius = float(input('radius: '))
                height = float(input('height: '))
                volume = (22/7)*(radius**2)*height
                print(volume)
                break
            except ValueError:
                print('please enter numbers only!!')
        elif type_of_working.lower() == 'pipe':
            try:
                print("inner cylinder properties :")
                inner_radius = float(input('inner radius: '))
                inner_height = float(input('inner_height: '))
                print("outer cylinder properties :")
                outer_radius = float(input('outer radius: '))
                outer_height = float(input('outer height: '))

                inner_volume = (22/7)*(inner_radius**2)*inner_height
                outer_volume = (22/7)*(outer_radius**2)*outer_height
                total_volume = outer_volume - inner_volume
                print(total_volume)
                break
            except ValueError:
                print('please enter numbers only!!')
        else:
            print('sry please enter exact wordings!')
            type_of_working = input('''lateral surface area -> 'lsa' 
total surface area -> 'tsa'
volume -> 'volume'
working with total volume of a hollow pipe? -> pipe
> ''')
    elif type_of_equation.lower() == 'quit':
        break
    elif type_of_equation.lower() == 'cone':
        lsa_or_tsa_or_volume = input("""lateral surface area ->'lsa'
total surface area -> 'tsa'
volume -> 'volume' : """)
        if lsa_or_tsa_or_volume.lower() == 'lsa':
            slant_length_or_height_or_radius = input("""if slant length is given->('sl') 
if height is given ->('h') 
if radius is not given ->('r'): """)
            if slant_length_or_height_or_radius.lower() == 'sl':
                try:
                    slant_length = float(input('slant length: '))
                    radius = float(input('radius: '))
                    lateral_surface_area_of_cone = (22/7)*radius*slant_length
                    print(lateral_surface_area_of_cone)
                    break
                except ValueError:
                    print('please enter only numeric values!')
            elif slant_length_or_height_or_radius.lower() == 'h':
                try:
                    height = float(input('height: '))
                    radius = float(input('radius: '))
                    lateral_surface_area_of_cone = (
                        22/7)*radius*(math.sqrt((height**2) + (radius**2)))
                    print(lateral_surface_area_of_cone)
                    break
                except ValueError:
                    print('please enter only numeric values!')
            elif slant_length_or_height_or_radius.lower() == 'r':
                try:
                    height = float(input('height: '))
                    slant_length = float(input('slant length: '))
                    radius = math.sqrt((slant_length**2)-(height**2))
                    lateral_surface_area_of_cone = (22/7)*radius*slant_length
                    print(lateral_surface_area_of_cone)
                    break
                except ValueError:
                    print('please enter only numeric values!')
            else:
                print("please enter only 'sl' or 'h' or 'r'")
                slant_length_or_height_or_radius = input("""if slant length is given->('sl') 
if height is given ->('h') 
if radius is not given ->('r'): """)
        elif lsa_or_tsa_or_volume.lower() == 'tsa':
            slant_length_or_height_or_radius = input("""if slant length is given->('sl') 
if height is given ->('h') 
if radius is not given ->('r'): """)
            if slant_length_or_height_or_radius.lower() == 'sl':
                try:
                    slant_length = float(input('slant length: '))
                    radius = float(input('radius: '))
                    total_surface_area_of_cone = (
                        22/7)*radius*(slant_length + radius)
                    print(total_surface_area_of_cone)
                    break
                except ValueError:
                    print('please enter only numeric values!')
            elif slant_length_or_height_or_radius.lower() == 'h':
                try:
                    height = float(input('height: '))
                    radius = float(input('radius: '))
                    total_surface_area_of_cone = (
                        22/7)*radius*(radius + math.sqrt((radius**2) + (height**2)))
                    print(total_surface_area_of_cone)
                    break
                except ValueError:
                    print('please enter only numeric values!')
            elif slant_length_or_height_or_radius.lower() == 'r':
                try:
                    height = float(input('height: '))
                    slant_length = float(input('slant length: '))
                    radius = math.sqrt((slant_length**2)-(height**2))
                    lateral_surface_area_of_cone = (
                        22/7)*radius*(radius + slant_length)
                    print(lateral_surface_area_of_cone)
                    break
                except ValueError:
                    print('please enter only numeric values!')
            else:
                print("please enter only 'sl' or 'h' or 'r'")
                slant_length_or_height_or_radius = input("""if slant length is given->('sl') 
if height is given ->('h') 
if radius is not given ->('r'): """)
        elif lsa_or_tsa_or_volume.lower() == 'volume':
            slant_length_given = input(
                "is slant length given? ('yes' or 'no') :")
            if slant_length_given.lower() == 'yes':
                radius_or_height = input(
                    "which of the following isn't given -> 'r' or 'h'")
                if radius_or_height.lower() == 'r':
                    try:
                        height = float(input('height: '))
                        slant_length = float(input('slant length: '))
                        radius = math.sqrt((slant_length**2)-(height**2))
                        volume_of_cone = (22/7)*(radius**2)*(height/3)
                        print(volume_of_cone)
                        break
                    except ValueError:
                        print('please enter only numeric values!')
                if radius_or_height.lower() == 'h':
                    try:
                        slant_length = float(input('slant length: '))
                        radius = float(input('radius: '))
                        height = math.sqrt((slant_length**2)-(radius**2))
                        volume_of_cone = (22/7)*(radius**2)*(height/3)
                        print(volume_of_cone)
                        break
                    except ValueError:
                        print('please enter only numeric values!')
                else:
                    print("please enter 'r' or 'h' only!")
                    radius_or_height = input(
                        "which of the following isn't given -> 'r' or 'h'")

            if slant_length_given.lower() == 'no':
                try:
                    height = float(input('height: '))
                    radius = float(input('radius: '))
                    volume_of_cone = (22/7)*(radius**2)*(height/3)
                    print(volume_of_cone)
                    break
                except ValueError:
                    print('please enter only numeric values!')
            else:
                print("please enter 'yes' or 'no' only!")
                slant_length_given = input(
                    "is slant length given? ('yes' or 'no') :")
        else:
            print("please enter 'tsa' or 'lsa' or 'volume' only!")
            lsa_or_tsa_or_volume = input("""lateral surface area ->'lsa'
total surface area -> 'tsa'
volume -> 'volume' : """)
    elif type_of_equation.lower() == 'sphr':
        type_of_working = input("""surface area -> 'sa'
volume -> 'volume'
working on hemispheres? -> 'hemis'
working on questions with hollow sphere and to find the 
    volume of the thick material or any related? -> 'tcv' 
: """)
        if type_of_working.lower() == "sa":
            try:
                radius = float(input('radius: '))
                sa_of_sphere = 4*(22/7)*(radius**2)
                print(sa_of_sphere)
                break
            except ValueError:
                print('please enter numeric values only!')
        elif type_of_working.lower() == 'volume':
            try:
                radius = float(input('radius: '))
                volume_of_sphere = (4/3)*(22/7)*(radius**3)
                print(volume_of_sphere)
                break
            except ValueError:
                print('please enter numeric values only!')
        elif type_of_working.lower() == 'hemis':
            lsa_or_tsa_or_volume = input("""visible surface area -> 'lsa'
total surface area -> 'tsa'
volume -> 'volume'
working on questions with hollow hemisphere and to find the 
    volume of the thick material or any related? -> 'hhemis'
:""")
            if lsa_or_tsa_or_volume.lower() == 'lsa':
                try:
                    radius = float(input('radius: '))
                    lsa_of_hemisphr = 4*(22/7)*(radius**2)
                    print(lsa_of_hemisphr)
                    break
                except ValueError:
                    print("please enter numeric values only!")
            elif lsa_or_tsa_or_volume.lower() == 'tsa':
                try:
                    radius = float(input('radius: '))
                    tsa_of_hemisphr = 4*(22/7)*(radius**2)+((22/7)*(radius**2))
                    print(tsa_of_hemisphr)
                    break
                except ValueError:
                    print("please enter numeric values only!")
            elif lsa_or_tsa_or_volume.lower() == 'volume':
                try:
                    radius = float(input('radius: '))
                    volume_of_hemisphere = (
                        4 / 3) * (22 / 7) * (radius ** 3) * (1/2)
                    print(volume_of_hemisphere)
                    break
                except ValueError:
                    print('please enter numeric values only!')
            elif lsa_or_tsa_or_volume.lower() == 'hhemis':
                try:
                    inner_radius = float(input('inner radius: '))
                    outer_radius = float(input('outer radius: '))
                    inner_volume = (4 / 3) * (22 / 7) * \
                        (inner_radius ** 3) * (1/2)
                    outer_volume = (4 / 3) * (22 / 7) * \
                        (outer_radius ** 3) * (1/2)
                    total_volume = outer_volume - inner_volume
                    print(total_volume)
                    break
                except ValueError:
                    print("please enter numeric values only!!")
            else:
                print("please enter 'lsa' or 'tsa' or 'volume' or 'hhemis' only!!")
                lsa_or_tsa_or_volume = input("""visible surface area -> 'lsa'
total surface area -> 'tsa'
volume -> 'volume'
working on questions with hollow hemisphere and to find the 
    volume of the thick material or any related? -> 'hhemis'
:""")
        elif type_of_working.lower() == 'tcv':
            try:
                inner_radius = float(input('inner radius: '))
                outer_radius = float(input('outer radius: '))
                inner_volume = (4/3)*(22/7)*(inner_radius**3)
                outer_volume = (4/3)*(22/7)*(outer_radius**3)
                total_volume = outer_volume - inner_volume
                print(total_volume)
                break
            except ValueError:
                print("please enter numeric values only!!")
        else:
            print("please enter 'sa' or 'volume' or 'hemis' or 'tcv' only!!")
            type_of_working = input("""surface area -> 'sa'
volume -> 'volume'
working on hemispheres? -> 'hemis'
working on questions with hollow sphere and to find the 
    volume of the thick material or any related? -> 'tcv' 
: """)
    elif type_of_equation.lower() == 'doc':
        print("""
this program helps you find:
cubes and cuboids :
    - volume
    - lateral surface area
    - total surface area
cylinders : 
    - lateral surface area
    - total surface area
    - volume
    - the total volume of a thick cylinderical container
cone :
    - lateral surface area
    - total surface area
    - volume
sphere :
    - surface area
    - volume
    - hemisphere
        - visible surface area
        - total surface area
        - hemisphere volume
- this program also doesn't crash on any work done by the user
- author: deeptanshu kumar
- code lines: 403""")
        break
    else:
        print('sry please enter exact wordings!')
        type_of_equation = input('''which equation:
working on cubes or cuboid? -> 'cubd' 
working on cylinders? -> 'cylinder'
working on cones? -> 'cone'
working on spheres? -> 'sphr'
documentations -> 'doc
> ''')
