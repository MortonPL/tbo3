from pytest import raises
from project.customers.models import Customer

def test_customer_simple():
    """Pass: All data is valid."""
    Customer("Name", "City", 18, "00010100008", "Street", "AppNo")

# Customer name tests

def test_customer_name_not_string():
    """Fail: Name must be a string."""
    with raises(Exception) as _info:
        Customer(124687, "City", 18, "00010100008", "Street", "AppNo")

def test_customer_name_empty():
    """Fail: Name must not be empty."""
    with raises(Exception) as _info:
        Customer("", "City", 18, "00010100008", "Street", "AppNo")

def test_customer_name_min():
    """Pass: Name can be at least 1 character long."""
    Customer("A", "City", 18, "00010100008", "Street", "AppNo")

def test_customer_name_max():
    """Pass: Name can be at most 64 characters long."""
    Customer("A" * 64, "City", 18, "00010100008", "Street", "AppNo")

def test_customer_name_over_limit():
    """Fail: Name must be at most 64 characters long."""
    with raises(Exception) as _info:
        Customer("A" * 65, "City", 18, "00010100008", "Street", "AppNo")

def test_customer_name_over_limit_extreme():
    """Fail: Name must be at most 64 characters long."""
    with raises(Exception) as _info:
        Customer("A" * 10000, "City", 18, "00010100008", "Street", "AppNo")

'''
def test_customer_name_not_unique():
    """Fail: Name must be unique."""
    with raises(Exception) as _info:
        Customer("A", "City", 18, "00010100008", "Street", "AppNo")
        Customer("B", "City", 18, "00010100008", "Street", "AppNo")
'''

def test_customer_name_legal_chars():
    """Pass: Name can contain any Latin script characters."""
    Customer("ABCDEFGHJIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "City", 18, "00010100008", "Street", "AppNo")

def test_customer_name_illegal_chars():
    """Fail: Name must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("[]ds;g\"hk:j<br>000", "City", 18, "00010100008", "Street", "AppNo")

def test_customer_name_illegal_xml():
    """Fail: Name must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("<script>window.alert(\"e\")</script>", "City", 18, "00010100008", "Street", "AppNo")

def test_customer_name_illegal_sql():
    """Fail: Name must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("\" OR 1=1;--", "City", 18, "00010100008", "Street", "AppNo")

# Customer city tests

def test_customer_city_not_string():
    """Fail: City must be a string."""
    with raises(Exception) as _info:
        Customer("Name", 298357, 18, "00010100008", "Street", "AppNo")

def test_customer_city_empty():
    """Fail: City must not be empty."""
    with raises(Exception) as _info:
        Customer("Name", "", 18, "00010100008", "Street", "AppNo")

def test_customer_city_min():
    """Pass: Name can be at least 1 character long."""
    Customer("Name", "A", 18, "00010100008", "Street", "AppNo")

def test_customer_city_max():
    """Pass: Name can be at most 64 characters long."""
    Customer("Name", "A" * 64, 18, "00010100008", "Street", "AppNo")

def test_customer_city_over_limit():
    """Fail: City must be at most 64 characters long."""
    with raises(Exception) as _info:
        Customer("Names", "A" * 65, 18, "00010100008", "Street", "AppNo")

def test_customer_city_over_limit_extreme():
    """Fail: City must be at most 64 characters long."""
    with raises(Exception) as _info:
        Customer("Names", "A" * 10000, 18, "00010100008", "Street", "AppNo")

def test_customer_city_legal_chars():
    """Pass: City can contain any Latin script characters."""
    Customer("Name", "ABCDEFGHJIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 18, "00010100008", "Street", "AppNo")

def test_customer_city_illegal_chars():
    """Fail: City must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "[]ds;g\"hk:j<br>000", 18, "00010100008", "Street", "AppNo")

def test_customer_city_illegal_xml():
    """Fail: City must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "<script>window.alert(\"e\")</script>", 18, "00010100008", "Street", "AppNo")

def test_customer_city_illegal_sql():
    """Fail: City must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "\" OR 1=1;--", 18, "00010100008", "Street", "AppNo")

# Customer age tests

def test_customer_age_not_number():
    """Fail: Age must be a number."""
    with raises(Exception) as _info:
        Customer("Name", "City", "basjfh", "00010100008", "Street", "AppNo")

def test_customer_age_not_integer():
    """Fail: Age must be an integer."""
    with raises(Exception) as _info:
        Customer("Name", "City", 1.5, "00010100008", "Street", "AppNo")

def test_customer_age_negative():
    """Fail: Age must not be negative."""
    with raises(Exception) as _info:
        Customer("Name", "", -1, "00010100008", "Street", "AppNo")

