while True:
    try:
        age = int(input("enter your age :"))
    except ValueError:
        print("may be you entered string or something instead of number,try again.")
    except:
        print("unexpected error")
    else:
        print(f"age is:{age}")
        break
    finally:
        print("finally block...")




