import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    # FIRST GRAPH (Field of Study Vs Opinion on Reliability of ChatGPT)

    # Creates figure and changes figure size 
    plt.figure(1,figsize=(12, 6))

    # df is set to the excel file read into pandas dataframe 
    df = pd.read_excel('ChatGPT Survey (Responses).xlsx', sheet_name = 'Form Responses 1')

    # groups the data in the row "What's your field of study" and returns the mean values of the different groups, held in DataFrame variable pivot
    pivot = df.groupby("What's your field of study?").mean(numeric_only = True)

    # Creates a variable field_and_reliability which extracts all "What's your field of study?" data associated with index "How reliable do you believe ChatGPT is?" 
    field_and_reliability = pivot.loc[:, "How reliable do you believe ChatGPT is?"]

    # Plots the data as a bar graph
    field_and_reliability.plot(kind="bar")

    # Creates the font for the labels 
    font1 = {'family':'times new roman','color':'black','size':14}

    # Sets each of the labels and the title of the graph
    plt.xlabel("Field of Study", font1)
    plt.ylabel("Reliability (5 point scale)", font1)
    plt.title("Field Of Study Vs Reliabilty of ChatGPT", font1)

    # Sets the y scale to go from 0 to 5
    plt.ylim(0,5)

    # Adjusts the graph to fit correctly 
    plt.subplots_adjust(bottom=0.514)
    plt.subplots_adjust(top=0.943)


    # SECOND GRAPH (Field of Study Vs If ChatGPT is plagiarism)

    # Creates figure and changes figure size 
    plt.figure(2,figsize=(12, 7))

    #  Creates a variable field_and_plagiarism which extracts all "What's your field of study?" data associated with index "Agree or Disagree: ChatGPT is a form of plagiarism."
    field_and_plagiarism = pivot.loc[:, "Agree or Disagree: ChatGPT is a form of plagiarism."] 

    # Plots the data as a bar graph
    field_and_plagiarism.plot(kind="bar", color="magenta")

    # Sets each of the labels and the title of the graph
    plt.xlabel("Field of Study", font1)
    plt.ylabel("Opinion on ChatGPT Plagiarism (5 point scale)", font1)
    plt.title("Field Of Study Vs Opinion on ChatGPT Plagiarism", font1)

    # Sets the y scale to go from 0 to 5
    plt.ylim(0,5)

    # Adjusts the graph to fit correctly 
    plt.subplots_adjust(bottom=0.438)
    plt.subplots_adjust(top=0.943)


    # THIRD GRAPH (Reliability vs If ChatGPT is plagiarism)
    # THIS GRAPH WAS NOT USED IN THE REPORT TO KEEP REPORT CONSISE

    # Creates figure and changes figure size 
    plt.figure(3,figsize=(12, 6))

    # groups the data in the row "How reliable do you believe ChatGPT is?" and returns the mean values of the different groups, held in DataFrame variable pivot
    pivot = df.groupby("How reliable do you believe ChatGPT is?").mean(numeric_only = True)

    # Creates a variable reliability_and_plagiarism which extracts all "How reliable do you believe ChatGPT is?" data associated with index "Agree or Disagree: ChatGPT is a form of plagiarism." 
    reliability_and_plagiarism = pivot.loc[:, "Agree or Disagree: ChatGPT is a form of plagiarism."] 

    # Plots the data as a bar graph
    reliability_and_plagiarism.plot(kind="bar", color="red")

    # Sets each of the labels and the title of the graph
    plt.xlabel("Reliability (5 point scale)", font1)
    plt.ylabel("Opinion on ChatGPT Plagiarism (5 point scale)", font1)
    plt.title("Reliability Vs Opinion on ChatGPT Plagiarism", font1)

    # Sets the y scale to go from 0 to 5
    plt.ylim(0,5)


    # FOURTH GRAPH (Opinion on Effect in Education vs Should be Allowed in Education)

    # Creates figure and changes figure size    
    plt.figure(4,figsize=(10, 5))

    # groups the data in the row "Should AI Tools such as ChatGPT be allowed to be utilized in education?" and returns the mean values of the different groups, held in DataFrame variable pivot
    pivot = df.groupby("Should AI Tools such as ChatGPT be allowed to be utilized in education?").mean(numeric_only = True)

    # Creates a variable Allowed_and_Effect which extracts all "Should AI Tools such as ChatGPT be allowed to be utilized in education?" data associated with index "What effect do you think ChatGPT will have on education?" 
    Allowed_and_Effect = pivot.loc[:, "What effect do you think ChatGPT will have on education?"] 

    # Plots the data as a horizontal bar graph
    Allowed_and_Effect.plot(kind="barh", color="yellow")

    # Sets each of the labels and the title of the graph
    plt.ylabel("Should ChatGPT be Allowed in Education", font1)
    plt.xlabel("Opinion on Effect on Education (5 point scale)", font1)
    plt.title("Opinion on Effect in Education Vs Should be Allowed in Education", font1)

    # Sets the x scale to go from 0 to 5
    plt.xlim(0,5)

    # Adjusts the graph to fit correctly 
    plt.subplots_adjust(left=0.276)
    plt.subplots_adjust(right=0.95)


    # FIFTH GRAPH (Does ChatGPT Give an Unfair Advantage vs Opinion on Effect in Education)
    # THIS GRAPH WAS NOT USED IN THE REPORT TO KEEP REPORT CONSISE

    # Creates figure and changes figure size 
    plt.figure(5,figsize=(12, 6))

    # groups the data in the row "Do you think AI Tools like ChatGPT give an unfair advantage to students?" and returns the mean values of the different groups, held in DataFrame variable pivot
    pivot = df.groupby("Do you think AI Tools like ChatGPT give an unfair advantage to students?").mean(numeric_only = True)

    # Creates a variable Advantage_and_Effect which extracts all "Do you think AI Tools like ChatGPT give an unfair advantage to students?" data associated with index "What effect do you think ChatGPT will have on education?" 
    Advantage_and_Effect = pivot.loc[:, "What effect do you think ChatGPT will have on education?"] 

    # Plots the data as a bar graph
    Advantage_and_Effect.plot(kind="bar", color="pink")

    # Sets each of the labels and the title of the graph
    plt.xlabel("Does ChatGPT Give Unfair Advantage?", font1)
    plt.ylabel("Opinion on Effect on Education (5 point scale)", font1)
    plt.title("Does ChatGPT Give Unfair Advantage Vs Opinion on Effect in Education", font1)

    # Sets the y scale to go from 0 to 5
    plt.ylim(0,5)

    # Adjusts the graph to fit correctly 
    plt.subplots_adjust(bottom=0.154)
    plt.subplots_adjust(top=0.935)

    # Shows all five of the graphs to the screen
    plt.show()
