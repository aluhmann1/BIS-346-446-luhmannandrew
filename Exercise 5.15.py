from operator import itemgetter

invoices = [(83, 'Electric sander', 7, 57.98), 
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77, 'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50)]
    

# sorting tuple for part and description
for part, desc, quant, price in sorted(invoices, key=itemgetter(1)):
    print(f'{part:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
# sorting tuple for price
for part, desc, quant, price in sorted(invoices, key=itemgetter(3)):
    print(f'{part:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
# return new tuples of part desc and quantity, print
quantities = [(desc, quant) for part, desc, quant, price in invoices]
for desc, quant in sorted(quantities, key=itemgetter(1)):
    print(f'{desc:<16}{quant:>3}')
    
# return new tuples of part desc and price, print
prices = [(desc, quant * price) for part, desc, quant, price in invoices]
for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
# return new tuples of part desc and price, print in the range $200 to $500.
prices = [(desc, quant * price) for part, desc, quant, price in invoices\
          if 200 <= quant * price <= 500]
for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
# Calculate the total of all the invoices. 
total = sum([(quant * price) for part, desc, quant, price in invoices])
print(f'Total for all invoices is: {total:.2f}')
