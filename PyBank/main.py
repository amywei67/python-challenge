import csv
import os

budgetcsv= os.path.join('budget_data.csv')
with open (budgetcsv, newline='') as file:
    budgetdata = csv.reader(file,delimiter=',')
    headerrow = next(budgetdata)
    print(f'Header:{headerrow}')
    
    data=[]
    profitslosses= []
    for item in budgetdata:
        print(item)
        data.append(item)
        profitslosses.append(int(item[1]))
    
    total_change=0
    greatest_changeprofit = 0
    greatest_changeloss = 0
    date_greatestprofitchange = ""
    date_greatestlosschange = ""

    for index in range(1,len(profitslosses)):
        change = int(profitslosses[index]) - int(profitslosses[index-1])
        total_change = total_change+change
        if change > greatest_changeprofit:
            greatest_changeprofit=change
            date_greatestprofitchange = data[index][0]
        if change < greatest_changeloss:
            greatest_changeloss = change    
            date_greatestlosschange = data[index][0]
        
    average_change = float(total_change/(len(profitslosses)-1))



    print(f'Total Months:{len(data)}')
    print(f'Total: ${sum(profitslosses)}')
    print(f'Average Change:${str(round(average_change,2))}')
    print(f'Greatest Increace in Profit:{date_greatestprofitchange}(${greatest_changeprofit})')
    print(f'Greatest Decrease in Loss:{date_greatestlosschange}(${greatest_changeloss})')

output_file = "Python_HW_PyBank_Output.txt"
with open(output_file,'w') as filevariable: 
	filevariable.write( "--------------------------\n")
	filevariable.write( "--- Financial Analysis ---\n")
	filevariable.write( "--------------------------\n")
	filevariable.write( "Total Months: " + str(len(data)))
	filevariable.write( "\nNet Total: $" + str(sum(profitslosses)))
	filevariable.write( "\nAverage Change: $" + str(average_change))
	filevariable.write( "\nGreatest Increase in Profits: " + str(date_greatestprofitchange) + " $" + str(greatest_changeprofit))
	filevariable.write( "\nGreatest Decrease in Profits: " + str(date_greatestlosschange) + " $" + str(greatest_changeloss))
	
