MULTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
def make_pesel(**kw):
    yy = kw.get("yy", "00")
    mm = kw.get("mm", "01")
    dd = kw.get("dd", "01")
    nnnn = kw.get("nnnn", "0000")
    pesel = "".join((yy, mm, dd, nnnn))
    c = sum([(int(n) * m) % 10 for n, m in zip(pesel, MULTS)])
    c = (10 - (c % 10)) % 10
    return pesel + str(c)

def gen_months(start, num, printer):
    for month in range(start, start + num + 1):
        month = f"{month:02}"
        pesel = make_pesel(mm=month)
        printer(pesel)

def gen_days(end, printer):
    for day in range(1, end):
        day = f"{day:02}"
        pesel = make_pesel(dd=day)
        printer(pesel)

def ctor_printer(s):
    print(f"Customer(\"Name\", \"City\", 18, \"{s}\", \"Street\", \"AppNo\")")


print("Good")
for i in range(0, 100, 20):
    gen_months(i, 12, ctor_printer)
print("Bad")
for i in range(13, 94, 20):
    gen_months(i, 6, ctor_printer)
