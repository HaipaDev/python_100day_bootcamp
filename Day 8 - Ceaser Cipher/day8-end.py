alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
_debug=True

#region first version
def encrypt(_text,_shift):
    _output=""
    for char in _text:
        _shiftLeft=_shift
        pos=alphabet.index(char)
        if(_debug):print(f"{_text} | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
        while(_shiftLeft>0 and pos<len(alphabet)-1):
            pos+=1
            _shiftLeft-=1
            if(_debug):print(f"1 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
        if(_shiftLeft>0 and pos==len(alphabet)-1):
            pos=0
            _shiftLeft-=1
            if(_debug):print(f"2 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
        while(_shiftLeft>0 and pos<len(alphabet)-1):
            pos+=1
            _shiftLeft-=1
            if(_debug):print(f"3 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
        _output+=alphabet[pos]
        if(_debug):print(f"{char} -> {alphabet[pos]}\n\n")
    #print(_output)
    print(f"\n{_text} -> {_output}")

def decrypt(_text,_shift):
    _output=""
    for char in _text:
        _shiftLeft=_shift
        pos=alphabet.index(char)
        if(_debug):print(f"{_text} | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
        while(_shiftLeft>0 and pos>0):
            pos-=1
            _shiftLeft-=1
            if(_debug):print(f"1 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
        if(_shiftLeft>0 and pos==0):
            pos=len(alphabet)-1
            _shiftLeft-=1
            if(_debug):print(f"2 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
        while(_shiftLeft>0 and pos>0):
            pos-=1
            _shiftLeft-=1
            if(_debug):print(f"3 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
        _output+=alphabet[pos]
        if(_debug):print(f"{char} -> {alphabet[pos]}\n\n")
    #print(_output)
    print(f"\n{_text} -> {_output}")
#endregion

#region caesar function
def caeasar(_text,_shift,_direction):
    _output=""
    _startpos=0
    _endpos=len(alphabet)-1
    _shiftAmnt=1
    if(_direction=="d" or _direction=="de" or _direction=="dec" or _direction=="decode" or _direction=="decrypt"):
        _endpos,_startpos=_startpos,_endpos
        _shiftAmnt*=-1
    if(_debug):print(f"{_startpos} -- {_endpos} | {_shiftAmnt}")

    for char in _text:
        _shiftLeft=_shift
        if(char in alphabet):
            pos=alphabet.index(char)
            if(_debug):print(f"{_text} | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
            while(_shiftLeft>0 and ((_endpos!=0 and pos<_endpos)or(_endpos==0 and pos>_endpos))):
                pos+=_shiftAmnt
                _shiftLeft-=1
                if(_debug):print(f"1 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
            if(_shiftLeft>0 and pos==_endpos):
                pos=_startpos
                _shiftLeft-=1
                if(_debug):print(f"2 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
            while(_shiftLeft>0 and ((_endpos!=0 and pos<_endpos)or(_endpos==0 and pos>_endpos))):
                pos+=_shiftAmnt
                _shiftLeft-=1
                if(_debug):print(f"3 | {_shift} {_shiftLeft} | Pos: {pos} = {alphabet[pos]}")
            _output+=alphabet[pos]
            if(_debug):print(f"{char} -> {alphabet[pos]}\n\n")
        else: _output+=char
    print(f"\n{_text} -> {_output}")
    reset=input("Do you want to restart the program? (1 or Y or Yes): ")
    if(reset=="" or reset=="1" or reset=="y" or reset=="Y" or reset=="yes" or reset=="Yes"):print("\n");start()
#endregion

#region start
from art import logo
print(logo)

def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift=len(alphabet)
    shiftMessage=""
    while(shift>=len(alphabet) or shift<1):
        while(not shiftMessage.isnumeric()):#shiftMessage=int(input("Type the shift number:\n"))
            shiftMessage=input("Type the shift number:\n")
        shift=int(shiftMessage)
        if(shift>=len(alphabet) or shift<1):shiftMessage=""#;shift=len(alphabet)
    caeasar(text,shift,direction)
start()
#if(direction=="" or direction=="e" or direction=="en" or direction=="enc" or direction=="encode" or direction=="encrypt"):encrypt(text,shift)
#elif(direction=="d" or direction=="de" or direction=="dec" or direction=="decode" or direction=="decrypt"):decrypt(text,shift)
#endregion