NULL = None
HEAP_ALL = "HEAP_ALL"
REGISTER_ALL = "REGISTER_ALL"

MR0 = "MR0"
MR1 = "MR1"
MR2 = "MR2"
MR3 = "MR3"
RR = "RR"

REGISTER_NAMES = ["MR0","MR1","MR2","MR3","RR"]

__RegisterData = {"MR0":NULL,"MR1":NULL,"MR2":NULL,"MR3":NULL,"RR":NULL}
__HeapData = {}
HeapLabel = []


#--------------------Exceptions--------------------
class Type_Error(Exception):
    pass

class Label_Not_Found(Exception):
    pass

class Register_Not_Found(Exception):
    pass

class Only_For_Reading(Exception):
    pass


#-------------------------Memory(Heap)-------------------------
def SetHeapData(Label, Data):
    if Label in HeapLabel:
        pass
    else:
        HeapLabel.append(Label)
        __HeapData[Label] = Data
    

def GetHeapData(Label):
    if Label in HeapLabel:
        return __HeapData.get(Label)
    else:
        raise Label_Not_Found(str(Label)+" not found!!!")


#-------------------------Memory(Register)-------------------------
def SetRegisterData(Register, Data):
    if Register in REGISTER_NAMES:
        if Register == "RR":
            raise Only_For_Reading("Register RR only for reading!!!")
        else:
            __RegisterData[Register] = Data
    else:
        raise Register_Not_Found("Register "+str(Register)+" not found!!!")

def GetRegisterData(Register):
    if Register in REGISTER_NAMES:
        return __RegisterData.get(Register)
    else:
        raise Register_Not_Found("Register "+str(Register)+" not found!!!")


#----------------------Functions for data processing, calculations, etc----------------------
def Dec(Register):
    if Register in REGISTER_NAMES:
        if type(GetRegisterData(Register)) == int:
            SetRegisterData(Register, GetRegisterData(Register)-1)
        else:
            raise Type_Error(str(GetRegisterData(Register))+" impossible to convert!!!")
    else:
        raise Register_Not_Found("Register "+str(Register)+" not found!!!")

def Inc(Register):
    if Register in REGISTER_NAMES:
        if type(GetRegisterData(Register)) == int:
            SetRegisterData(Register, GetRegisterData(Register)+1)
        else:
            raise Type_Error(str(GetRegisterData(Register))+" impossible to convert!!!")
    else:
        raise Register_Not_Found("Register "+str(Register)+" not found!!!")

def Add(FirstArgv, SecondArgv):
    if type(FirstArgv) == int and type(SecondArgv) == int:
        __RegisterData[RR] = FirstArgv + SecondArgv
    elif (FirstArgv) == str and type(SecondArgv) == str:
        __RegisterData[RR] = FirstArgv + SecondArgv
    else:
        raise Type_Error(str(FirstArgv)+" + "+str(SecondArgv)+" impossible to convert!!!")


#--------------------Additional functions for working with data-------------------
def ClearRegister(Register):
    if Register == REGISTER_ALL:
        for RegisterName in REGISTER_NAMES:
            __RegisterData[RegisterName] = NULL
    else:
        if Register in REGISTER_NAMES:
            if Register == "RR":
                raise Only_For_Reading("Register RR only for reading!!!")
            else:
                __RegisterData[Register] = NULL
        else:
            raise Register_Not_Found("Register "+str(Register)+" not found!!!")

def ClearHeap(Label):
    if Label == HEAP_ALL:
        __HeapData.clear()
    elif Label not in HeapLabel:
        raise Label_Not_Found(str(Label)+" not found!!!")
    else:
        HeapBackup = {}
        if Label in HeapLabel:
            for Element in __HeapData:
                if Element == Label:
                    HeapLabel.remove(Label)
                else:
                    HeapBackup[Element] = GetHeapData(Element)
        __HeapData.clear()
        for Element in HeapBackup:
            __HeapData[Element] = HeapBackup.get(Element)

def PrintRegister(Password):
    if Password == chr(71)+chr(97)+chr(115)+chr(109)+chr(70)+chr(111)+chr(114)+chr(68)+chr(101)+chr(118):
        print(__RegisterData)
    else:
        exit(print("The password is incorrect!!! Pls use Password: https://github.com/Groiznyi-Studio/GasmCore"))

def PrintHeap(Password):
    if Password == chr(71)+chr(97)+chr(115)+chr(109)+chr(70)+chr(111)+chr(114)+chr(68)+chr(101)+chr(118):
        print(__HeapData)
    else:
        exit(print("The password is incorrect!!! Pls use Password: https://github.com/Groiznyi-Studio/GasmCore"))
