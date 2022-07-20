from connect import Cur, Conn
import random as r


def Add():
    player_id = int(input("Enter the player Id : "))
    ans = Yesno(player_id)
    if ans == 0:
        name = input("Enter the name of player : \n")
        matches = int(input("Enter the number of matches : \n"))
        inn = int(input("Enter the innings : \n"))
        Runs = int(input("Enter the total runs : \n"))
        Pavg = float(input("Enter the average runs : \n"))
        Hund = int(input("Enter the hundreds of the player : \n"))
        fif = int(input("Enter the fifties of the player : \n"))
        Zeroes = int(input("Enter the zeroes : \n"))
        info = f"insert into icc values({player_id},'{name}','{matches}','{inn}','{Runs}','{Pavg}'," \
               f"'{Hund}','{fif}','{Zeroes}');"
        Cur.execute(info)
        Conn.commit()
        print(f"Record added with Player ID : {player_id}")
    else:
        print("Player ID already exists!")


def Modify():
    print("The fields are :-"
          "\n1. Name"
          "\n2. Matches"
          "\n3. Innings"
          "\n4. Runs"
          "\n5. Average"
          "\n6. Hundreds"
          "\n7. Fifties"
          "\n8. Zeroes")
    num = int(input("Enter the field (1/6) you want to modify : "))
    name = input("Enter the player's Name whose record you wanna modify: ")
    Cur.execute(f"Select * from icc where name like '%{name}%';")
    a = Cur.fetchall()
    if len(a) > 0:
        print("="*103)
        print(f"{'Player ID': ^15s}{'NAME': ^26s}{'MATCHES': ^10s}{'INNINGS': ^10s}{'RUNS':^6s}{'AVERAGE':^10s}"
              f"{'HUNDREDS': ^10s}{'FIFTIES': ^10s}{'ZEROES': ^6s}")
        print("="*103)
        for i in a:
            print(f"{i[0]: ^15}{i[1]:^26}{i[2]:^10}{i[3]:^10}{i[4]:^6}{i[5]:^10}{i[6]:^10}{i[7]:^10}{i[8]:^8}")
            print("-"*103)
    id = int(input("Enter the ID of the player whose record you wanna modify : "))
    if num == 1:
        newname = input("Enter the new name: ")
        Cur.execute(f"Update ICC set Name ='{newname}' where pid = {id};")
    if num == 2:
        new_match = input("Enter new number of matches: ")
        Cur.execute(f"Update ICC set Matches ='{new_match}' where pid={id};")
    if num == 3:
        new_inns = input("Enter new number of Innings:")
        Cur.execute(f"Update ICC set Innings ='{new_inns}' where pid={id};")
    if num == 4:
        new_runs = input("Enter new number of runs:")
        Cur.execute(f"Update ICC set Runs ='{new_runs}' where pid={id};")
    if num == 5:
        new_avg = input("Enter new average: ")
        Cur.execute(f"Update ICC set Average ='{new_avg}' where pid={id};")
    if num == 6:
        new_hun = input("Enter new hundreds:")
        Cur.execute(f"Update ICC set Hundreds ='{new_hun}' where pid={id};")
    if num == 7:
        new_fif = input("Enter new fifties:")
        Cur.execute(f"Update ICC set Fifties ='{new_fif}' where pid={id};")
    if num == 8:
        new_avg = input("Enter new zeroes:")
        Cur.execute(f"Update ICC set Zeroes ='{new_avg}' where pid={id};")
    Conn.commit()
    print()
    print(f"{'RECORD MODIFIED': ^100s}")
    print()


def Search():
    a = input("Enter full Name of the cricketer : ")
    Cur.execute(f"Select * from icc where name like '%{a}%';")
    a = Cur.fetchall()
    if len(a) > 0:
        print("="*103)
        print(f"{'Player ID': ^15s}{'NAME': ^26s}{'MATCHES': ^10s}{'INNINGS': ^10s}{'RUNS':^6s}{'AVERAGE':^10s}"
              f"{'HUNDREDS': ^10s}{'FIFTIES': ^10s}{'ZEROES': ^6s}")
        print("="*103)
        for i in a:
            print(f"{i[0]: ^15}{i[1]:^26}{i[2]:^10}{i[3]:^10}{i[4]:^6}{i[5]:^10}{i[6]:^10}{i[7]:^10}{i[8]:^8}")

    else:
        print("NO RECORDS FOUND")
    for i in range(5):
        print()


