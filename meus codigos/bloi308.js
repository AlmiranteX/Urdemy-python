
function participar() {
    itens = document.querySelectorAll('button.btn-participate').length
    for (let i = 0; i < itens; i++) {

        try {
            document.querySelectorAll('button.btn-participate')[i].click()
            clear()
            console.log('Participando: '+i)

        } catch (error) {
            clear()
            console.log('Aconteceu um error: ' + error)
            continue
        }
                  
    }
}

participar()