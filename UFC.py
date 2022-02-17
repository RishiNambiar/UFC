from bs4 import BeautifulSoup
import requests

q = True

while q:

    print("""
                You have three options:
        1 - See list of champions in each division
        2 - Find details of any fighter
        3 - See fights in a UFC card
        4 - quit
    """) 

    run = True

    while run:
        pick = input("Pick an input(1/2/3/4): ")

        try:
            pick = int(pick)
            if pick <= 4:
                run = False
            else:
                print("Enter a number between 1 and 4: ")

        except ValueError:
            print("Enter a number between 1 and 4: ")


    if pick == 1:

        url = "https://www.ufc.com/athletes"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")

        div = doc.find(class_ = "views-element-container block block-views block-views-blockathletes-titleholders-block-1")

        athelete_blocks = doc.find_all(class_ = "node node--type-athlete node--view-mode-listing-detail clearfix athlete-listing-detail-wrp")

        for athelete in athelete_blocks:

            division = athelete.find_all(class_ = "ath-wlcass")
            division_to_string = "".join(str(e) for e in division)
            division = division_to_string.split(">")[2].split("<")[0]
            print(f'Division: {division}')

            name = athelete.find_all(class_ = "field field--name-title field--type-string field--label-hidden")
            name_to_string = "".join(str(e) for e in name)
            name = name_to_string.split(">")[1].split("<")[0]
            print(f'Champion: {name}')

            nickname = athelete.find_all(class_ = "field field--name-nickname field--type-string field--label-hidden")
            nickname_to_string = "".join(str(e) for e in nickname)

            try:
                nickname = nickname_to_string.split(">")[2].split("<")[0]
                print(f'Nickname: {nickname}')

            except Exception as e:
                print("No Nickname :(")

            weight = athelete.find_all(class_ = "ath-weight")
            weight_to_string = "".join(str(e) for e in weight)
            weight = weight_to_string.split(">")[1].split("<")[0]
            print(f'Weight: {weight}')

            record = athelete.find_all(class_ = "c-ath--record ath-lf-fl")
            record_to_string = "".join(str(e) for e in record)
            record = record_to_string.split(">")[1].split("<")[0]
            record = record.strip()
            print(f'record: {record}')

            last_fight = athelete.find_all(class_ = "views-row")
            last_fight_to_string = "".join(str(e) for e in last_fight)
            last_fight = last_fight_to_string.split(">")[1].split("<")[0]
            print(f'Last Fight: {last_fight}')

            print("------------------------------------------")


    # ----------------------------------------------------------------------------------------

    elif pick == 2:

        name_of_fighter = input("Enter fighter name: ").lower()
        name_of_fighter = name_of_fighter.split(" ")
        name_of_fighter = list(name_of_fighter)

        if len(name_of_fighter) == 2:
            fn = name_of_fighter[0]
            ln = name_of_fighter[1]

        elif len(name_of_fighter) == 3:
            fn = name_of_fighter[0]
            mn = name_of_fighter[1]
            ln = name_of_fighter[2]

        try:

            try:
                url2 = f"https://www.ufc.com/athlete/{fn}-{mn}-{ln}"
                
            except:
                url2 = f"https://www.ufc.com/athlete/{fn}-{ln}"
                

            page = requests.get(url2).text
            doc = BeautifulSoup(page, "html.parser")
            div = doc.find(class_ = "c-bio__info-details")
            details = div.find_all(class_ = "c-bio__field")

            first = details[0]
            first = first.find(class_ = "c-bio__label").string

            first_answer = details[0]
            first_answer = first_answer.find(class_ = "c-bio__text").string

            second = details[1]
            second = second.find(class_ = "c-bio__label").string

            second_answer = details[1]
            second_answer = second_answer.find(class_ = "c-bio__text").string

            third = details[2]
            third = third.find(class_ = "c-bio__label").string

            try:
                third_answer = details[2]
                third_answer = third_answer.find(class_ = "field field--name-age field--type-integer field--label-hidden field__item").string
            except:
                third_answer = details[2]
                third_answer = third_answer.find(class_ = "c-bio__text").string

            fourth = details[3]
            fourth = fourth.find(class_ = "c-bio__label").string

            try:
                fourth_answer = details[3]
                fourth_answer = fourth_answer.find(class_ = "field field--name-age field--type-integer field--label-hidden field__item").string
            except:
                fourth_answer = details[3]
                fourth_answer = fourth_answer.find(class_ = "c-bio__text").string

            fifth = details[4]
            fifth = fifth.find(class_ = "c-bio__label").string

            try:
                fifth_answer = details[4]
                fifth_answer = fifth_answer.find(class_ = "field field--name-age field--type-integer field--label-hidden field__item").string
            except:
                fifth_answer = details[4]
                fifth_answer = fifth_answer.find(class_ = "c-bio__text").string

            sixth = details[5]
            sixth = sixth.find(class_ = "c-bio__label").string

            sixth_answer = details[5]
            sixth_answer = sixth_answer.find(class_ = "c-bio__text").string

            record = doc.find(class_ = "c-hero__headline-suffix tz-change-inner").string
            record = record.strip()
            record = record.replace("•", "")


            print(record)
            print(f"{first}: {first_answer}")
            print(f"{second}: {second_answer}")
            print(f"{third}: {third_answer}")
            print(f"{fourth}: {fourth_answer}")
            print(f"{fifth}: {fifth_answer}")
            print(f"{sixth}: {sixth_answer}")


            try:
                seventh = details[6]
                seventh = seventh.find(class_ = "c-bio__label").string

                seventh_answer = details[6]
                seventh_answer = seventh_answer.find(class_ = "c-bio__text").string
                print(f"{seventh}: {seventh_answer}")

            except:
                pass

            try:
                eigth = details[7]
                eigth = eigth.find(class_ = "c-bio__label").string

                eigth_answer = details[7]
                eigth_answer = eigth_answer.find(class_ = "c-bio__text").string
                print(f"{eigth}: {eigth_answer}")

            except:
                pass


            try:
                ninth = details[8]
                ninth = ninth.find(class_ = "c-bio__label").string

                ninth_answer = details[8]
                ninth_answer = ninth_answer.find(class_ = "c-bio__text").string
                print(ninth, ninth_answer)

            except:
                pass

        except:
            print("Enter an actual fighter's name!")

    # ----------------------------------------------------------------------------------------

    elif pick == 3:

        run = True

        while run:
            card = input("Enter a UFC card: ")

            try:
                card = int(card)
                run = False
            except ValueError:
                print("Please type in a number!")


        url3 = f"https://www.ufc.com/event/ufc-{card}"
        pagee = requests.get(url3).text
        docc = BeautifulSoup(pagee, "html.parser")


        def functionn():
            try:
                divisionn = docc.find(class_ = "l-listing--stacked--full-width")
                block = divisionn.find_all(class_ = "c-listing-fight")

                number = 0
            
                for x in range(6):
                    try:
                        x = block[number]
                        name = x.find(class_ = "c-listing-fight__detail-corner-name").string
                        name2 = name.find_next(class_ = "c-listing-fight__detail-corner-name").string

                        name = name.strip()
                        name2 = name2.strip()

                        weight_class = x.find(class_ = "c-listing-fight__class").string
                
                        roundd = x.find(class_ = "c-listing-fight__result-text round").string 

                        time = x.find(class_ = "c-listing-fight__result-text time").string 

                        method = x.find(class_ = "c-listing-fight__result-text method").string

                        print(weight_class)
                        print(f"{name} VS {name2}")
                        print(f"Round: {roundd}")
                        print(f'Time: {time}')
                        print(f'Method: {method}')

                        try:
                            try:
                                winner = docc.find(class_ = "c-listing-fight__corner--red")
                                win = winner.find(class_ = "c-listing-fight__outcome--Win").string 

                                if win:
                                    print(f"Winner: {name}")

                                else:
                                    winner = docc.find(class_ = "c-listing-fight__corner--blue")
                                    win = winner.find(class_ = "c-listing-fight__outcome--Win").string
                                    if win:
                                        print(f"Winner: {name2}")

                            except:
                                winner = docc.find(class_ = "c-listing-fight__corner--blue")
                                win = winner.find(class_ = "c-listing-fight__outcome--Win").string

                                if win:
                                    print(f"Winner: {name2}")

                                else:
                                    winner = docc.find(class_ = "c-listing-fight__corner--red")
                                    win = winner.find(class_ = "c-listing-fight__outcome--Win").string
                                    if win:
                                        print(f"Winner: {name}")
                            
                        except:
                            pass 

                        print("----------------------------------------")

                        number += 1
                        
                    except IndexError:
                        pass
            except:
                print("Something went wrong :(")

        functionn()

    else:
        q = False
        