def test_customer_age_too_old():
    """Fail: Age must not be over 130 years."""
    with raises(Exception) as _info:
        Customer("Name", "", 131, "00010100008", "Street", "AppNo")

# Customer PESEL tests

def test_customer_pesel_not_string():
    """Fail: PESEL must be a string."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, 298357, "Street", "AppNo")

def test_customer_pesel_empty():
    """Fail: PESEL must not be empty."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "", "Street", "AppNo")

def test_customer_pesel_good():
    """Pass: PESEL must be exactly 11 characters long."""
    Customer("Name", "City", 18, "00010100008", "Street", "AppNo")

def test_customer_pesel_under_limit():
    """Fail: PESEL must be exactly 11 characters long."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "0", "Street", "AppNo")

def test_customer_pesel_over_limit():
    """Fail: PESEL must be exactly 11 characters long."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "000000000000", "Street", "AppNo")

def test_customer_pesel_over_limit_extreme():
    """Fail: PESEL must be exactly 11 characters long."""
    with raises(Exception) as _info:
        Customer("Names", "City", 18, "0" * 10000, "Street", "AppNo")

def test_customer_pesel_legal_chars():
    """Pass: PESEL can contain any digits."""
    Customer("Name", "City", 18, "45230167897", "Street", "AppNo")

def test_customer_pesel_illegal_chars():
    """Fail: PESEL must contain only digits."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "ABCDEFGHIJ", "Street", "AppNo")

def test_customer_pesel_illegal_xml():
    """Fail: PESEL must contain only digits."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "<script>window.alert(\"e\")</script>", "Street", "AppNo")

