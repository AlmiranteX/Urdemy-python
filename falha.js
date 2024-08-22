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
                    clear()
                    console.log('Erro ao participar')
   
                }
            
            }
            
        } catch (error) {
            // jonata
        }
       
}, 190000);

