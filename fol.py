import pandas as pd 

df = pd.read_excel("actors.xlsx") 

print(df) 

# noOfHits should be more than 40 

# noOfFlops should be less than 8 

# netWorth should be more than $350 million 

# Should be popular 

# Popularity crieteria: 

# awards should be more than 15 

# followers should be more than 40k 

idealBestActor = {'noOfHits': 40, 'noOfFlops':8, 'netWorth':350, 'awards':15, 'followers':40} 

def hits(hits): 
    return hits>idealBestActor['noOfHits'] 

def flops(flops): 
    return flops<idealBestActor['noOfFlops'] 

def networth(networth): 
    return networth>idealBestActor['netWorth'] 

def popularity(awards,followers): 
    return awards>idealBestActor['awards'] and followers>idealBestActor['followers'] 

def algorithm(actor): 

    if hits(actor['Hits']) and flops(actor['Flops']) and networth(actor['NetWorth']) and popularity(actor['NoOfAwards'],actor['NoOfFollowers']): 

        return True 

    return False 

def findBestActor(df): 

    for i in range(len(df)): 

        if algorithm(df.loc[i]): 

            print("{} is the best actor ".format(df.loc[i,"Name"])) 

# print(df.loc[2])
findBestActor(df) 