def test_customer_pesel_illegal_sql():
    """Fail: PESEL must contain only digits."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "\" OR 1=1;--", "Street", "AppNo")

def test_customer_pesel_good_month():
    """Pass: PESEL month can be in ranges [80-92], [00-12], [20-32], [40-52], [60-72]."""
    Customer("Name", "City", 18, "00000100007", "Street", "AppNo")
    Customer("Name", "City", 18, "00010100008", "Street", "AppNo")
    Customer("Name", "City", 18, "00020100009", "Street", "AppNo")
    Customer("Name", "City", 18, "00030100000", "Street", "AppNo")
    Customer("Name", "City", 18, "00040100001", "Street", "AppNo")
    Customer("Name", "City", 18, "00050100002", "Street", "AppNo")
    Customer("Name", "City", 18, "00060100003", "Street", "AppNo")
    Customer("Name", "City", 18, "00070100004", "Street", "AppNo")
    Customer("Name", "City", 18, "00080100005", "Street", "AppNo")
    Customer("Name", "City", 18, "00090100006", "Street", "AppNo")
    Customer("Name", "City", 18, "00100100000", "Street", "AppNo")
    Customer("Name", "City", 18, "00110100001", "Street", "AppNo")
    Customer("Name", "City", 18, "00120100002", "Street", "AppNo")
    Customer("Name", "City", 18, "00200100003", "Street", "AppNo")
    Customer("Name", "City", 18, "00210100004", "Street", "AppNo")
    Customer("Name", "City", 18, "00220100005", "Street", "AppNo")
    Customer("Name", "City", 18, "00230100006", "Street", "AppNo")
    Customer("Name", "City", 18, "00240100007", "Street", "AppNo")
    Customer("Name", "City", 18, "00250100008", "Street", "AppNo")
    Customer("Name", "City", 18, "00260100009", "Street", "AppNo")
    Customer("Name", "City", 18, "00270100000", "Street", "AppNo")
    Customer("Name", "City", 18, "00280100001", "Street", "AppNo")
    Customer("Name", "City", 18, "00290100002", "Street", "AppNo")
    Customer("Name", "City", 18, "00300100006", "Street", "AppNo")
    Customer("Name", "City", 18, "00310100007", "Street", "AppNo")
    Customer("Name", "City", 18, "00320100008", "Street", "AppNo")
    Customer("Name", "City", 18, "00400100009", "Street", "AppNo")
    Customer("Name", "City", 18, "00410100000", "Street", "AppNo")
    Customer("Name", "City", 18, "00420100001", "Street", "AppNo")
    Customer("Name", "City", 18, "00430100002", "Street", "AppNo")
    Customer("Name", "City", 18, "00440100003", "Street", "AppNo")
    Customer("Name", "City", 18, "00450100004", "Street", "AppNo")
    Customer("Name", "City", 18, "00460100005", "Street", "AppNo")
    Customer("Name", "City", 18, "00470100006", "Street", "AppNo")
    Customer("Name", "City", 18, "00480100007", "Street", "AppNo")
    Customer("Name", "City", 18, "00490100008", "Street", "AppNo")
    Customer("Name", "City", 18, "00500100002", "Street", "AppNo")
    Customer("Name", "City", 18, "00510100003", "Street", "AppNo")
    Customer("Name", "City", 18, "00520100004", "Street", "AppNo")
    Customer("Name", "City", 18, "00600100005", "Street", "AppNo")
    Customer("Name", "City", 18, "00610100006", "Street", "AppNo")
    Customer("Name", "City", 18, "00620100007", "Street", "AppNo")
    Customer("Name", "City", 18, "00630100008", "Street", "AppNo")
    Customer("Name", "City", 18, "00640100009", "Street", "AppNo")
    Customer("Name", "City", 18, "00650100000", "Street", "AppNo")
    Customer("Name", "City", 18, "00660100001", "Street", "AppNo")
    Customer("Name", "City", 18, "00670100002", "Street", "AppNo")
    Customer("Name", "City", 18, "00680100003", "Street", "AppNo")
    Customer("Name", "City", 18, "00690100004", "Street", "AppNo")
    Customer("Name", "City", 18, "00700100008", "Street", "AppNo")
    Customer("Name", "City", 18, "00710100009", "Street", "AppNo")
    Customer("Name", "City", 18, "00720100000", "Street", "AppNo")
    Customer("Name", "City", 18, "00800100001", "Street", "AppNo")
    Customer("Name", "City", 18, "00810100002", "Street", "AppNo")
    Customer("Name", "City", 18, "00820100003", "Street", "AppNo")
    Customer("Name", "City", 18, "00830100004", "Street", "AppNo")
    Customer("Name", "City", 18, "00840100005", "Street", "AppNo")
    Customer("Name", "City", 18, "00850100006", "Street", "AppNo")
    Customer("Name", "City", 18, "00860100007", "Street", "AppNo")
    Customer("Name", "City", 18, "00870100008", "Street", "AppNo")
    Customer("Name", "City", 18, "00880100009", "Street", "AppNo")
    Customer("Name", "City", 18, "00890100000", "Street", "AppNo")
    Customer("Name", "City", 18, "00900100004", "Street", "AppNo")
    Customer("Name", "City", 18, "00910100005", "Street", "AppNo")
    Customer("Name", "City", 18, "00920100006", "Street", "AppNo")

def test_customer_pesel_bad_month():
    """Fail: PESEL month must be in ranges [80-92], [00-12], [20-32], [40-52], [60-72]."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00930100007", "Street", "AppNo")
        Customer("Name", "City", 18, "00940100008", "Street", "AppNo")
        Customer("Name", "City", 18, "00950100009", "Street", "AppNo")
        Customer("Name", "City", 18, "00960100000", "Street", "AppNo")
        Customer("Name", "City", 18, "00970100001", "Street", "AppNo")
        Customer("Name", "City", 18, "00980100002", "Street", "AppNo")
        Customer("Name", "City", 18, "00990100003", "Street", "AppNo")
        Customer("Name", "City", 18, "00130100003", "Street", "AppNo")
        Customer("Name", "City", 18, "00140100004", "Street", "AppNo")
        Customer("Name", "City", 18, "00150100005", "Street", "AppNo")
        Customer("Name", "City", 18, "00160100006", "Street", "AppNo")
        Customer("Name", "City", 18, "00170100007", "Street", "AppNo")
        Customer("Name", "City", 18, "00180100008", "Street", "AppNo")
        Customer("Name", "City", 18, "00190100009", "Street", "AppNo")
        Customer("Name", "City", 18, "00330100009", "Street", "AppNo")
        Customer("Name", "City", 18, "00340100000", "Street", "AppNo")
        Customer("Name", "City", 18, "00350100001", "Street", "AppNo")
        Customer("Name", "City", 18, "00360100002", "Street", "AppNo")
        Customer("Name", "City", 18, "00370100003", "Street", "AppNo")
        Customer("Name", "City", 18, "00380100004", "Street", "AppNo")
        Customer("Name", "City", 18, "00390100005", "Street", "AppNo")
        Customer("Name", "City", 18, "00530100005", "Street", "AppNo")
        Customer("Name", "City", 18, "00540100006", "Street", "AppNo")
        Customer("Name", "City", 18, "00550100007", "Street", "AppNo")
        Customer("Name", "City", 18, "00560100008", "Street", "AppNo")
        Customer("Name", "City", 18, "00570100009", "Street", "AppNo")
        Customer("Name", "City", 18, "00580100000", "Street", "AppNo")
        Customer("Name", "City", 18, "00590100001", "Street", "AppNo")
        Customer("Name", "City", 18, "00730100001", "Street", "AppNo")
        Customer("Name", "City", 18, "00740100002", "Street", "AppNo")
        Customer("Name", "City", 18, "00750100003", "Street", "AppNo")
        Customer("Name", "City", 18, "00760100004", "Street", "AppNo")
        Customer("Name", "City", 18, "00770100005", "Street", "AppNo")
        Customer("Name", "City", 18, "00780100006", "Street", "AppNo")
        Customer("Name", "City", 18, "00790100007", "Street", "AppNo")

