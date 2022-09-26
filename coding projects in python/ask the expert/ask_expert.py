from tkinter import Tk,simpledialog, messagebox



def read_from_file():
    with open('/home/nktirop/Desktop/coding projects in python/ask the expert/capital_data.txt.txt') as file:
        for line in file:
            line=line.rstrip('\n')
            country,city=line.split('/')
            the_world[country]=city

def write_to_file(country_name, city_name):
    with open('/home/nktirop/Desktop/coding projects in python/ask the expert/capital_data.txt.txt','a') as file:
        file.write('\n'+ country_name + '/' + city_name)


print('ask the expert - capital cities of the world')
root=Tk()
root.withdraw()
the_world ={}

read_from_file()

while True:
    query_country = simpledialog.askstring('Country','type the name of a country:')
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('answer',
                            'the capital city of' + query_country + 'is' + result + '!' )

    else:
        new_city=simpledialog.askstring('teach me'
                                        'i do not know!' + 
                                        'what is the capital city of' + query_country + '?')

        the_world[query_country]=new_city
        write_to_file(query_country,new_city)

root.mainloop()






    



