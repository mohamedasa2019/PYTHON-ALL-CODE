
import urllib.request,json
def main():
    data=urllib.request.urlopen("http://awlady.codanyon.com/api/getTypes").read()
    jsonr=json.loads(data.decode("utf-8"))
    print(jsonr,type(jsonr))
    for row in jsonr:      # for row in json['يكتب اسم الليست اي الاراي ']:
        print(row)    #اكسس علي البيانات كلها
        print(row['name'])        # اكسس علي ال name فقط














if __name__ == '__main__': main()
