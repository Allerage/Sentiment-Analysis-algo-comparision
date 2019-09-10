import pandas as pd
def tocsv(review,res,lxsc,pw,nw ):
    lecdic = {

        "Review": review,
        "Result": res,
        "Lexscore": lxsc,
        "Positive Words": pw,
        "Negative Words": nw

    }
    df=pd.DataFrame(lecdic)
    print(df)
    if(res.lower()=="positive"):
        with open("positive.csv", mode="a") as cs:
            df.to_csv(cs, index=False)
    if(res.lower()=="negative"):
        with open("negative.csv", mode="a") as cs:
            df.to_csv(cs, index=False)







