def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        returner = ", ".join(items)
        last_comma_index = returner.rfind(",")
        returner = f"{returner[0: last_comma_index+1]} and {returner[last_comma_index + 2: len(returner)]}"
        return returner
