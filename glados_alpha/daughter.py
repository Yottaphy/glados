from .nucleus import Nucleus, elements

def alphaDaughter(parent, dicNuc):
    if elements[parent.z-2] + str(parent.a-4) in dicNuc.keys():
        return dicNuc[elements[parent.z-2] + str(parent.a-4)]
    else:
        return False
        
def alphaParent(child, dicNuc):
    if elements[child.z+2] + str(child.a+4) in dicNuc.keys():
        return dicNuc[elements[child.z+2] + str(child.a+4)]
    else:
        return False