def Del():
    a = input("Enter Full Name of the cricketer : ")
    Cur.execute(f"Select * from icc where name like '%{a}%';")
    a = Cur.fetchall()
    if len(a) > 0:
        print("="*103)
        print(f"{'Player ID': ^15s}{'NAME': ^26s}{'MATCHES': ^10s}{'INNINGS': ^10s}{'RUNS':^6s}{'AVERAGE':^10s}"
              f"{'HUNDREDS': ^10s}{'FIFTIES': ^10s}{'ZEROES': ^6s}")
        print("="*103)
        for i in a:
            print(f"{i[0]: ^15}{i[1]:^26}{i[2]:^10}{i[3]:^10}{i[4]:^6}{i[5]:^10}{i[6]:^10}{i[7]:^10}{i[8]:^8}")
            print("*"*103)
        i_d = int(input("Enter the ID of the player whose record you wanna remove : "))
        ans = Yesno(i_d)
        if ans == 0:
            del_sen = f"delete from icc where pid = {i_d}"
            Cur.execute(del_sen)
            Conn.commit()
            print(" ")
            print(f"{'RECORD DELETED SUCCESSFULLY':^100s}")
    else:
        print(f"{'* NO SUCH CRICKETER FOUND! *': ^100s}")



def Yesno(pid):
    a = f"select * from icc where pid = {pid};"
    Cur.execute(a)
    record = Cur.fetchall()
    print(record)
    if len(record) == 1:
        return 1    # RECORD EXISTS
    return 0


def Random():  # r.randint(10,20)
    a = "select pid,Name,average from ICC;"
    Cur.execute(a)
    names = Cur.fetchall()
    player_lst1 = []
    player_lst2 = []
    for i in range(30):
        player_lst1.append(r.choices(names))
    for i in player_lst1:
        if len(player_lst2) <= 9:
            if i not in player_lst2:
                player_lst2.append(i)
    for i in player_lst2:
        Cur.execute(f"insert into players values({i[0][0]},'{i[0][1]}',{i[0][2]});")
    Conn.commit()


def Game():
    Random()
    a = f"select * from Players;"
    Cur.execute(a)
    p_ls1 = Cur.fetchall()
    print("="*40)
    print(f"{'Player ID': ^14}{'NAME': ^25}")
    print("="*40)
    for i in p_ls1:
        print(f"{i[0]: ^14}{i[1]: ^25}")
    p_ls2 = []
    for i in range(1, 6):
        pid = int(input(f"Enter the ID of player {i} you want in your team : "))
        p_ls2.append(pid)
    p_lst3 = tuple(p_ls2)
    for i in p_lst3:
        b = f"select pid, pname, average from players where pid = {i};"
        d = f"delete from players where pid = {i};"
        Cur.execute(b)
        c = Cur.fetchall()
        Cur.execute(d)
        for j in c:
            Cur.execute(f"insert into player1 values({j[0]},'{j[1]}',{j[2]});")
    e = f"select sum(average) from players;"
    Cur.execute(e)
    z = Cur.fetchall()
    f = f"select sum(average) from player1;"
    Cur.execute(f)
    x = Cur.fetchall()
    print()
    print("="*100)
    print(f"{'GAME RESULTS': ^100s}")
    print("="*100)
    print(f"{'YOUR SCORE : '}{z[0][0]}")
    print(f"{'AI SCORE : '}{x[0][0]}")
    print()
    if z > x:
        print(f"Congratulations! Your team won by {z[0][0]-x[0][0]} runs!")
    else:
        print(f"Oh No! Your team lost by {x[0][0]-z[0][0]} runs!")

    Cur.execute("delete from Players;")
    Cur.execute("delete from player1;")
    Conn.commit()
    print()


while True:

    print("="*100)
    print(f"{'LORDS CRICKSANITY BUZZ': ^100s}")
    print("="*100)
    print()
    print(f"{'F I L E   O P E R A T I O N S': ^100}")
    print(f"{'1. A D D': <50}")
    print(f"{'2. S E A R C H': <50}")
    print(f"{'3. M O D I F Y': <50}")
    print(f"{'4. D E L E T E' : <50}")
    print(f"{'5. G A M E': <50}")
    print(f"{'6. Q U I T': <50}")

    CH = input("Enter your Choice (1-6) : ")
    if CH == '1':
        Add()
    elif CH == '2':
        Search()
    elif CH == '3':
        Modify()
    elif CH == '4':
        Del()
    elif CH == '5':
        Game()
    elif CH == '6':
        print(

            "END OF THE GAME\n"
            "THANK YOU FOR PLAYING\n"
            "HOPE YOU ENJOYED\n"

        )
        break

    else:
        print("Wrong Input..")










