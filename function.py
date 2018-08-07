
def fn():
    for i in range(1,10):
        for j in range(1,i):
	    print('%s * %s = %s' % (j, i,j * i), end='\t')
        print('')

fn()
