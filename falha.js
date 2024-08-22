var maquina = true
var modo = true
clear()

setInterval(() => {

    
        try {
            
            qtd_elementos = document.querySelectorAll('div#sweepstakes-list')[0].childElementCount

            for (let i = 0; i < qtd_elementos; i++) {

                try {
                    document.querySelectorAll('button.btn-participate')[i].click()
                } catch (error) {
                    
                    //okbb
        
                    console.log('Erro ao participar')
                    
                }
            
            }
            
            

            
        } catch (error) {
            
            console.log('erro ao entra em gratuitos')
        }
       
}, 100000);

setInterval(() => {
    try {
        document.querySelectorAll('a')[1].click()
    } catch (error) {
        //ok
    }
    setInterval(() => {
        try {
            document.querySelectorAll('a')[6].click()
        } catch (error) {
            //ok
        }
    }, 80000);
}, 80000);