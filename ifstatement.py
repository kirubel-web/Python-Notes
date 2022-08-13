#if statement
ismale = True
istall = False
if ismale and istall:
    print("You are a tall male")
elif ismale and not(istall):
    print("You are a short male")
elif istall and not(ismale):
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall")