#belongs to EXPERIMENT 3
#tautology
p=0
q=0
flag=0
p1=1
p2=1
checker=0
print("THE EXPRESSION USED FOR TAUTOLOGY IS:(p->q)or(q->p):\np\tq\tp->q\tq->p\texp\n")
for i in range(4):
    if(p==1 and q==0):
        p1=0
    if(q==1 and p==0):
        p2=0    
    if(p1==1 or p2==1):
        print("{}\t{}\t{}\t{}\t1".format(p,q,p1,p2))
    else:
        print("{}\t{}\t{}\t{}\t0".format(p,q,p1,p2))
        checker=1
    flag=flag+1
    if(q==0):
        q=1
    else:
        q=0
    if(flag%2==0):
        if(p==0):
            p=1
        else:
            p=0
    p1=1
    p2=1
if(checker==0):
    print("\nTAUTOLOGY")
else:
    print("\nNOT TAUTOLOGY")
#contradiction
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++\nTHE EXPRESSION USED FOR CONTRADICTION IS:(p and q) and (~p):\np\tq\tp and q\t~p\texp\n")
p=0
q=0
flag=0
p1=0
p2=1
checker=0
for i in range(4):
    if(p==1 and q==1):
        p1=1
    if(p==0):
        p2=1
    else:
        p2=0
    if( p1==1 and p2==1):
        print("{}\t{}\t{}\t{}\t1".format(p,q,p1,p2))
        checker=1
    else:
        print("{}\t{}\t{}\t{}\t0".format(p,q,p1,p2))
    flag=flag+1
    if(q==0):
        q=1
    else:
        q=0
    if(flag%2==0):
        if(p==0):
            p=1
        else:
            p=0
    p1=0
    p2=1
if(checker==0):
    print("\nCONTRADICTION")
else:
    print("\nNOT CONTRADICTION")
#staisfied
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++\nTHE EXPRESSION USED FOR SATISFICATION IS: ~p ->(q^~q) :\np\tq\t~p\tq^~q\texp\n")
p=0
q=0
flag=0
p1=0
p2=0
checker=0
for i in range(4):
    if(p==0):
        p1=1
    else:
        p1=0
    if( p1==1 and p2==0):
        print("{}\t{}\t{}\t{}\t0".format(p,q,p1,p2))
    else:
        print("{}\t{}\t{}\t{}\t1".format(p,q,p1,p2))
        checker=1
    flag=flag+1
    if(q==0):
        q=1
    else:
        q=0
    if(flag%2==0):
        if(p==0):
            p=1
        else:
            p=0
    p1=0
    p2=0
if(checker==1):
    print("\nSATISFIED\n")
else:
    print("\nNOT SATISFIED\n")

#the next day 
p=0
q=0
flag=0
p1=1
p2=1
checker=0
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++\nTHE EXPRESSION USED FOR TAUTOLOGY IS:(p -> q) <-> (~q-> ~p):\np\tq\tp->q\t~q->~p\texp\n")
for i in range(4):
    if(p==1 and q==0):
        p1=0
    if(q==0 and p==1):
        p2=0 
    if((p1==0 and p2==0)or(p1==1 and p2==1)):
        print("{}\t{}\t{}\t{}\t1".format(p,q,p1,p2))
    else:
        print("{}\t{}\t{}\t{}\t0".format(p,q,p1,p2))
        checker=1
    flag=flag+1
    if(q==0):
        q=1
    else:
        q=0
    if(flag%2==0):
        if(p==0):
            p=1
        else:
            p=0
    p1=1
    p2=1
if(checker==0):
    print("\nTAUTOLOGY")
else:
    print("\nNOT TAUTOLOGY")