def test_customer_pesel_good_day():
    """Pass: PESEL day can be in range [01-31], [01-30], [01-28], [01-29], depending on the month."""
    Customer("Name", "City", 18, "00400100009", "Street", "AppNo")

def test_customer_pesel_bad_day():
    """Fail: PESEL day must be in range [01-31], [01-30], [01-28], [01-29], depending on the month."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00000000000", "Street", "AppNo")
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00013200002", "Street", "AppNo")

def test_customer_pesel_bad_control():
    """Fail: PESEL control number must be correct."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00400100000", "Street", "AppNo")

# Customer street tests

def test_customer_street_not_string():
    """Fail: Street must be a string."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", 298357, "AppNo")

def test_customer_street_empty():
    """Fail: Street must not be empty."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "", "AppNo")

def test_customer_street_min():
    """Pass: Street can be at least 1 character long."""
    Customer("Name", "City", 18, "00010100008", "A", "AppNo")

def test_customer_street_max():
    """Pass: Street can be at most 128 characters long."""
    Customer("Name", "City", 18, "00010100008", "A" * 128, "AppNo")

def test_customer_street_over_limit():
    """Fail: Street must be at most 128 characters long."""
    with raises(Exception) as _info:
        Customer("Names", "City", 18, "00010100008", "A" * 129, "AppNo")

def test_customer_street_over_limit_extreme():
    """Fail: Street must be at most 64 characters long."""
    with raises(Exception) as _info:
        Customer("Names", "City", 18, "00010100008", "A" * 10000, "AppNo")

def test_customer_street_legal_chars():
    """Pass: Street can contain any Latin script characters."""
    Customer("Name", "City", 18, "00010100008", "ABCDEFGHJIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "AppNo")

def test_customer_street_illegal_chars():
    """Fail: Street must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "[]ds;g\"hk:j<br>000", "AppNo")

def test_customer_street_illegal_xml():
    """Fail: Street must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "<script>window.alert(\"e\")</script>", "AppNo")

def test_customer_street_illegal_sql():
    """Fail: Street must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "\" OR 1=1;--", "AppNo")

# Customer AppNo tests

def test_customer_appno_not_string():
    """Fail: AppNo must be a string."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "Street", 298357)

def test_customer_appno_empty():
    """Fail: AppNo must not be empty."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "Street", "")

def test_customer_appno_min():
    """Pass: AppNo can be at least 1 character long."""
    Customer("Name", "City", 18, "00010100008", "Street", "A")

def test_customer_appno_max():
    """Pass: AppNo can be at most 10 characters long."""
    Customer("Name", "City", 18, "00010100008", "Street", "A" * 10)

def test_customer_appno_over_limit():
    """Fail: AppNo must be at most 10 characters long."""
    with raises(Exception) as _info:
        Customer("Names", "City", 18, "00010100008", "Street", "A" * 11)

def test_customer_appno_over_limit_extreme():
    """Fail: AppNo must be at most 64 characters long."""
    with raises(Exception) as _info:
        Customer("Names", "City", 18, "00010100008", "Street", "A" * 10000)

def test_customer_appno_legal_chars():
    """Pass: AppNo can contain any Latin script characters."""
    Customer("Name", "City", 18, "00010100008", "Street", "ABCDEFGHJI")
    Customer("Name", "City", 18, "00010100008", "Street", "KLMNOPQRST")
    Customer("Name", "City", 18, "00010100008", "Street", "UVWXYZabcd")
    Customer("Name", "City", 18, "00010100008", "Street", "efghijklmn")
    Customer("Name", "City", 18, "00010100008", "Street", "opqrstuvwx")
    Customer("Name", "City", 18, "00010100008", "Street", "yz")

def test_customer_appno_illegal_chars():
    """Fail: AppNo must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "Street", "[]ds;g\"h:0")

def test_customer_appno_illegal_xml():
    """Fail: AppNo must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "Street", "<script>window.alert(\"e\")</script>")

def test_customer_appno_illegal_sql():
    """Fail: AppNo must contain only Latin script characters."""
    with raises(Exception) as _info:
        Customer("Name", "City", 18, "00010100008", "Street", "\" OR 1=1;--")
