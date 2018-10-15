from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd
from Person import Person

# The idea of this kNN project will be to create a group of 10 people with 5 different
# personality traits and figure out which of them will be the most compatible
# The people included with be Parker Weech, Kara Burgoyne, Thomas O'Neill
# , Josh Black, Austin Francis, Cliff Phillips, Michael Da Ponte, Bryan Da Ponte
# , Josh Ledbetter, and Rob Curry
# The five personality traits will be 1. Extroverted, 2. Conversational , 3. Group leader,
# 4. Argumentative, 5. Complimenting
# All personality traits will be given a value between 1-10


Parker = Person(Name='Parker',Extro=6,Convo=6,Lead=6,Argu=5,Comp=4)
Kara = Person(Name='Kara',Extro=4,Convo=4,Lead=3,Argu=3,Comp=6)
Thomas = Person(Name='Thomas',Extro=7,Convo=6,Lead=8,Argu=7,Comp=5)
Black = Person(Name='Black',Extro=7,Convo=7,Lead=6,Argu=8,Comp=6)
Austin = Person(Name='Austin',Extro=4,Convo=5,Lead=2,Argu=5,Comp=5)
Cliff = Person(Name='Cliff',Extro=6,Convo=7,Lead=5,Argu=9,Comp=6)
Michael = Person(Name='Michael',Extro=8,Convo=8,Lead=8,Argu=5,Comp=6)
Bryan = Person(Name='Bryan',Extro=3,Convo=8,Lead=3,Argu=7,Comp=6)
Ledbetter = Person(Name='Ledbetter',Extro=9,Convo=8,Lead=7,Argu=4,Comp=6)
Rob = Person(Name='Rob',Extro=6,Convo=6,Lead=5,Argu=4,Comp=6)

people = np.array([Parker.getFeatures(),Kara.getFeatures(),Thomas.getFeatures(),
                   Black.getFeatures(),Austin.getFeatures(),Cliff.getFeatures(),
                   Michael.getFeatures(),Bryan.getFeatures(),Ledbetter.getFeatures(),
                   Rob.getFeatures()])

nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(people)
names = [Parker.getName(),Kara.getName(),Thomas.getName(),Black.getName(),
         Austin.getName(),Cliff.getName(),Michael.getName(),Bryan.getName(),
         Ledbetter.getName(),Rob.getName()]
distances, indices = nbrs.kneighbors(people)
print(indices)
print(distances)
relationship = nbrs.kneighbors_graph(people).toarray()
relationship_df = pd.DataFrame(data=relationship,index=names,columns=names)
print(relationship_df)

