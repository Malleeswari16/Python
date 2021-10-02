# to find the courses.
bio_cut = int(input("Enter the biology cut-off: "))
eng_cut = int(input("Enter the engineering cut-off: "))
biology = (bio_cut/200)*100
engineering = (eng_cut/200)*100
if biology > 60 and engineering > 50:
    if bio_cut > 190:
        print("The bio course available are:\nAgriculture\nBio-tech\n Biology\nzoology\nbotany\n\n")
    if bio_cut > 175:
        print("The bio course available are:\nPhysiotherapy\nNursing\nBio-medical engineering\n\n")
    if eng_cut > 185:
        print('The engineering courses:\nECE\nEEE\nmechanical\nCS\n ')
    else:
        print("Engineering course:\nCivil engineering\nIT\n")
else:
    print("no courses found")
