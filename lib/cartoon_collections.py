def roll_call_dwarves(dwarfs):
    for index, dwarf in enumerate(dwarfs):
        print("{}. {}".format(index + 1, dwarf))

def summon_captain_planet(values):
    return [value.capitalize() + "!" for value in values]

def long_planeteer_calls(words):
    status = False
    for word in words:
        if len(word) > 4:
            status = True
            break
    return status

def find_the_cheese(cheeses):
    cheese_set = set(cheeses)
    cheese_check = {"cheddar", "gouda", "camembert"}
    answer = cheese_set & cheese_check
    try:
        return answer.pop()
    except:
        return None
