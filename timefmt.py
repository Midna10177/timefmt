def timefmt(s,neg=False):
    out=[]
    names=[ ['centurie',100*365*24*60*60],
            ['decade',10*365*24*60*60],
            ['year',365*24*60*60],
            ['month',730.001*60*60],
            ['week',7*24*60*60],
            ['day',24*60*60],
            ['hour',60*60],
            ['minute',60],
            ['second',1]]
    while names and s>=0:
        cur=names.pop(0)
        if s<cur[1]: continue
        if s//cur[1]>1: cur[0] += 's'

        out.append('-'*neg+str(int(s//cur[1])) +' '+ cur[0])
        s%=cur[1]
    return(', '.join(out))
i='none'
while(i.lower().strip()!='exit'):
    i=input('enter a num: ')
    try:
        i=float(i)
        if i % int(i)==0: i=int(i)
    except:
        print('float convert error')
    formatcode='{:,'+['d','f'][type(i)==float]+'}'
    print(formatcode.format(i))
    print(timefmt(i))
    i=str(i)
