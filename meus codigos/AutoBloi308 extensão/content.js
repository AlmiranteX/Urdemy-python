var Numero = 0
var Gm = true
var motor = NaN

function iniciar (){
    // responsavel por participar e mudar aba
    motor = setInterval(() => {
                
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

            if (Gm== true) {
                document.querySelectorAll('a')[1].click()
                Gm = false
            }else{
                document.querySelectorAll('a')[6].click()
                Gm = true
            }
        
        }
            
    }, 5000);

}



chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {

        if (request.mensagem === "Iniciar") {
            
            //window.location.href = "https://bloi308.com/sorteios?ref=OdxkK5x8G0Uu12wFOEp3rlY4yh53&tab=sweepstakes6#";
            
        
            // excluir abas de pagos para evita acidentes de aposta com saldo
            setTimeout(() => {
                for (let i = 0; i  < Number(document.querySelectorAll('li').length) ; i++){
                    if (i == 0 || i == 5 || i == 7){
                        continue
                    }else{
                        document.querySelectorAll('li')[i].style.display = 'none'
                    }
                }
            }, 5);
    
            iniciar()
            
            //repassa que recebeu a mensagem
            sendResponse({resposta: "O bot foi iniciado"});
    
        };
        if (request.mensagem === "Parar") {
            clearInterval(motor);

            window.location.assign("https://bloi308.com/sorteios?ref=OdxkK5x8G0Uu12wFOEp3rlY4yh53&tab=sweepstakes2");

        };
})


