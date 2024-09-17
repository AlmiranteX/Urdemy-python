
def saldacao(msg):
    return msg

def executar(func_salda, *texto):
    return func_salda(texto)

print(
    *executar(saldacao, 'Jonatas', 'araujo')
)


#v = *'1', 'k'
#print(*v)