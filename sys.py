'''import mysql      #connecting python with mysql
import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
mycursor=mycon.cursor()
#creating table for AUDI1
mycursor.execute("create table AUDI_1(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,NAME varchar(50) NOT NULL,EMAIL varchar(50),PHONE_NUMBER varchar(11),TOTAL_SEATS integer(4),SEATS VARCHAR(100),TOTAL_PRICE integer(10))")
mycursor.execute("create table SEATAUDI_1(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,SEAT varchar(5))") #creating table to store seat numbers
#creating table for AUDI2
mycursor.execute("create table AUDI_2(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,NAME varchar(50) NOT NULL,EMAIL varchar(50),PHONE_NUMBER varchar(11),TOTAL_SEATS integer(4),SEATS VARCHAR(100),TOTAL_PRICE integer(10))")
mycursor.execute("create table SEATAUDI_2(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,SEAT varchar(5))")  #creating table to store seat numbers
#creating table for AUDI3
mycursor.execute("create table AUDI_3(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,NAME varchar(50) NOT NULL,EMAIL varchar(50),PHONE_NUMBER varchar(11),TOTAL_SEATS integer(4),SEATS VARCHAR(100),TOTAL_PRICE integer(10))")
mycursor.execute("create table SEATAUDI_3(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,SEAT varchar(5))")   #creating table to store seat numbers
#creating table to store movies' details
mycursor.execute("create table MOVIES(SNO integer(3) primary key NOT NULL AUTO_INCREMENT,MOVIE_NAME varchar(50) NOT NULL,GENRE varchar(50),RATING decimal(4,1),RUNNING_TIME varchar(20),DESCRIPTION long,CAST long)")
#creating table to store auditoriums' details
mycursor.execute("create table theatre(SNO integer(4) primary key NOT NULL auto_increment,AUDI varchar(25),MOVIE varchar(50),CAPACITY integer(5),BOOKED_SEAT integer(5))")  #creating table to store number of booked seats
'''

def title():
    print("\t\t                           __                          ")
    print("\t\t\    / * __ *  __         /  \ *       _           _   ")
    print("\t\t \  /  ||__ | |  | \/\   |     | \/\  /_\ \/\ /\  / _\ ")
    print("\t\t  \/   | __|| |__| |  |   \__/ | |  | \_  |  |  | < _|_")
    print("\n\t      WELCOME TO VISION CINEMA! FIND THE BEST MOVIE TO WATCH WITH US!")
    print("\t\t     GET THE BEST EXPERIENCE HAPPENING OUT THERE!") 

def movies_playing():
    import mysql      #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    mycursor.execute("select SNO,MOVIE_NAME,GENRE,RATING,RUNNING_TIME,DESCRIPTION,CAST from MOVIES")  #displaying movies and their details
    for x in mycursor:
        print('\n',x[0],')',"MOVIE       :",x[1],'\n',"    GENRE       :",x[2],'\n',"    RATING      :",x[3],'\n',"    RUNNING TIME:",x[4],'\n',"    DESCRIPTION :",x[5],'\n',"    CAST        :",x[6])

