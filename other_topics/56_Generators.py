''' 
Generators :
Easier way to create iterators.
Produces values once at a time.
it uses yield inastead of return.

yield :
Returns a value from the generator and suspends the execution of the function until next value is requested.
'''

def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))