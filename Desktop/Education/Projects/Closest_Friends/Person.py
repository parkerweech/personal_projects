import numpy as np

class Person(object):


    def __init__(self, Name, Extro, Convo, Lead, Argu, Comp):

        self.Name = Name
        self.Extro = Extro
        self.Convo = Convo
        self.Lead = Lead
        self.Argu = Argu
        self.Comp = Comp

    def __repr__(self):

        return "{}:: Extro: {}, Convo: {}, " \
               "Lead: {}, Argu: {}, Comp: {}".format(self.Name, self.Extro,
                                                     self.Convo, self.Lead,
                                                     self.Argu, self.Comp)

    def getFeatures(self):

        features = np.array([self.Extro,self.Convo,self.Lead,self.Argu,self.Comp])
        return features

    def getName(self):
        return self.Name



