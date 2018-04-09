# String Interpolation with Python

Name='Renjith'
Distance=12

# Message='|%sThe Employee %s need to travel %s kilometers daily %s|' % (''.ljust(10), Name,Distance, ''.rjust(10)) # Correct way

Message='|          The Employee %s need to travel %s kilometers daily           |' % (Name,Distance)


print('==============================================================================')
print('|                                                                            |')
print(Message)
print('|                                                                            |')
print('==============================================================================')