def Audi1():
    import mysql     #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    #creating table for AUDI1
    '''mycursor.execute("create table AUDI_1(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,NAME varchar(50) NOT NULL,EMAIL varchar(50),PHONE_NUMBER varchar(11),TOTAL_SEATS integer(4),SEATS VARCHAR(100),TOTAL_PRICE integer(10))")
    mycursor.execute("create table SEATAUDI_1(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,SEAT varchar(5))") '''#creating table to store seat numbers
    mycursor.execute("SELECT * FROM SEATAUDI_1")
    C=[]
    for x in mycursor:
        C.append(x[1])
    book=[]
    #seat is stored as a key in a dictonary
    theaudi={'A1':' ','A2':' ','A3':' ','A4':' ','A5':' ','A6':' ','A7':' ','A8':' ','A9':' ','A10':' ','A11':' ','A12':' ','A13':' ','A14':' ','A15':' ','A16':' ',
             'B1':' ','B2':' ','B3':' ','B4':' ','B5':' ','B6':' ','B7':' ','B8':' ','B9':' ','B10':' ','B11':' ','B12':' ','B13':' ','B14':' ','B15':' ','B16':' ',
             'C1':' ','C2':' ','C3':' ','C4':' ','C5':' ','C6':' ','C7':' ','C8':' ','C9':' ','C10':' ','C11':' ','C12':' ','C13':' ','C14':' ','C15':' ','C16':' ',
             'D1':' ','D2':' ','D3':' ','D4':' ','D5':' ','D6':' ','D7':' ','D8':' ','D9':' ','D10':' ','D11':' ','D12':' ','D13':' ','D14':' ','D15':' ','D16':' ',
             'E1':' ','E2':' ','E3':' ','E4':' ','E5':' ','E6':' ','E7':' ','E8':' ','E9':' ','E10':' ','E11':' ','E12':' ','E13':' ','E14':' ','E15':' ','E16':' ',
             'F1':' ','F2':' ','F3':' ','F4':' ','F5':' ','F6':' ','F7':' ','F8':' ','F9':' ','F10':' ','F11':' ','F12':' ','F13':' ','F14':' ','F15':' ','F16':' ',
             'G1':' ','G2':' ','G3':' ','G4':' ','G5':' ','G6':' ','G7':' ','G8':' ','G9':' ','G10':' ','G11':' ','G12':' ','G13':' ','G14':' ','G15':' ','G16':' ',
             'H1':' ','H2':' ','H3':' ','H4':' ','H5':' ','H6':' ','H7':' ','H8':' ','H9':' ','H10':' ','H11':' ','H12':' ','H13':' ','H14':' ','H15':' ','H16':' ',
             'I1':' ','I2':' ','I3':' ','I4':' ','I5':' ','I6':' ','I7':' ','I8':' ','I9':' ','I10':' ','I11':' ','I12':' ','I13':' ','I14':' ','I15':' ','I16':' ',
             'J1':' ','J2':' ','J3':' ','J4':' ','J5':' ','J6':' ','J7':' ','J8':' ','J9':' ','J10':' ','J11':' ','J12':' ','J13':' ','J14':' ','J15':' ','J16':' ',
             'K1':' ','K2':' ','K3':' ','K4':' ','K5':' ','K6':' ','K7':' ','K8':' ','K9':' ','K10':' ','K11':' ','K12':' ','K13':' ','K14':' ','K15':' ','K16':' ',
             'L1':' ','L2':' ','L3':' ','L4':' ','L5':' ','L6':' ','L7':' ','L8':' ','L9':' ','L10':' ','L11':' ','L12':' ','L13':' ','L14':' ','L15':' ','L16':' ','L17':' ','L18':' ','L19':' ','L20':' '}
    audiseat=[]
    for num in theaudi:
        audiseat.append(num)

    def printseats(seat):
        #arrangement of seats
        print()
        print("\t  1       5         10        15        20")
        print("\t +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print('\tL|'+ seat['L1'] + '|'+ seat['L2']+'|'+ seat['L3']+'|'+ seat['L4']+'|'+ seat['L5']+'|'+ seat['L6']+'|'+ seat['L7']+'|'+ seat['L8']+'|'+ seat['L9']+'|'+ seat['L10'] + '|'+ seat['L11'] + '|'+ seat['L12']+ '|' + seat['L13']+'|'+ seat['L14']+'|'+ seat['L15']+'|'+ seat['L16']+'|'+ seat['L17']+'|'+ seat['L18']+'|'+ seat['L19']+'|'+ seat['L20'] + '|L')
        print("\t +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print('\tK    |'+ seat['K1'] + '|'+ seat['K2']+'|'+ seat['K3']+'|'+ seat['K4']+'|'+ seat['K5']+'|'+ seat['K6']+'|'+ seat['K7']+'|'+ seat['K8']+'|'+ seat['K9']+'|'+ seat['K10'] + '|'+ seat['K11'] + '|'+ seat['K12']+ '|' + seat['K13']+'|'+ seat['K14']+'|'+ seat['K15']+'|'+ seat['K16'] + '|K')
        print("\t     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("\t      1       5         10          16")
        print("\t  1             8           9             16")
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")  
        print('\tJ|'+ seat['J1'] + '|'+ seat['J2']+'|'+ seat['J3']+'|'+ seat['J4']+'|'+ seat['J5']+'|'+ seat['J6']+'|'+ seat['J7']+'|'+ seat['J8']+'|'+'         |'+ seat['J9']+'|'+ seat['J10'] + '|'+ seat['J11'] + '|'+ seat['J12']+ '|' + seat['J13']+'|'+ seat['J14']+'|'+ seat['J15']+'|'+ seat['J16'] + '|J')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+") 
        print('\tI|'+ seat['I1'] + '|'+ seat['I2']+'|'+ seat['I3']+'|'+ seat['I4']+'|'+ seat['I5']+'|'+ seat['I6']+'|'+ seat['I7']+'|'+ seat['I8']+'|'+'         |'+ seat['I9']+'|'+ seat['I10'] + '|'+ seat['I11'] + '|'+ seat['I12']+ '|' + seat['I13']+'|'+ seat['I14']+'|'+ seat['I15']+'|'+ seat['I16'] + '|I')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print('\tH|'+ seat['H1'] + '|'+ seat['H2']+'|'+ seat['H3']+'|'+ seat['H4']+'|'+ seat['H5']+'|'+ seat['H6']+'|'+ seat['H7']+'|'+ seat['H8']+'|'+'         |'+ seat['H9']+'|'+ seat['H10'] + '|'+ seat['H11'] + '|'+ seat['H12']+ '|' + seat['H13']+'|'+ seat['H14']+'|'+ seat['H15']+'|'+ seat['H16'] + '|H')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print('\tG|'+ seat['G1'] + '|'+ seat['G2']+'|'+ seat['G3']+'|'+ seat['G4']+'|'+ seat['G5']+'|'+ seat['G6']+'|'+ seat['G7']+'|'+ seat['G8']+'|'+'         |'+ seat['G9']+'|'+ seat['G10'] + '|'+ seat['G11'] + '|'+ seat['G12']+ '|' + seat['G13']+'|'+ seat['G14']+'|'+ seat['G15']+'|'+ seat['G16'] + '|G')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print('\tF|'+ seat['F1'] + '|'+ seat['F2']+'|'+ seat['F3']+'|'+ seat['F4']+'|'+ seat['F5']+'|'+ seat['F6']+'|'+ seat['F7']+'|'+ seat['F8']+'|'+'         |'+ seat['F9']+'|'+ seat['F10'] + '|'+ seat['F11'] + '|'+ seat['F12']+ '|' + seat['F13']+'|'+ seat['F14']+'|'+ seat['F15']+'|'+ seat['F16'] + '|F')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print("\t  1             8           9             16")
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print('\tE|'+ seat['E1'] + '|'+ seat['E2']+'|'+ seat['E3']+'|'+ seat['E4']+'|'+ seat['E5']+'|'+ seat['E6']+'|'+ seat['E7']+'|'+ seat['E8']+'|'+'         |'+ seat['E9']+'|'+ seat['E10'] + '|'+ seat['E11'] + '|'+ seat['E12']+ '|' + seat['E13']+'|'+ seat['E14']+'|'+ seat['E15']+'|'+ seat['E16'] + '|E')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print('\tD|'+ seat['D1'] + '|'+ seat['D2']+'|'+ seat['D3']+'|'+ seat['D4']+'|'+ seat['D5']+'|'+ seat['D6']+'|'+ seat['D7']+'|'+ seat['D8']+'|'+'         |'+ seat['D9']+'|'+ seat['D10'] + '|'+ seat['D11'] + '|'+ seat['D12']+ '|' + seat['D13']+'|'+ seat['D14']+'|'+ seat['D15']+'|'+ seat['D16'] + '|D')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print('\tC|'+ seat['C1'] + '|'+ seat['C2']+'|'+ seat['C3']+'|'+ seat['C4']+'|'+ seat['C5']+'|'+ seat['C6']+'|'+ seat['C7']+'|'+ seat['C8']+'|'+'         |'+ seat['C9']+'|'+ seat['C10'] + '|'+ seat['C11'] + '|'+ seat['C12']+ '|' + seat['C13']+'|'+ seat['C14']+'|'+ seat['C15']+'|'+ seat['C16'] + '|C')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print('\tB|'+ seat['B1'] + '|'+ seat['B2']+'|'+ seat['B3']+'|'+ seat['B4']+'|'+ seat['B5']+'|'+ seat['B6']+'|'+ seat['B7']+'|'+ seat['B8']+'|'+'         |'+ seat['B9']+'|'+ seat['B10'] + '|'+ seat['B11'] + '|'+ seat['B12']+ '|' + seat['B13']+'|'+ seat['B14']+'|'+ seat['B15']+'|'+ seat['B16'] + '|B')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print('\tA|'+ seat['A1'] + '|'+ seat['A2']+'|'+ seat['A3']+'|'+ seat['A4']+'|'+ seat['A5']+'|'+ seat['A6']+'|'+ seat['A7']+'|'+ seat['A8']+'|'+'         |'+ seat['A9']+'|'+ seat['A10'] + '|'+ seat['A11'] + '|'+ seat['A12']+ '|' + seat['A13']+'|'+ seat['A14']+'|'+ seat['A15']+'|'+ seat['A16'] + '|A')
        print("\t +-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+")
        print("\n\n")
        print("\t                SCRREEN THIS WAY")
        print("\t ___________________________________________")
    totalseat=int(input("\n\nEnter the total number of seats to be booked:"))
    print("\nPLATINUM(K-L):Rs.250")
    print("GOLD(F-J)    :Rs.170")
    print("SILVER(A-E)  :Rs.100")
    print("\n+-+")
    print("|X| -->OCCUPIED")
    print("+-+")
    ts=totalseat
    booked='X'  #seat's value will become 'X' if the seat is booked 
    count=0
    b=[]
    for i in C:
        theaudi[i]=booked
    while totalseat>0:
        printseats(theaudi)
        print()
        try:
            row=input("Enter the row:")
            col=input("Enter the seat number:")
            bookedseat=row.upper()+col
        
            if bookedseat not in book:
                book.append(bookedseat)
                ss="insert into SEATAUDI_1(SEAT) values('{}')".format(bookedseat)
                mycursor.execute(ss)
                if theaudi[bookedseat]==' ':
                    theaudi[bookedseat]=booked
                    totalseat-=1
                
                else:
                    print("Sorry the seat is already filled, please move somewhere else..")
            b.append(bookedseat)
        except:    #checking exceptions
            print("Invalid input. Please choose somewhere else")
        else:
            if row.upper=='L':
                if int(col)==0 or int(col)>20:
                    print("Sorry, Only 1 to 20 seats available")
                    continue
            elif row.upper() in "ABCDEFGHIJK":
                if int(col)==0 or int(col)>16:
                    print("Sorry ,Only 1 to 16 seats available")
                    continue
            elif row.upper() not in "ABCDEFGHIJKL" and int(col)>=0:
                print("Sorry, Only A to L rows are available")
                continue
            else:
                pass
    printseats(theaudi)

    be=' '.join(b)     #converting list into string 
    price=0
    for i in b:
        if i[0] in "ABCDE":
            price+=100
        elif i[0] in "FGHIJ":
            price+=170
        elif i[0] in "KL":
            price+=250

    #taking deatils of people
    nm=input("\nENTER NAME\n>")
    email=input("ENTER EMAIL ID\n>")
    phno=input("ENTER PHONE NUMBER\n>")
    try:
        z="insert into AUDI_1(NAME,EMAIL,PHONE_NUMBER,TOTAL_SEATS,SEATS,TOTAL_PRICE) values('{}','{}','{}',{},'{}',{})".format(nm.upper(),email,phno,ts,be,price)  #storing details in table
        mycursor.execute(z)
        mycon.commit()
    except:
        mycon.rollback()
        
    print("\nYOU SUBTOTAL IS: RS.",price)
    print("\nPROCEEDING FOR TRANSACTION...")
    mycursor.execute("select MOVIE from theatre where AUDI='Audi1'")
    
    print("\n\n**BOOKING CONFIRMED**")
    print("\nHere is your ticket. Enjoy your movie!")
    print("_______________________________________________________")      #displaying ticket
    print("                    VISION CINEMA                      ")
    print("                 -------------------                   ")
    print("                                                       ")
    print("                                                       ")
    print("  ",nm.upper(),"                                           ")
    print("                                                       ")
    print("   AUDI:1    ",be,"       6:00PM","     22/10         ")
    print("                                                       ")
    print("________________________________________________________")
    print("\nTHANK YOU FOR BOOKING!") 
    print("")  

def Audi2():
    import mysql     #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    #creating table for AUDI2
    '''mycursor.execute("create table AUDI_2(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,NAME varchar(50) NOT NULL,EMAIL varchar(50),PHONE_NUMBER varchar(11),TOTAL_SEATS integer(4),SEATS VARCHAR(100),TOTAL_PRICE integer(10))")
    mycursor.execute("create table SEATAUDI_2(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,SEAT varchar(5))") ''' #creating table to store seat numbers
    mycursor.execute("SELECT * FROM SEATAUDI_2")
    C=[]
    for x in mycursor:
        C.append(x[1])
    book=[]
    #seat is stored as a key in a dictonary
    theaudi={'A1':' ','A2':' ','A3':' ','A4':' ','A5':' ','A6':' ','A7':' ','A8':' ','A9':' ','A10':' ','A11':' ','A12':' ','A13':' ','A14':' ','A15':' ','A16':' ','A17':' ','A18':' ',
             'B1':' ','B2':' ','B3':' ','B4':' ','B5':' ','B6':' ','B7':' ','B8':' ','B9':' ','B10':' ','B11':' ','B12':' ','B13':' ','B14':' ','B15':' ','B16':' ','B17':' ','B18':' ',
             'C1':' ','C2':' ','C3':' ','C4':' ','C5':' ','C6':' ','C7':' ','C8':' ','C9':' ','C10':' ','C11':' ','C12':' ','C13':' ','C14':' ','C15':' ','C16':' ','C17':' ','C18':' ',
             'D1':' ','D2':' ','D3':' ','D4':' ','D5':' ','D6':' ','D7':' ','D8':' ','D9':' ','D10':' ','D11':' ','D12':' ','D13':' ','D14':' ','D15':' ','D16':' ','D17':' ','D18':' ',
             'E1':' ','E2':' ','E3':' ','E4':' ','E5':' ','E6':' ','E7':' ','E8':' ','E9':' ','E10':' ','E11':' ','E12':' ','E13':' ','E14':' ','E15':' ','E16':' ','E17':' ','E18':' ',
             'F1':' ','F2':' ','F3':' ','F4':' ','F5':' ','F6':' ','F7':' ','F8':' ','F9':' ','F10':' ','F11':' ','F12':' ','F13':' ','F14':' ','F15':' ','F16':' ','F17':' ','F18':' ',
             'G1':' ','G2':' ','G3':' ','G4':' ','G5':' ','G6':' ','G7':' ','G8':' ','G9':' ','G10':' ','G11':' ','G12':' ','G13':' ','G14':' ','G15':' ','G16':' ','G17':' ','G18':' ',
             'H1':' ','H2':' ','H3':' ','H4':' ','H5':' ','H6':' ','H7':' ','H8':' ','H9':' ','H10':' ','H11':' ','H12':' ','H13':' ','H14':' ','H15':' ','H16':' ','H17':' ','H18':' ',
             'I1':' ','I2':' ','I3':' ','I4':' ','I5':' ','I6':' ','I7':' ','I8':' ','I9':' ','I10':' ','I11':' ','I12':' ','I13':' ','I14':' ','I15':' ','I16':' ','I17':' ','I18':' ',
             'J1':' ','J2':' ','J3':' ','J4':' ','J5':' ','J6':' ','J7':' ','J8':' ','J9':' ','J10':' ','J11':' ','J12':' ','J13':' ','J14':' ','J15':' ','J16':' ','J17':' ','J18':' ',
             'K1':' ','K2':' ','K3':' ','K4':' ','K5':' ','K6':' ','K7':' ','K8':' ','K9':' ','K10':' ','K11':' ','K12':' ','K13':' ','K14':' ','K15':' ','K16':' ',
             'L1':' ','L2':' ','L3':' ','L4':' ','L5':' ','L6':' ','L7':' ','L8':' ','L9':' ','L10':' ','L11':' ','L12':' ','L13':' ','L14':' ','L15':' ','L16':' ','L17':' ','L18':' ','L19':' ','L20':' '}
    audiseat=[]
    for num in theaudi:
        audiseat.append(num)

    def printseats(seat):
        #arrangement of seats
        print("\t  1       5         10        15        20")
        print("\t +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print('\tL|'+ seat['L1'] + '|'+ seat['L2']+'|'+ seat['L3']+'|'+ seat['L4']+'|'+ seat['L5']+'|'+ seat['L6']+'|'+ seat['L7']+'|'+ seat['L8']+'|'+ seat['L9']+'|'+ seat['L10'] + '|'+ seat['L11'] + '|'+ seat['L12']+ '|' + seat['L13']+'|'+ seat['L14']+'|'+ seat['L15']+'|'+ seat['L16']+'|'+ seat['L17']+'|'+ seat['L18']+'|'+ seat['L19']+'|'+ seat['L20'] + '|L')
        print("\t +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print('\tK    |'+ seat['K1'] + '|'+ seat['K2']+'|'+ seat['K3']+'|'+ seat['K4']+'|'+ seat['K5']+'|'+ seat['K6']+'|'+ seat['K7']+'|'+ seat['K8']+'|'+ seat['K9']+'|'+ seat['K10'] + '|'+ seat['K11'] + '|'+ seat['K12']+ '|' + seat['K13']+'|'+ seat['K14']+'|'+ seat['K15']+'|'+ seat['K16'] + '|     K')
        print("\t     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("\t     1       5         10          16")
        print("\t  1         6   7         12  13        18")
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+")  
        print('\tJ|'+ seat['J1'] + '|'+ seat['J2']+'|'+ seat['J3']+'|'+ seat['J4']+'|'+ seat['J5']+'|'+ seat['J6']+'| '+'|'+  seat['J7']+'|'+ seat['J8']+'|'+ seat['J9']+'|'+ seat['J10'] + '|'+ seat['J11'] + '|'+ seat['J12']+ '| '+ '|' + seat['J13']+'|'+ seat['J14']+'|'+ seat['J15']+'|'+ seat['J16'] + '|'+ seat['J17']+'|'+ seat['J18']+'|J')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+")  
        print('\tI|'+ seat['I1'] + '|'+ seat['I2']+'|'+ seat['I3']+'|'+ seat['I4']+'|'+ seat['I5']+'|'+ seat['I6']+'| '+ '|'+ seat['I7']+'|'+ seat['I8']+'|'+ seat['I9']+'|'+ seat['I10'] + '|'+ seat['I11'] + '|'+ seat['I12']+ '| '+ '|' + seat['I13']+'|'+ seat['I14']+'|'+ seat['I15']+'|'+ seat['I16'] + '|'+ seat['I17']+'|'+ seat['I18']+'|I')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print('\tH|'+ seat['H1'] + '|'+ seat['H2']+'|'+ seat['H3']+'|'+ seat['H4']+'|'+ seat['H5']+'|'+ seat['H6']+'| '+ '|'+ seat['H7']+'|'+ seat['H8']+'|'+ seat['H9']+'|'+ seat['H10'] + '|'+ seat['H11'] + '|'+ seat['H12']+ '| '+ '|' + seat['H13']+'|'+ seat['H14']+'|'+ seat['H15']+'|'+ seat['H16'] + '|'+ seat['H17']+'|'+ seat['H18']+'|H')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print('\tG|'+ seat['G1'] + '|'+ seat['G2']+'|'+ seat['G3']+'|'+ seat['G4']+'|'+ seat['G5']+'|'+ seat['G6']+'| '+ '|'+ seat['G7']+'|'+ seat['G8']+'|'+ seat['G9']+'|'+ seat['G10'] + '|'+ seat['G11'] + '|'+ seat['G12']+ '| '+ '|' + seat['G13']+'|'+ seat['G14']+'|'+ seat['G15']+'|'+ seat['G16'] + '|'+ seat['G17']+'|'+ seat['G18']+'|G')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print('\tF|'+ seat['F1'] + '|'+ seat['F2']+'|'+ seat['F3']+'|'+ seat['F4']+'|'+ seat['F5']+'|'+ seat['F6']+'| '+ '|'+ seat['F7']+'|'+ seat['F8']+'|'+ seat['F9']+'|'+ seat['F10'] + '|'+ seat['F11'] + '|'+ seat['F12']+ '| '+ '|' + seat['F13']+'|'+ seat['F14']+'|'+ seat['F15']+'|'+ seat['F16'] + '|'+ seat['F17']+'|'+ seat['F18']+'|F')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print("\t  1         6   7         12  13        18")
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print('\tE|'+ seat['E1'] + '|'+ seat['E2']+'|'+ seat['E3']+'|'+ seat['E4']+'|'+ seat['E5']+'|'+ seat['E6']+'| '+ '|'+ seat['E7']+'|'+ seat['E8']+'|'+ seat['E9']+'|'+ seat['E10'] + '|'+ seat['E11'] + '|'+ seat['E12']+ '| '+ '|' + seat['E13']+'|'+ seat['E14']+'|'+ seat['E15']+'|'+ seat['E16'] + '|'+ seat['E17']+'|'+ seat['E18']+'|E')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print('\tD|'+ seat['D1'] + '|'+ seat['D2']+'|'+ seat['D3']+'|'+ seat['D4']+'|'+ seat['D5']+'|'+ seat['D6']+'| '+ '|'+ seat['D7']+'|'+ seat['D8']+'|'+ seat['D9']+'|'+ seat['D10'] + '|'+ seat['D11'] + '|'+ seat['D12']+ '| '+ '|' + seat['D13']+'|'+ seat['D14']+'|'+ seat['D15']+'|'+ seat['D16'] + '|'+ seat['D17']+'|'+ seat['D18']+'|D')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print('\tC|'+ seat['C1'] + '|'+ seat['C2']+'|'+ seat['C3']+'|'+ seat['C4']+'|'+ seat['C5']+'|'+ seat['C6']+'| '+ '|'+ seat['C7']+'|'+ seat['C8']+'|'+ seat['C9']+'|'+ seat['C10'] + '|'+ seat['C11'] + '|'+ seat['C12']+ '| '+ '|' + seat['C13']+'|'+ seat['C14']+'|'+ seat['C15']+'|'+ seat['C16'] + '|'+ seat['C17']+'|'+ seat['C18']+'|C')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print('\tB|'+ seat['B1'] + '|'+ seat['B2']+'|'+ seat['B3']+'|'+ seat['B4']+'|'+ seat['B5']+'|'+ seat['B6']+'| '+ '|'+ seat['B7']+'|'+ seat['B8']+'|'+ seat['B9']+'|'+ seat['B10'] + '|'+ seat['B11'] + '|'+ seat['B12']+ '| '+ '|' + seat['B13']+'|'+ seat['B14']+'|'+ seat['B15']+'|'+ seat['B16'] + '|'+ seat['B17']+'|'+ seat['B18']+'|B')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print('\tA|'+ seat['A1'] + '|'+ seat['A2']+'|'+ seat['A3']+'|'+ seat['A4']+'|'+ seat['A5']+'|'+ seat['A6']+'| '+ '|'+ seat['A7']+'|'+ seat['A8']+'|'+ seat['A9']+'|'+ seat['A10'] + '|'+ seat['A11'] + '|'+ seat['A12']+ '| '+ '|' + seat['A13']+'|'+ seat['A14']+'|'+ seat['A15']+'|'+ seat['A16'] + '|'+ seat['A17']+'|'+ seat['A18']+'|A')
        print("\t +-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+") 
        print("\t  1         6   7         12  13        18")
        print("\n\n")
        print("\t             SCRREEN THIS WAY")
        print("\t _________________________________________")
    totalseat=int(input("\nEnter the total number of seats to be booked:"))
    print("\nPLATINUM(K-L):Rs.250")
    print("GOLD(F-J)    :Rs.170")
    print("SILVER(A-E)  :Rs.100")
    print("\n+-+")
    print("|X| -->OCCUPIED")
    print("+-+")
    ts=totalseat
    booked='X'    #seat's value will become 'X' if the seat is booked 
    count=0

    b=[]
    for i in C:
        theaudi[i]=booked
    while totalseat>0:
        printseats(theaudi)
        print()
        try:
            row=input("Enter the row:")
            col=input("Enter the seat number:")
            bookedseat=row.upper()+col

            if bookedseat not in book:
                book.append(bookedseat)
                ss="insert into SEATAUDI_2(SEAT) values('{}')".format(bookedseat)
                mycursor.execute(ss)
                if theaudi[bookedseat]==' ':
                    theaudi[bookedseat]=booked
                    totalseat-=1
                else:
                    print("Sorry the seat is already filled, please move somewhere else..")
            b.append(bookedseat)
        except:
            print("Invalid input. Please choose somewhere else")
        else:    #checking exceptions
            if row.upper=='L':
                if int(col)==0 or int(col)>20:
                        print("Sorry, Only 1 to 20 seats available")
                        continue
            elif row.upper() in "ABCDEFGHIJ":
                if int(col)==0 or int(col)>18:
                    print("Sorry ,Only 1 to 18 seats available")
                    continue
            elif row.upper() in "K":
                if int(col)==0 or int(col)>16:
                    print("Sorry ,Only 1 to 16 seats available")
                    continue
            elif row.upper() not in "ABCDEFGHIJKL" and int(col)>=0:
                print("Sorry, Only A to L rows are available")
                continue
            else:
                pass
    printseats(theaudi)

    be=' '.join(b)
    price=0
    for i in b:
        if i[0] in "ABCDE":
            price+=100
        elif i[0] in "FGHIJ":
            price+=170
        elif i[0] in "KL":
            price+=250
     #taking deatils of people
    nm=input("\nENTER NAME\n>")
    email=input("ENTER EMAIL ID\n>")
    phno=input("ENTER PHONE NUMBER\n>")
    try:
        z="insert into AUDI_2(NAME,EMAIL,PHONE_NUMBER,TOTAL_SEATS,SEATS,TOTAL_PRICE) values('{}','{}','{}',{},'{}',{})".format(nm.upper(),email,phno,ts,be,price)
        mycursor.execute(z)
        mycon.commit()
    except:
        mycon.rollback()
    '''mycursor.execute("select * from AUDI_2")
    for x in mycursor:
        print(x)'''
    print("\nYOU SUBTOTAL IS: RS.",price)
    print("\nPROCEEDING FOR TRANSACTION...")
    mycursor.execute("select MOVIE from theatre where AUDI='Audi2'")
    print("\n\n**BOOKING CONFIRMED**")
    print("\nHere is your ticket. Enjoy your movie!")
    print("_______________________________________________________")       #displaying ticket
    print("                    VISION CINEMA                      ")         
    print("                 -------------------                   ")
    print("                                                       ")
    print("                                                       ")
    print("  ",nm.upper(),  "                                      ")
    print("                                                       ")
    print("   AUDI:2    ",be,"       5:30PM","     22/10         ")
    print("                                                       ")
    print("________________________________________________________")
    print("\nTHANK YOU FOR BOOKING!") 
    print("")  

def Audi3():
    import mysql      #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    #creating table for AUDI3
    '''mycursor.execute("create table AUDI_3(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,NAME varchar(50) NOT NULL,EMAIL varchar(50),PHONE_NUMBER varchar(11),TOTAL_SEATS integer(4),SEATS VARCHAR(100),TOTAL_PRICE integer(10))")
    mycursor.execute("create table SEATAUDI_3(SNO integer(4) primary key NOT NULL AUTO_INCREMENT,SEAT varchar(5))") '''  ##creating table to store seat numbers 
    mycursor.execute("SELECT * FROM SEATAUDI_3")
    C=[]
    for x in mycursor:
        C.append(x[1])
    book=[]
    #arrangement of seats
    theaudi={'A1':' ','A2':' ','A3':' ','A4':' ','A5':' ','A6':' ','A7':' ','A8':' ','A9':' ','A10':' ','A11':' ','A12':' ','A13':' ','A14':' ','A15':' ','A16':' ',
             'B1':' ','B2':' ','B3':' ','B4':' ','B5':' ','B6':' ','B7':' ','B8':' ','B9':' ','B10':' ','B11':' ','B12':' ','B13':' ','B14':' ','B15':' ','B16':' ',
             'C1':' ','C2':' ','C3':' ','C4':' ','C5':' ','C6':' ','C7':' ','C8':' ','C9':' ','C10':' ','C11':' ','C12':' ','C13':' ','C14':' ','C15':' ','C16':' ',
             'D1':' ','D2':' ','D3':' ','D4':' ','D5':' ','D6':' ','D7':' ','D8':' ','D9':' ','D10':' ','D11':' ','D12':' ','D13':' ','D14':' ','D15':' ','D16':' ',
             'E1':' ','E2':' ','E3':' ','E4':' ','E5':' ','E6':' ','E7':' ','E8':' ','E9':' ','E10':' ','E11':' ','E12':' ','E13':' ','E14':' ','E15':' ','E16':' ',
             'F1':' ','F2':' ','F3':' ','F4':' ','F5':' ','F6':' ','F7':' ','F8':' ','F9':' ','F10':' ','F11':' ','F12':' ','F13':' ','F14':' ','F15':' ','F16':' ',
             'G1':' ','G2':' ','G3':' ','G4':' ','G5':' ','G6':' ','G7':' ','G8':' ','G9':' ','G10':' ','G11':' ','G12':' ','G13':' ','G14':' ','G15':' ','G16':' ',
             'H1':' ','H2':' ','H3':' ','H4':' ','H5':' ','H6':' ','H7':' ','H8':' ','H9':' ','H10':' ','H11':' ','H12':' ','H13':' ','H14':' ','H15':' ','H16':' ',
             'I1':' ','I2':' ','I3':' ','I4':' ','I5':' ','I6':' ','I7':' ','I8':' ','I9':' ','I10':' ','I11':' ','I12':' ','I13':' ','I14':' ','I15':' ','I16':' ',
             'J1':' ','J2':' ','J3':' ','J4':' ','J5':' ','J6':' ','J7':' ','J8':' ','J9':' ','J10':' ','J11':' ','J12':' ','J13':' ','J14':' ','J15':' ','J16':' ',
             'K1':' ','K2':' ','K3':' ','K4':' ','K5':' ','K6':' ','K7':' ','K8':' ','K9':' ','K10':' ','K11':' ','K12':' ','K13':' ','K14':' ','K15':' ','K16':' ',
             'L1':' ','L2':' ','L3':' ','L4':' ','L5':' ','L6':' ','L7':' ','L8':' ','L9':' ','L10':' ','L11':' ','L12':' ','L13':' ','L14':' ','L15':' ','L16':' ',
             'M1':' ','M2':' ','M3':' ','M4':' ','M5':' ','M6':' ','M7':' ','M8':' ','M9':' ','M10':' ','M11':' ','M12':' ','M13':' ','M14':' ','M15':' ','M16':' ','M17':' ','M18':' ','M19':' ','M20':' '}
    audiseat=[]
    for num in theaudi:
        audiseat.append(num)

    def printseats(seat):
        print()
        print("\t  1       5         10        15        20")
        print("\t +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print('\tM|'+ seat['M1'] + '|'+ seat['M2']+'|'+ seat['M3']+'|'+ seat['M4']+'|'+ seat['M5']+'|'+ seat['M6']+'|'+ seat['M7']+'|'+ seat['M8']+'|'+ seat['M9']+'|'+ seat['M10'] + '|'+ seat['M11'] + '|'+ seat['M12']+ '|' + seat['M13']+'|'+ seat['M14']+'|'+ seat['M15']+'|'+ seat['M16']+'|'+ seat['M17']+'|'+ seat['M18']+'|'+ seat['M19']+'|'+ seat['M20'] + '|M')
        print("\t +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print('\tL|'+ seat['L1'] + '|'+ seat['L2']+'|'+ seat['L3']+'|'+ seat['L4']+'|'+'   |'+ seat['L5']+'|'+ seat['L6']+'|'+ seat['L7']+'|'+ seat['L8']+'|'+ seat['L9']+'|'+ seat['L10'] + '|'+ seat['L11'] + '|'+ seat['L12']+'|' + '   |' + seat['L13']+'|'+ seat['L14']+'|'+ seat['L15']+'|'+ seat['L16']+'|L')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tK|'+ seat['K1'] + '|'+ seat['K2']+'|'+ seat['K3']+'|'+ seat['K4']+'|'+'   |'+ seat['K5']+'|'+ seat['K6']+'|'+ seat['K7']+'|'+ seat['K8']+'|'+ seat['K9']+'|'+ seat['K10'] + '|'+ seat['K11'] + '|'+ seat['K12']+'|' + '   |' + seat['K13']+'|'+ seat['K14']+'|'+ seat['K15']+'|'+ seat['K16'] + '|K')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")  
        print('\tJ|'+ seat['J1'] + '|'+ seat['J2']+'|'+ seat['J3']+'|'+ seat['J4']+'|'+'   |'+ seat['J5']+'|'+ seat['J6']+'|'+ seat['J7']+'|'+ seat['J8']+'|'+ seat['J9']+'|'+ seat['J10'] + '|'+ seat['J11'] + '|'+ seat['J12']+'|' + '   |' + seat['J13']+'|'+ seat['J14']+'|'+ seat['J15']+'|'+ seat['J16'] + '|J')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tI|'+ seat['I1'] + '|'+ seat['I2']+'|'+ seat['I3']+'|'+ seat['I4']+'|'+'   |'+ seat['I5']+'|'+ seat['I6']+'|'+ seat['I7']+'|'+ seat['I8']+'|'+ seat['I9']+'|'+ seat['I10'] + '|'+ seat['I11'] + '|'+ seat['I12']+'|' + '   |' + seat['I13']+'|'+ seat['I14']+'|'+ seat['I15']+'|'+ seat['I16'] + '|I')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print("\t  1     4     5             12   13     16")
        #print()
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tH|'+ seat['H1'] + '|'+ seat['H2']+'|'+ seat['H3']+'|'+ seat['H4']+'|'+'   |'+ seat['H5']+'|'+ seat['H6']+'|'+ seat['H7']+'|'+ seat['H8']+'|'+ seat['H9']+'|'+ seat['H10'] + '|'+ seat['H11'] + '|'+ seat['H12']+'|' + '   |' + seat['H13']+'|'+ seat['H14']+'|'+ seat['H15']+'|'+ seat['H16'] + '|H')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tG|'+ seat['G1'] + '|'+ seat['G2']+'|'+ seat['G3']+'|'+ seat['G4']+'|'+'   |'+ seat['G5']+'|'+ seat['G6']+'|'+ seat['G7']+'|'+ seat['G8']+'|'+ seat['G9']+'|'+ seat['G10'] + '|'+ seat['G11'] + '|'+ seat['G12']+'|' + '   |' + seat['G13']+'|'+ seat['G14']+'|'+ seat['G15']+'|'+ seat['G16'] + '|G')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tF|'+ seat['F1'] + '|'+ seat['F2']+'|'+ seat['F3']+'|'+ seat['F4']+'|'+'   |'+ seat['F5']+'|'+ seat['F6']+'|'+ seat['F7']+'|'+ seat['F8']+'|'+ seat['F9']+'|'+ seat['F10'] + '|'+ seat['F11'] + '|'+ seat['F12']+'|' + '   |' + seat['F13']+'|'+ seat['F14']+'|'+ seat['F15']+'|'+ seat['F16'] + '|F')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tE|'+ seat['E1'] + '|'+ seat['E2']+'|'+ seat['E3']+'|'+ seat['E4']+'|'+'   |'+ seat['E5']+'|'+ seat['E6']+'|'+ seat['E7']+'|'+ seat['E8']+'|'+ seat['E9']+'|'+ seat['E10'] + '|'+ seat['E11'] + '|'+ seat['E12']+'|' + '   |' + seat['E13']+'|'+ seat['E14']+'|'+ seat['E15']+'|'+ seat['E16'] + '|E')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print("\t  1     4     5             12   13     16")
        #print()
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tD|'+ seat['D1'] + '|'+ seat['D2']+'|'+ seat['D3']+'|'+ seat['D4']+'|'+'   |'+ seat['D5']+'|'+ seat['D6']+'|'+ seat['D7']+'|'+ seat['D8']+'|'+ seat['D9']+'|'+ seat['D10'] + '|'+ seat['D11'] + '|'+ seat['D12']+'|' + '   |' + seat['D13']+'|'+ seat['D14']+'|'+ seat['D15']+'|'+ seat['D16'] + '|D')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tC|'+ seat['C1'] + '|'+ seat['C2']+'|'+ seat['C3']+'|'+ seat['C4']+'|'+'   |'+ seat['C5']+'|'+ seat['C6']+'|'+ seat['C7']+'|'+ seat['C8']+'|'+ seat['C9']+'|'+ seat['C10'] + '|'+ seat['C11'] + '|'+ seat['C12']+'|' + '   |' + seat['C13']+'|'+ seat['C14']+'|'+ seat['C15']+'|'+ seat['C16'] + '|C')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tB|'+ seat['B1'] + '|'+ seat['B2']+'|'+ seat['B3']+'|'+ seat['B4']+'|'+'   |'+ seat['B5']+'|'+ seat['B6']+'|'+ seat['B7']+'|'+ seat['B8']+'|'+ seat['B9']+'|'+ seat['B10'] + '|'+ seat['B11'] + '|'+ seat['B12']+'|' + '   |' + seat['B13']+'|'+ seat['B14']+'|'+ seat['B15']+'|'+ seat['B16'] + '|B')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print('\tA|'+ seat['A1'] + '|'+ seat['A2']+'|'+ seat['A3']+'|'+ seat['A4']+'|'+'   |'+ seat['A5']+'|'+ seat['A6']+'|'+ seat['A7']+'|'+ seat['A8']+'|'+ seat['A9']+'|'+ seat['A10'] + '|'+ seat['A11'] + '|'+ seat['A12']+'|' + '   |' + seat['A13']+'|'+ seat['A14']+'|'+ seat['A15']+'|'+ seat['A16'] + '|A')
        print("\t +-+-+-+-+   +-+-+-+-+-+-+-+-+   +-+-+-+-+")
        print("\t  1     4     5             12   13     16")
        print("\n\n")
        print("\t             SCRREEN THIS WAY")
        print("\t _________________________________________")
    totalseat=int(input("\nEnter the total number of seats to be booked:"))
    print("PLATINUM(I-M):Rs.250")
    print("GOLD(E-H)    :Rs.170")
    print("SILVER(A-D)  :Rs.100")
    print("\n+-+")
    print("|X| -->OCCUPIED")
    print("+-+")
    ts=totalseat
    booked='X'      #seat's value will become 'X' if the seat is booked 
    count=0

    b=[]
    for i in C:
        theaudi[i]=booked
    while totalseat>0:
        printseats(theaudi)
        print()
        try:
            row=input("Enter the row:")
            col=input("Enter the seat number:")
            bookedseat=row.upper()+col
            if bookedseat not in book:
                book.append(bookedseat)
                ss="insert into SEATAUDI_3(SEAT) values('{}')".format(bookedseat)
                mycursor.execute(ss)
                if theaudi[bookedseat]==' ':
                    theaudi[bookedseat]=booked
                    totalseat-=1
                else:
                    print("Sorry the seat is already filled, please move somewhere else..")
            b.append(bookedseat)
        
        except:
            print("Invalid input. Please choose somewhere else")
        else:      #checking exceptions
            if row.upper=='M':
                if int(col)==0 or int(col)>20:
                    print("Sorry, Only 1 to 20 seats available")
                    continue
            elif row.upper() in "ABCDEFGHIJKL":
                if int(col)==0 or int(col)>16:
                    print("Sorry ,Only 1 to 16 seats available")
                    continue
            elif row.upper() not in "ABCDEFGHIJKLM" and int(col)>=0:
                print("Sorry, Only A to M rows are available")
                continue
            else:
                pass
    
    printseats(theaudi)

    be=' '.join(b)

    price=0
    for i in b:
        if i[0] in "ABCD":
            price+=100
        elif i[0] in "EFGH":
            price+=170
        elif i[0] in "IJKLM":
            price+=250


    #taking details of people
    nm=input("\nENTER NAME\n>")
    email=input("ENTER EMAIL ID\n>")
    phno=input("ENTER PHONE NUMBER\n>")
    try:
        z="insert into AUDI_3(NAME,EMAIL,PHONE_NUMBER,TOTAL_SEATS,SEATS,TOTAL_PRICE) values('{}','{}','{}',{},'{}',{})".format(nm.upper(),email,phno,ts,be,price)
        mycursor.execute(z)
        mycon.commit()
    except:
        mycon.rollback()
    '''mycursor.execute("select * from AUDI_3")
    for x in mycursor:
        print(x)'''
    print("\nYOU SUBTOTAL IS: RS.",price)
    print("\nPROCEEDING FOR TRANSACTION...")
    mycursor.execute("select MOVIE from theatre where AUDI='Audi3'")
    print("\n\n**BOOKING CONFIRMED**")
    print("\nHere is your ticket. Enjoy your movie! ")
    print("_______________________________________________________")    #displaying ticket
    print("                    VISION CINEMA                      ")
    print("                 -------------------                   ")
    print("                                                       ")
    print("                                                       ")
    print("  ",nm.upper(),"                                           ")
    print("                                                       ")
    print("   AUDI:3    ",be,"       4:50PM","     22/10         ")
    print("                                                       ")
    print("________________________________________________________")
    print("\nTHANK YOU FOR BOOKING!")  
    
    
def cancellation():
    import mysql   #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    mycursor.execute("select SNO,MOVIE_NAME from MOVIES")
    g=1
    for x in mycursor:
        print('\n',g,')',"MOVIE :",x[1])
        g+=1
    mo_n=int(input("\nENTER MOVIE NUMBER FOR WHICH YOU BOOKED TICKET:"))
    nam=input("\nENTER YOUR NAME\n>")
    c_email=input("ENTER YOUR EMAIL\n>")
    phoneno=input("ENTER YOUR PHONE NUMBER\n>")
    if mo_n==1:
        try:
            mycursor.execute("select SEATS from Audi_1 where EMAIL='{}' ".format(c_email))  
            for x in mycursor:
                dop=x[0]
                pod=dop.split()
                
                j=0
                for i in range(0,len(pod)):
                    jol="delete from SEATAUDI_1 where SEAT='{}'".format(pod[j])  #deleting seats from the table
                    mycursor.execute(jol)
                    mycon.commit()
                    j+=1
        except Error as error:
            print("****#BOOKING DOES NOT EXIST****")
        
            
        mycursor.execute("select EMAIL from Audi_1 where EMAIL='{}'".format(c_email))
        for x in mycursor:
            if x[0]==c_email:
                try:
                    z="delete from Audi_1 where EMAIL='{}'".format(c_email)     #deleting customer's record 
                    mycursor.execute(z)
                    mycon.commit()
                    print("\n***CANCELLATION DONE***")
                    print("\n  HAVE A GREAT DAY!:)")
                except:
                    
                    mycon.rollback()
                    print("****BOOKING DOES NOT EXIST****")
                
                
            
    elif mo_n==2:
        try:
            mycursor.execute("select SEATS from Audi_2 where EMAIL='{}'".format(c_email))
            for x in mycursor:
                dop=x[0]
                pod=dop.split()
                
                j=0
                for i in range(0,len(pod)):
                    jol="delete from SEATAUDI_2 where SEAT='{}'".format(pod[j])    #deleting seats from the table
                    mycursor.execute(jol)
                    mycon.commit()
                    j+=1
        except:
            mycon.rollback()
        else:
            print("BOOKING DOES NOT EXIST")
        
        mycursor.execute("select EMAIL from Audi_2 where EMAIL='{}'".format(c_email))
        for x in mycursor:
            
            if x[0]==c_email:
                try:
                    z="delete from Audi_2 where EMAIL='{}'".format(c_email)     #deleting customer's record 
                    mycursor.execute(z)
                    mycon.commit()
                except:
                    print("BOOKING DOES NOT EXIST")
                    mycon.rollback()
                print("\n***CANCELLATION DONE***")
                print("\n  HAVE A GREAT DAY!:)")
                break
            else:
                print("BOOKING DOES NOT EXIST")
    elif mo_n==3:
        try:
            mycursor.execute("select SEATS from Audi_3 where EMAIL='{}'".format(c_email))
            for x in mycursor:
                dop=x[0]
                pod=dop.split()
                
                j=0
                for i in range(0,len(pod)):
                    jol="delete from SEATAUDI_3 where SEAT='{}'".format(pod[j])    #deleting seats from the table 
                    mycursor.execute(jol)
                    mycon.commit()
                    j+=1
        except:
            mycon.rollback()
        print("BOOKING DOES NOT EXIST")
        
        mycursor.execute("select EMAIL from Audi_3 where EMAIL='{}'".format(c_email))
        for x in mycursor:
            
            if x[0]==c_email:
                try:
                    z="delete from Audi_3 where EMAIL='{}'".format(c_email)      #deleting customer's record 
                    mycursor.execute(z)
                    mycon.commit()
                except:
                    mycon.rollback()
                print("\n***CANCELLATION DONE***")
                print("\n  HAVE A GREAT DAY!:)")
                break
            else:
                print("BOOKING DOES NOT EXIST")
                
def add_movie():  
    import mysql      #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    '''mycursor.execute("create table MOVIES(SNO integer(3) primary key NOT NULL AUTO_INCREMENT,MOVIE_NAME varchar(50) NOT NULL,GENRE varchar(50),RATING decimal(4,1),RUNNING_TIME varchar(20),DESCRIPTION long,CAST long)")'''
    mname=input("\nENTER NAME OF THE MOVIE\n>")   #adding a movie (only 3 movies can be added)
    gen=input("ENTER GENRE OF THE MOVIE\n>")
    rate=float(input("ENTER RATING OF THE MOVIE\n>"))
    time=input("ENTER RUNNING TIME OF THE MOVIE\n>")
    des=input("ENTER DESCRIPTION OF THE MOVIE\n>")
    cast=input("ENTER CAST OF THE MOVIE\n>")
    try:
        det="insert into MOVIES(MOVIE_NAME,GENRE,RATING,RUNNING_TIME,DESCRIPTION,CAST) values('{}','{}',{},'{}','{}','{}')".format(mname,gen,rate,time,des,cast)
        mycursor.execute(det)
        mycon.commit()
    except:
        mycon.rollback()
    j=1
    mycursor.execute("select * from MOVIES")
    for x in mycursor:
        print('\n',j,')',"MOVIE       :",x[1],'\n',"    GENRE       :",x[2],'\n',"    RATING      :",x[3],'\n',"    RUNNING TIME:",x[4],'\n',"    DESCRIPTION :",x[5],'\n',"    CAST        :",x[6])
        j+=1



def add_newmovie():
    import mysql      #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()

    mycursor.execute("select SNO,MOVIE_NAME from MOVIES")
    g=1
    for x in mycursor:
        print('\n',g,')',"MOVIE :",x[1])
        g+=1
    delmo=int(input("\nENTER NUMBER TO DELETE MOVIE:"))    #if one movie is to be added, one has to be deleted (all the records will be deleted)
    sure=input("\nCONFIRM TO DELETE AND ADD NEW MOVIE(Y/N)")
    if sure in ("yY"):
        mname=input("\nENTER NAME OF THE MOVIE\n>")         #details of new movie
        gen=input("ENTER GENRE OF THE MOVIE\n>")
        rate=float(input("ENTER RATING OF THE MOVIE\n>"))
        time=input("ENTER RUNNING TIME OF THE MOVIE\n>")
        des=input("ENTER DESCRIPTION OF THE MOVIE\n>")
        cast=input("ENTER CAST OF THE MOVIE\n>")
        if delmo==1:
            try:
                det="update MOVIES set MOVIE_NAME='{}',GENRE='{}',RATING={},RUNNING_TIME='{}',DESCRIPTION='{}',CAST='{}' where SNO=1".format(mname,gen,rate,time,des,cast)
                mt="update theatre set MOVIE='{}' where AUDI='Audi1'".format(mname)
                trunc1="truncate table AUDI_1"          #deleting the records of previous movie
                trunc2="truncate table SEATAUDI_1"
                mycursor.execute(det)
                mycursor.execute(mt)
                mycursor.execute(trunc1)
                mycursor.execute(trunc2)
                mycon.commit()
            except:
                mycon.rollback()
            j=1
            mycursor.execute("select count(seat) from seataudi_1")
            for x in mycursor :
                a1_book=x[0]
            mycursor.execute("update theatre set BOOKED_SEAT={} where AUDI='Audi1'".format(a1_book))
            mycon.commit()
            mycursor.execute("select * from MOVIES")
            for x in mycursor:
                print('\n',j,')',"MOVIE       :",x[1],'\n',"    GENRE       :",x[2],'\n',"    RATING      :",x[3],'\n',"    RUNNING TIME:",x[4],'\n',"    DESCRIPTION :",x[5],'\n',"    CAST        :",x[6])
                j+=1

        elif delmo==2:
            try:
                det="update MOVIES set MOVIE_NAME='{}',GENRE='{}',RATING={},RUNNING_TIME='{}',DESCRIPTION='{}',CAST='{}' where SNO=2".format(mname,gen,rate,time,des,cast)
                mt="update theatre set MOVIE='{}' where AUDI='Audi2'".format(mname)
                trunc1="truncate table AUDI_2"           #deleting the records of previous movie
                trunc2="truncate table SEATAUDI_2"
                mycursor.execute(det)
                mycursor.execute(mt)
                mycursor.execute(trunc1)
                mycursor.execute(trunc2)
                mycon.commit()
            except:
                mycon.rollback()
            j=1
            mycursor.execute("select count(seat) from seataudi_2")
            for x in mycursor :
                a1_book=x[0]
            mycursor.execute("update theatre set BOOKED_SEAT={} where AUDI='Audi2'".format(a2_book))
            mycon.commit()
            mycursor.execute("select * from MOVIES")
            for x in mycursor:
                print('\n',j,')',"MOVIE       :",x[1],'\n',"    GENRE       :",x[2],'\n',"    RATING      :",x[3],'\n',"    RUNNING TIME:",x[4],'\n',"    DESCRIPTION :",x[5],'\n',"    CAST        :",x[6])
                j+=1

        elif delmo==3:
            try:
                det="update MOVIES set MOVIE_NAME='{}',GENRE='{}',RATING={},RUNNING_TIME='{}',DESCRIPTION='{}',CAST='{}' where SNO=3".format(mname,gen,rate,time,des,cast)
                mt="update theatre set MOVIE='{}' where AUDI='Audi3'".format(mname)
                trunc1="truncate table AUDI_3"          #deleting the records of previous movie
                trunc2="truncate table SEATAUDI_3"
                mycursor.execute(det)
                mycursor.execute(mt)
                mycursor.execute(trunc1)
                mycursor.execute(trunc2)
                mycon.commit()
            except:
                mycon.rollback()
            j=1
            mycursor.execute("select count(seat) from seataudi_3")
            for x in mycursor :
                a1_book=x[0]
            mycursor.execute("update theatre set BOOKED_SEAT={} where AUDI='Audi3'".format(a3_book))
            mycon.commit()
            mycursor.execute("select * from MOVIES")
            for x in mycursor:
                print('\n',j,')',"MOVIE       :",x[1],'\n',"    GENRE       :",x[2],'\n',"    RATING      :",x[3],'\n',"    RUNNING TIME:",x[4],'\n',"    DESCRIPTION :",x[5],'\n',"    CAST        :",x[6])
                j+=1



def update_movie():
    import mysql          #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    j=1
    mycursor.execute("select * from MOVIES")
    for x in mycursor:
        print('\n',j,')',"MOVIE       :",x[1],'\n',"    GENRE       :",x[2],'\n',"    RATING      :",x[3],'\n',"    RUNNING TIME:",x[4],'\n',"    DESCRIPTION :",x[5],'\n',"    CAST        :",x[6])
        j+=1
    upd_mo=int(input("\nENTER MOVIE NUMBER TO UPDATE MOVIE\n>"))    
    if upd_mo==1:
        mycursor.execute("select MOVIE from theatre where AUDI='Audi1'")
        for x in mycursor:
            sel=x[0]
        mycursor.execute("select * from movies where MOVIE_NAME='{}'".format(sel))
        for x in mycursor:
            print(x)
        ch='y'
        while ch.lower()=='y':
            print("\n1)MOVIE NAME")
            print("2)GENRE")
            print("3)RATING")
            print("4)RUNNING TIME")
            print("5)DESCRIPTION")
            print("6)CAST")
            c=int(input("\nWHAT DO YOU WANT TO UPDATE?"))    #updating the details of movie
            if c==1:
                mnam=input("ENTER MOVIE NAME\n>")
                try:
                    m="update MOVIES set MOVIE_NAME='{}' where SNO=1".format(mnam)
                    mt="update theatre set MOVIE='{}' where AUDI='Audi1'".format(mnam)
                    mycursor.execute(m)
                    mycursor.execute(mt)
                    mycon.commit()
                    print("\n***MOVIE NAME UPDATED***")
                except:
                    mycon.rollback()
            elif c==2:
                mgen=input("ENTER MOVIE GENRE\n>")
                try:
                    g="update MOVIES set GENRE='{}' where SNO=1".format(mgen)
                    mycursor.execute(g)
                    mycon.commit()
                    print("\n***MOVIE GENRE UPDATED***")
                except:
                    mycon.rollback()
            elif c==3:
                mrate=float(input("ENTER MOVIE RATING\n>"))
                try:
                    r="update MOVIES set RATING={} where SNO=1".format(mrate)
                    mycursor.execute(r)
                    mycon.commit()
                    print("\n***MOVIE RATING UPDATED***")
                except:
                    mycon.rollback()
            elif c==4:
                mrt=input("ENTER MOVIE RUNNING TIME\n>")
                try:
                    rt="update MOVIES set RUNNING_TIME='{}' where SNO=1".format(mrt)
                    mycursor.execute(rt)
                    mycon.commit()
                    print("\n***MOVIE RUNNING TIME UPDATED***")
                except:
                    mycon.rollback()
            elif c==5:
                mdes=input("ENTER MOVIE DESCRIPTION\n>")
                try:
                    d="update MOVIES set DESCRIPTION='{}' where SNO=1".format(mdes)
                    mycursor.execute(d)
                    mycon.commit()
                    print("\n***MOVIE DESCRIPTION UPDATED***")
                except:
                    mycon.rollback()
            elif c==6:
                mcast=input("ENTER MOVIE CAST\n>")
                try:
                    ct="update MOVIES set CAST='{}' where SNO=1".format(mcast)
                    mycursor.execute(ct)
                    mycon.commit()
                    print("\n***MOVIE CAST UPDATED***")
                except:
                    mycon.rollback()
            else:
                print("\nWRONG INPUT. PLEASE CHOOSE CORRECT CATEGORY.")
            ch=input("\nDO YOU WANT TO KEEP UPDATING?(Y/N)")
    elif upd_mo==2:
        mycursor.execute("select MOVIE from theatre where AUDI='Audi2'")
        for x in mycursor:
            sel=x[0]
        mycursor.execute("select * from movies where MOVIE_NAME='{}'".format(sel))
        for x in mycursor:
            print(x)
        ch='y'
        while ch.lower()=='y':
            print("\n1)MOVIE NAME")
            print("2)GENRE")
            print("3)RATING")
            print("4)RUNNING TIME")
            print("5)DESCRIPTION")
            print("6)CAST")
            c=int(input("\nWHAT DO YOU WANT TO UPDATE?"))
            if c==1:
                mnam=input("ENTER MOVIE NAME\n>")
                try:
                    m="update MOVIES set MOVIE_NAME='{}' where SNO=2".format(mnam)
                    mt="update theatre set MOVIE='{}' where AUDI='Audi2'".format(mnam)
                    mycursor.execute(m)
                    mycon.commit()
                    print("\n***MOVIE NAME UPDATED***")
                except:
                    mycon.rollback()
            elif c==2:
                mgen=input("ENTER MOVIE GENRE\n>")
                try:
                    g="update MOVIES set GENRE='{}' where SNO=2".format(mgen)
                    mycursor.execute(g)
                    mycon.commit()
                    print("\n***MOVIE GENRE UPDATED***")
                except:
                    mycon.rollback()
            elif c==3:
                mrate=float(input("ENTER MOVIE RATING\n>"))
                try:
                    r="update MOVIES set RATING={} where SNO=2 ".format(mrate)
                    mycursor.execute(r)
                    mycon.commit()
                    print("\n***MOVIE RATING UPDATED***")
                except:
                    mycon.rollback()
            elif c==4:
                mrt=input("ENTER MOVIE RUNNING TIME\n>")
                try:
                    rt="update MOVIES set RUNNING_TIME='{}' where SNO=2'".format(mrt)
                    mycursor.execute(rt)
                    mycon.commit()
                    print("\n***MOVIE RUNNING TIME UPDATED***")
                except:
                    mycon.rollback()
            elif c==5:
                mdes=input("ENTER MOVIE DESCRIPTION\n>")
                try:
                    d="update MOVIES set DESCRIPTION='{}' where SNO=2".format(mdes)
                    mycursor.execute(d)
                    mycon.commit()
                    print("\n***MOVIE DESCRIPTION UPDATED***")
                except:
                    mycon.rollback()
            elif c==6:
                mcast=input("ENTER MOVIE CAST\n>")
                try:
                    ct="update MOVIES set CAST='{}' where SNO=2".format(mcast)
                    mycursor.execute(ct)
                    mycon.commit()
                    print("\n***MOVIE CAST UPDATED***")
                except:
                    mycon.rollback()
            else:
                print("\nWRONG INPUT. PLEASE CHOOSE CORRECT CATEGORY.")
            ch=input("\nDO YOU WANT TO KEEP UPDATING?(Y/N)")
    elif upd_mo==3:
        mycursor.execute("select MOVIE from theatre where AUDI='Audi3'")
        for x in mycursor:
            sel=x[0]
        mycursor.execute("select * from movies where MOVIE_NAME='{}'".format(sel))
        for x in mycursor:
            print(x)
        ch='y'
        while ch.lower()=='y':
            print("\n1)MOVIE NAME")
            print("2)GENRE")
            print("3)RATING")
            print("4)RUNNING TIME")
            print("5)DESCRIPTION")
            print("6)CAST")
            c=int(input("\nWHAT DO YOU WANT TO UPDATE?"))
            if c==1:
                mnam=input("ENTER MOVIE NAME\n>")
                try:
                    m="update MOVIES set MOVIE_NAME='{}' where SNO=3".format(mnam)
                    mt="update theatre set MOVIE='{}' where AUDI='Audi3'".format(mnam)
                    mycursor.execute(m)
                    mycon.commit()
                    print("\n***MOVIE NAME UPDATED***")
                except:
                    mycon.rollback()
            elif c==2:
                mgen=input("ENTER MOVIE GENRE\n>")
                try:
                    g="update MOVIES set GENRE='{}' where SNO=3 ".format(mgen)
                    mycursor.execute(g)
                    mycon.commit()
                    print("\n***MOVIE GENRE UPDATED***")
                except:
                    mycon.rollback()
            elif c==3:
                mrate=float(input("ENTER MOVIE RATING\n>"))
                try:
                    r="update MOVIES set RATING={} where SNO=3".format(mrate)
                    mycursor.execute(r)
                    mycon.commit()
                    print("\n***MOVIE RATING UPDATED***")
                except:
                    mycon.rollback()
            elif c==4:
                mrt=input("ENTER MOVIE RUNNING TIME\n>")
                try:
                    rt="update MOVIES set RUNNING_TIME='{}' where SNO=3 ".format(mrt)
                    mycursor.execute(rt)
                    mycon.commit()
                    print("\n***MOVIE RUNNING TIME UPDATED***")
                except:
                    mycon.rollback()
            elif c==5:
                mdes=input("ENTER MOVIE DESCRIPTION\n>")
                try:
                    d="update MOVIES set DESCRIPTION='{}' where SNO=3".format(mdes)
                    mycursor.execute(d)
                    mycon.commit()
                    print("\n***MOVIE DESCRIPTION UPDATED***")
                except:
                    mycon.rollback()
            elif c==6:
                mcast=input("ENTER MOVIE CAST\n>")
                try:
                    ct="update MOVIES set CAST='{}' where SNO=3".format(mcast)
                    mycursor.execute(ct)
                    mycon.commit()
                    print("\n***MOVIE CAST UPDATED***")
                except:
                    mycon.rollback()
            else:
                print("\nWRONG INPUT. PLEASE CHOOSE CORRECT CATEGORY.")
            ch=input("\nDO YOU WANT TO KEEP UPDATING?(Y/N)")
                


    
def theatre():
    import mysql #connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    '''an1='Audi1'
    an2='Audi2'
    an3='Audi3'
    cap1=196
    cap2=216
    cap3=216

    try:
        v="insert into theatre(AUDI,CAPACITY) values('{}',{})".format(an1,cap1)
        mycursor.execute(v)
        mycon.commit()
    except:
        mycon.rollback()
    try:
        y="insert into theatre(AUDI,CAPACITY) values('{}',{})".format(an2,cap2)
        mycursor.execute(y)
        mycon.commit()
    except:
        mycon.rollback()
    try:
        z="insert into theatre(AUDI,CAPACITY) values('{}',{})".format(an3,cap3)
        mycursor.execute(z)
        mycon.commit()
    except:
        mycon.rollback()'''
    

    mycursor.execute("select count(seat) from seataudi_1")
    for x in mycursor :
        a1_book=x[0]
        
    mycursor.execute("select count(seat) from seataudi_2")
    for x in mycursor :
        a2_book=x[0]
        
    mycursor.execute("select count(seat) from seataudi_3")
    for x in mycursor :
        a3_book=x[0]
       


    mycursor.execute("select MOVIE_NAME from movies where SNO=1")
    for x in mycursor:
        mov1=x[0]
    mycursor.execute("select MOVIE_NAME from movies where SNO=2")
    for x in mycursor:
        mov2=x[0]
    mycursor.execute("select MOVIE_NAME from movies where SNO=3")
    for x in mycursor:
        mov3=x[0]

    try:
        mycursor.execute("update theatre set MOVIE='{}' where AUDI='Audi1'".format(mov1))
        mycursor.execute("update theatre set MOVIE='{}' where AUDI='Audi2'".format(mov2))
        mycursor.execute("update theatre set MOVIE='{}' where AUDI='Audi3'".format(mov3))
        mycon.commit()
    except:
        mycon.rollback()
        

    try:
        mycursor.execute("update theatre set BOOKED_SEAT={} where AUDI='Audi1'".format(a1_book))
        mycursor.execute("update theatre set BOOKED_SEAT={} where AUDI='Audi2'".format(a2_book))
        mycursor.execute("update theatre set BOOKED_SEAT={} where AUDI='Audi3'".format(a3_book))
        mycon.commit()
    except:
        mycon.rollback()

    mycursor.execute("select * from theatre")
    for x in mycursor:
        print('\n',x[0],')',"AUDI       :",x[1],'\n',"    MOVIE      :",x[2],'\n',"    CAPACITY   :",x[3],'\n',"    BOOKED SEAT:",x[4])
    
    





def show_details():
    import mysql#connecting python with mysql
    import mysql.connector as mys
    mycon=mys.connect(host='localhost',user='root',passwd='heist',database='CINEMA')
    mycursor=mycon.cursor()
    c='y'
    while c.lower()=='y':
        print("  AUDITORIUMS:\n\t1.AUDI_1\n\t2.AUDI_2\n\t3.AUDI_3")
        no=int(input("\nENTER TO SEE DETAILS OF CUSTOMERS:"))        #displayling details of customers
        if no==1:
            mycursor.execute("select * from AUDI_1")
            p=1
            print()
            print("_"*135)
            print("%4s"%"SNO","%30s"%"NAME","%25s"%"EMAIL","%15s"%"PHONE NUMBER","%15s"%"TOTAL SEATS","%23s"%"SEATS","%13s"%"SUBTOTAL")
            print("_"*135)
            print()
            for x in mycursor:
                print("%3s"%p,"%30s"%x[1],"%25s"%x[2],"%15s"%x[3],"%10s"%x[4],"%30s"%x[5],"%10s"%x[6])
                p+=1
            print("_"*135)
            mycursor.execute("select count(*) from AUDI_1")
            for x in mycursor:
                print('\nTOTAL RECORDS:',x[0])
        elif no==2:
            mycursor.execute("select * from AUDI_2")
            p=1
            print()
            print("_"*135)
            print("%4s"%"SNO","%30s"%"NAME","%25s"%"EMAIL","%15s"%"PHONE NUMBER","%15s"%"TOTAL SEATS","%23s"%"SEATS","%13s"%"SUBTOTAL")
            print("_"*135)
            print()
            for x in mycursor:
                print("%3s"%p,"%30s"%x[1],"%25s"%x[2],"%15s"%x[3],"%10s"%x[4],"%30s"%x[5],"%10s"%x[6])
                p+=1
            print("_"*135)
            mycursor.execute("select count(*) from AUDI_2")
            for x in mycursor:
                print('\nTOTAL RECORDS:',x[0])
        elif no==3:
            mycursor.execute("select * from AUDI_3")
            p=1
            print()
            print("_"*135)
            print("%4s"%"SNO","%30s"%"NAME","%25s"%"EMAIL","%15s"%"PHONE NUMBER","%15s"%"TOTAL SEATS","%23s"%"SEATS","%13s"%"SUBTOTAL")
            print("_"*135)
            print()
            for x in mycursor:
                print("%3s"%p,"%30s"%x[1],"%25s"%x[2],"%15s"%x[3],"%10s"%x[4],"%30s"%x[5],"%10s"%x[6])
                p+=1
            print("_"*135)
            mycursor.execute("select count(*) from AUDI_3")
            for x in mycursor:
                print('\nTOTAL RECORDS:',x[0])
        c=input("\n\t\t\tDo you want to continue to see details of customers(Y/N)?")








#MAIN PROGRAM 
#theatre name
title()
choice="y"
while choice.lower()=="y":
    a_c=int(input('\n\nLOGIN AS: \n\t1)CUSTOMER \n\t2)ADMINISTRATOR\n>'))

    if a_c==1:
        b_c=int(input("\nDO YOU WANT TO: \n\t1)BOOK TICKET(S) \n\t2)CANCEL TICKET(S)\n>"))
        if b_c==1:
            print("\nMOVIES PLAYING")
            print("---------------")
            movies_playing()
            sel_movie=int(input("\n\nWHICH MOVIE DO YOU WANT TO WATCH?"))
            if sel_movie==1:
                Audi1()
            elif sel_movie==2:
                Audi2()
            elif sel_movie==3:
                Audi3()
        elif b_c==2:
            cancellation()
    elif a_c==2:
        ch='y'
        while ch.lower()=='y':
            adm=int(input("\nDO YOU WANT TO: \n\t1)ADD MOVIE \n\t2)VIEW CUSTOMERS' DETAILS\n\t3)UPDATE MOVIE DETAILS\n\t4)VIEW AUDITORIUMS' DETAILS\n\t5)ADD NEW MOVIE(when three movies are already there)\n>"))
            if adm==1:
                add_movie()
            elif adm==2:
                show_details()
            elif adm==3:
                update_movie()
            elif adm==4:
                theatre()
            elif adm==5:
                add_newmovie()
            ch=input("\nDo you want to continue as ADMIN(Y/N)?")
    choice=input("\nDO YOU WANT TO START FROM BEGINNING(Y/N)?")
        
        
        
    
    
 
