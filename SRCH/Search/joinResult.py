from typing import List

from .GoogleFetch import GoogleFetch
from .bingFetch import BingFetch
import random

class joinR:

    def merge(self,key):
        obGoogle = GoogleFetch()
        linksGoogle = obGoogle.fetch(key)

        obBing = BingFetch()
        linksBing = obBing.bing(key)
        for i in range(10):
           print(linksGoogle[i])

        print("here")
        for i in range(10):
            print(linksBing[i])

        merge = list()
        mergeOb: List[Results] = list()

        for i in range(10):
            c = random.choice([1,2])
            if(c==1):
                if linksGoogle[i].link not in merge:
                    merge.append(linksGoogle[i].link)
                    mergeOb.append(linksGoogle[i])
                if linksBing[i].link not in merge:
                    merge.append(linksBing[i].link)
                    mergeOb.append(linksBing[i])

            else:
                if linksBing[i].link not in merge:
                    merge.append(linksBing[i].link)
                    mergeOb.append(linksBing[i])
                if linksGoogle[i].link not in merge:
                    merge.append(linksGoogle[i].link)
                    mergeOb.append(linksGoogle[i])

        print("after merge")
        for m in mergeOb:
            print(m.link)
        return mergeOb


ob=joinR()
ob.merge("dog")