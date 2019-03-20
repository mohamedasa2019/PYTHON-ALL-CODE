def main():
    student=dict(name="mohamed",age=48,slary=700);
    print(student,type(student))
    student['name']="hamada"
    print(student['name'])
    print(student)
    student["color"]="red"   # to add new key
    print(student)
    del student["age"]       # to delet key
    print(student)
    student.clear()          # to delet all
    print(student)



    x=3
    z=20
    value = z+x
    value +=5
    value /=3
    value *=4
    value = z-x
    print(value)

    x=4
    z=18
    print(z%x)
    print(z/x)
    print(z//x)




    





















if __name__ == '__main__': main()







